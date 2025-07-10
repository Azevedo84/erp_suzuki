from pynfe.processamento.comunicacao import ComunicacaoSefaz
from lxml import etree
import base64
import gzip
from io import BytesIO

# Configurações do certificado e empresa
certificado = r"C:\Users\Anderson\Downloads\Maquinas_1006652074.pfx"
senha = "unisold11"
CNPJ = "93183853000197"
chave_desejada = "43250609570840000164550010001451931164272590"
ambiente = False  # False = Produção (1) / True = Homologação (2)

# Extrair UF da chave
def extrair_uf_da_chave(chave):
    ufs = {
        "12": "AC", "27": "AL", "13": "AM", "16": "AP", "29": "BA", "23": "CE",
        "53": "DF", "32": "ES", "52": "GO", "21": "MA", "31": "MG", "50": "MS",
        "51": "MT", "15": "PA", "25": "PB", "26": "PE", "22": "PI", "41": "PR",
        "33": "RJ", "24": "RN", "11": "RO", "14": "RR", "43": "RS", "42": "SC",
        "28": "SE", "35": "SP", "17": "TO"
    }
    return ufs.get(chave[:2], "UF Desconhecida")

uf = extrair_uf_da_chave(chave_desejada)

# Comunicação com a SEFAZ
comunicacao = ComunicacaoSefaz(uf, certificado, senha, ambiente)

print("Consultando NF diretamente pela chave...")
resposta = comunicacao.consulta_distribuicao(cnpj=CNPJ, chave=chave_desejada)

xml_resposta = resposta.content
tree = etree.fromstring(xml_resposta)
doc_zip_elements = tree.findall('.//{http://www.portalfiscal.inf.br/nfe}docZip')

if not doc_zip_elements:
    print("❌ A NF com a chave especificada **não foi encontrada** nos documentos distribuídos.")
else:
    for doc_zip in doc_zip_elements:
        conteudo_zipado = base64.b64decode(doc_zip.text)
        with gzip.GzipFile(fileobj=BytesIO(conteudo_zipado)) as gz:
            xml_nfe = gz.read().decode('utf-8')
            print("✅ NF encontrada! Extraindo dados...")

            # Namespace do XML da NF-e
            ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

            tree_nfe = etree.fromstring(xml_nfe.encode('utf-8'))
            print(tree_nfe)
            infNFe = tree_nfe.find('.//nfe:infNFe', namespaces=ns)
            print("bahh", infNFe)

            # Dados gerais da NF-e
            ide = infNFe.find('nfe:ide', namespaces=ns)
            chave = infNFe.attrib.get('Id', '')[3:]
            numero_nf = ide.find('nfe:nNF', namespaces=ns).text
            data_emissao = ide.find('nfe:dhEmi', namespaces=ns).text

            print(f"Chave NF-e: {chave}")
            print(f"Número NF-e: {numero_nf}")
            print(f"Data de emissão: {data_emissao}")

            # Emitente
            emit = infNFe.find('nfe:emit', namespaces=ns)
            cnpj_emit = emit.find('nfe:CNPJ', namespaces=ns).text
            nome_emit = emit.find('nfe:xNome', namespaces=ns).text
            print(f"Emitente: {nome_emit} - CNPJ: {cnpj_emit}")

            # Destinatário
            dest = infNFe.find('nfe:dest', namespaces=ns)
            cnpj_dest = dest.find('nfe:CNPJ', namespaces=ns).text
            nome_dest = dest.find('nfe:xNome', namespaces=ns).text
            print(f"Destinatário: {nome_dest} - CNPJ: {cnpj_dest}")

            # Valor total da NF-e
            total = infNFe.find('nfe:total', namespaces=ns)
            vNF = total.find('nfe:ICMSTot/nfe:vNF', namespaces=ns).text
            print(f"Valor total NF-e: R$ {vNF}")

            # Produtos
            produtos = infNFe.findall('nfe:det', namespaces=ns)
            print(f"Produtos ({len(produtos)}):")
            for det in produtos:
                prod = det.find('nfe:prod', namespaces=ns)
                cProd = prod.find('nfe:cProd', namespaces=ns).text
                xProd = prod.find('nfe:xProd', namespaces=ns).text
                qCom = prod.find('nfe:qCom', namespaces=ns).text
                vUnCom = prod.find('nfe:vUnCom', namespaces=ns).text
                vProd = prod.find('nfe:vProd', namespaces=ns).text
                print(f" - Código: {cProd} | Produto: {xProd} | Quantidade: {qCom} | Valor Unitário: R$ {vUnCom} | Valor Total: R$ {vProd}")
