import xml.etree.ElementTree as ET
import os

# Caminho do arquivo XML
caminho_xml = os.path.expanduser("~/Desktop/35250613743249000139550010001562461121645934-nfe.xml")

# Carregar e parsear o XML
tree = ET.parse(caminho_xml)
root = tree.getroot()

# Namespace padrão do XML da NF-e
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

# Encontra o nó principal da nota
infNFe = root.find('.//nfe:infNFe', ns)

# Dados do emitente
emitente = infNFe.find('nfe:emit', ns)
nome_emitente = emitente.find('nfe:xNome', ns).text
cnpj_emitente = emitente.find('nfe:CNPJ', ns).text

# Dados do destinatário
destinatario = infNFe.find('nfe:dest', ns)
nome_destinatario = destinatario.find('nfe:xNome', ns).text
cnpj_destinatario = destinatario.find('nfe:CNPJ', ns)
cnpj_destinatario = cnpj_destinatario.text if cnpj_destinatario is not None else "CPF (provavelmente)"

# Dados da nota
ide = infNFe.find('nfe:ide', ns)
data_emissao = ide.find('nfe:dhEmi', ns).text

# Valor total
total = infNFe.find('nfe:total', ns)
valor_total = total.find('nfe:ICMSTot/nfe:vNF', ns).text

# Exibir resultados
print(f"Emitente: {nome_emitente} (CNPJ: {cnpj_emitente})")
print(f"Destinatário: {nome_destinatario} (CNPJ/CPF: {cnpj_destinatario})")
print(f"Data de Emissão: {data_emissao}")
print(f"Valor Total da Nota: R$ {valor_total}")

# Produtos detalhados
detalhes = infNFe.findall('nfe:det', ns)
print(f"{'CÓDIGO':<10} {'DESCRIÇÃO':<40} {'NCM':<10} {'CST':<5} {'CFOP':<6} {'UN':<4} {'QTD':>6} {'VL UNIT':>10} {'VL TOTAL':>10} {'BC ICMS':>10} {'VL ICMS':>10} {'BC IPI':>10} {'VL IPI':>10} {'ALQ ICMS':>8} {'ALQ IPI':>7}")
print("-" * 150)

for det in detalhes:
    prod = det.find('nfe:prod', ns)
    imposto = det.find('nfe:imposto', ns)

    # Dados principais
    cProd = prod.findtext('nfe:cProd', default='', namespaces=ns)
    xProd = prod.findtext('nfe:xProd', default='', namespaces=ns)
    NCM = prod.findtext('nfe:NCM', default='', namespaces=ns)
    CFOP = prod.findtext('nfe:CFOP', default='', namespaces=ns)
    uCom = prod.findtext('nfe:uCom', default='', namespaces=ns)
    qCom = prod.findtext('nfe:qCom', default='0', namespaces=ns)
    vUnCom = prod.findtext('nfe:vUnCom', default='0', namespaces=ns)
    vProd = prod.findtext('nfe:vProd', default='0', namespaces=ns)

    # Impostos
    # ICMS
    icms = imposto.find('.//nfe:ICMS', ns)
    cst_icms = ''
    bc_icms = vl_icms = alq_icms = ''
    if icms is not None:
        icms_tag = list(icms)[0]  # Pode ser ICMS00, ICMS10, etc.
        cst_icms = icms_tag.findtext('nfe:CST', default='', namespaces=ns)
        bc_icms = icms_tag.findtext('nfe:vBC', default='', namespaces=ns)
        vl_icms = icms_tag.findtext('nfe:vICMS', default='', namespaces=ns)
        alq_icms = icms_tag.findtext('nfe:pICMS', default='', namespaces=ns)

    # IPI
    ipi = imposto.find('.//nfe:IPI', ns)
    cst_ipi = ''
    bc_ipi = vl_ipi = alq_ipi = ''
    if ipi is not None:
        ipi_tag = ipi.find('.//nfe:IPITrib', ns)
        if ipi_tag is not None:
            cst_ipi = ipi.findtext('nfe:CST', default='', namespaces=ns)
            bc_ipi = ipi_tag.findtext('nfe:vBC', default='', namespaces=ns)
            vl_ipi = ipi_tag.findtext('nfe:vIPI', default='', namespaces=ns)
            alq_ipi = ipi_tag.findtext('nfe:pIPI', default='', namespaces=ns)

    print(f"{cProd:<10} {xProd[:38]:<40} {NCM:<10} {cst_icms:<5} {CFOP:<6} {uCom:<4} {qCom:>6} {vUnCom:>10} {vProd:>10} {bc_icms:>10} {vl_icms:>10} {bc_ipi:>10} {vl_ipi:>10} {alq_icms:>8} {alq_ipi:>7}")

infAdic = infNFe.find('nfe:infAdic', ns)
inf_cpl = infAdic.findtext('nfe:infCpl', default='', namespaces=ns) if infAdic is not None else ''

print(f"Informações Complementares: {inf_cpl}")

from banco_dados.conexao import conecta

cursor = conecta.cursor()
cursor.execute(
    f"SELECT oc.numero, prodoc.item, prodoc.codigo, "
    f"prod.descricao, COALESCE(prod.obs, ''), "
    f"prod.unidade, (prodoc.quantidade - prodoc.produzido) "
    f"FROM ordemcompra as oc "
    f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
    f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
    f"LEFT JOIN produtoordemSOLICITACAO as prodsol ON prodreq.id_prod_sol = prodsol.id "
    f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
    f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
    f"where oc.entradasaida = 'E' "
    f"AND oc.STATUS = 'A' "
    f"AND prodoc.produzido < prodoc.quantidade "
    f"ORDER BY oc.numero;")
dados_oc = cursor.fetchall()

if dados_oc:
    for i in dados_oc:
        oc, item_oc, cod, descr, ref, um, qtde = i