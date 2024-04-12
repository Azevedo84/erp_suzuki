from banco_dados.conexao import conecta
from comandos.comando_notificacao import tratar_notificar_erros
import os
import inspect


class Produto:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_por_codigo(self, codigo_produto):
        try:
            cur = conecta.cursor()
            cur.execute(f"SELECT id, descricao, descricaocomplementar, obs, unidade, localizacao, quantidade, "
                        f"embalagem, kilosmetro, ncm, conjunto, terceirizado, tipomaterial "
                        f"FROM produto "
                        f"where codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()

            return detalhes_produto

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_acabado(self, codigo_produto):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, descricao, descricaocomplementar, obs, unidade, localizacao, quantidade, "
                           f"embalagem, kilosmetro, ncm "
                           f"FROM produto "
                           f"where codigo = {codigo_produto} "
                           f"AND conjunto = 10;")
            produto_acabado = cursor.fetchall()

            return produto_acabado

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


class ProdutoOrdemSolicitacao:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_por_produto_aberto(self, id_prod):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT mestre, quantidade, data "
                           f"from produtoordemsolicitacao "
                           f"where produto = {id_prod} and status = 'A';")
            select_solicitacao = cursor.fetchall()

            return select_solicitacao

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


class ProdutoOrdemRequisicao:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_por_produto_aberto(self, id_prod):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT numero, quantidade, data "
                           f"from produtoordemrequisicao "
                           f"where produto = {id_prod} and status = 'A';")
            select_requisicao = cursor.fetchall()

            return select_requisicao

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


class ProdutoOrdemCompra:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_por_produto_aberto(self, id_prod):
        try:
            # Foi colocado a data de "01-01-2021", pois antes disso as ordens eram controladas de forma diferente

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prodoc.numero, prodoc.quantidade, oc.data "
                           f"from produtoordemcompra as prodoc "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"where prodoc.produto = {id_prod} and (prodoc.quantidade - prodoc.produzido) > '0' "
                           f"and oc.status = 'A' and oc.entradasaida = 'E' and oc.data > '01-01-2021';")
            select_oc = cursor.fetchall()

            return select_oc

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


class Projeto:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_todos_itens(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, projeto FROM projeto order by projeto;")
            projetos = cursor.fetchall()

            return projetos

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def consulta_por_codigo_data(self, id_projeto, ano):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT pr.codigo, max(pr.descricao), COALESCE(max(pr.obs), ' '), max(pr.unidade), "
                           f"max(m.quantidade), COALESCE(max(pr.localizacao), ' '), max(pr.quantidade) "
                           f"FROM produto as pr "
                           f"INNER JOIN movimentacao as m ON m.codigo = pr.codigo "
                           f"WHERE pr.projeto = {id_projeto} and m.tipo = 130 "
                           f"AND m.DATA BETWEEN ('{ano}-01-01') AND 'now' "
                           f"group BY pr.codigo, m.codigo "
                           f"ORDER BY max(pr.descricao);")
            compras = cursor.fetchall()

            return compras

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


class MateriaPrima:
    def __init__(self):
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

    def consulta_estrutura_pro_produto(self, id_prod, qtde):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT mat.codigo, prod.descricao, prod.obs, prod.unidade,"
                           f"(mat.quantidade * {qtde}) as qtde, prod.localizacao, prod.quantidade "
                           f"from materiaprima as mat "
                           f"INNER JOIN produto prod ON mat.codigo = prod.codigo "
                           f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                           f"where mat.mestre = {id_prod} order by conj.conjunto DESC, prod.descricao ASC;")
            tabela_estrutura = cursor.fetchall()

            return tabela_estrutura

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)
