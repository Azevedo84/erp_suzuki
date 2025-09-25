import sys
from banco_dados.conexao import conecta
from forms.tela_pi_vinculos import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import layout_cabec_tab, lanca_tabela, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback


class TelaPiVincular(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Vinculos)
        layout_cabec_tab(self.table_OC)
        layout_cabec_tab(self.table_OP)

        self.table_OC.viewport().installEventFilter(self)
        self.table_OP.viewport().installEventFilter(self)

        self.line_Num.editingFinished.connect(self.verifica_line_num_pi)

        self.combo_Produto.activated.connect(self.lanca_vinculos_pi)

        self.oc_pendentes()
        self.op_pendentes()

        self.processando = False

    def trata_excecao(self, nome_funcao, mensagem, arquivo, excecao):
        try:
            tb = traceback.extract_tb(excecao)
            num_linha_erro = tb[-1][1]

            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}"\n{mensagem} {num_linha_erro}')
            self.mensagem_alerta(f'Houve um problema no arquivo:\n\n{arquivo}\n\n'
                                 f'Comunique o desenvolvedor sobre o problema descrito abaixo:\n\n'
                                 f'{nome_funcao}: {mensagem}')

            grava_erro_banco(nome_funcao, mensagem, arquivo, num_linha_erro)

        except Exception as e:
            nome_funcao_trat = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            tb = traceback.extract_tb(exc_traceback)
            num_linha_erro = tb[-1][1]
            print(f'Houve um problema no arquivo: {self.nome_arquivo} na função: "{nome_funcao_trat}"\n'
                  f'{e} {num_linha_erro}')
            grava_erro_banco(nome_funcao_trat, e, self.nome_arquivo, num_linha_erro)

    def mensagem_alerta(self, mensagem):
        try:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setText(mensagem)
            alert.setWindowTitle("Atenção")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_num_pi(self):
        if not self.processando:
            try:
                self.processando = True

                num_ped = self.line_Num.text()
                if num_ped:
                    if int(num_ped) == 0:
                        self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                        self.line_Num.clear()
                    else:
                        self.verifica_sql_pi()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def verifica_sql_pi(self):
        try:
            num_ped = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT * FROM pedidointerno where id = {num_ped};")
            detalhes = cursor.fetchall()
            if not detalhes:
                self.mensagem_alerta('Este número de pedido não existe!')
                self.line_Num.clear()
            else:
                self.lanca_dados_pi()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_pi(self):
        try:
            num_ped = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT pi.emissao, cli.razao, pi.solicitante, "
                           f"COALESCE(pi.num_req_cliente, '') as req, "
                           f"pi.nome_pc, pi.status, COALESCE(pi.obs, '') as obs "
                           f"FROM PEDIDOINTERNO as pi "
                           f"INNER JOIN clientes as cli ON pi.id_cliente = cli.id "
                           f"where pi.id = {num_ped} "
                           f"and pi.status = 'A';")
            dados_interno = cursor.fetchall()
            if dados_interno:
                emissao, cliente, solicitante, num_req, pc, status, obs = dados_interno[0]

                self.date_Emissao.setDate(emissao)

                self.line_Solicitante.setText(solicitante)

                self.line_Cliente.setText(cliente)

                self.lanca_combo_produto()

            else:
                self.mensagem_alerta("Este Pedido Interno está encerrado!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_produto(self):
        try:
            tabela = []

            num_ped = self.line_Num.text()

            self.combo_Produto.clear()
            tabela.append("")

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, "
                           f"prod.unidade, prodint.qtde, prodint.data_previsao, prodint.status "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where ped.id = {num_ped};")
            dados_produtos = cursor.fetchall()

            for dadus in dados_produtos:
                cod, descr, ref, um, qtde, entrega, status = dadus
                tabela.append(f"{cod} - {descr}")

            self.combo_Produto.addItems(tabela)

            self.combo_Produto.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_vinculos_pi(self):
        try:
            num_ped = self.line_Num.text()

            produto = self.combo_Produto.currentText()
            if produto and num_ped:
                produtotete = produto.find(" - ")
                cod_produto = produto[:produtotete]

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, descricao "
                               f"FROM produto where codigo = {cod_produto};")
                detalhes_produto = cursor.fetchall()
                id_prod = detalhes_produto[0][0]

                cursor = conecta.cursor()
                cursor.execute(f'SELECT * FROM VINCULO_PRODUTO_PI '
                               f'where id_produto = {id_prod} and id_pedidointerno = {num_ped};')
                lista_completa = cursor.fetchall()
                print(lista_completa)
                if lista_completa:
                    lanca_tabela(self.table_Vinculos, lista_completa)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def oc_pendentes(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, forn.razao "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"LEFT JOIN produtoordemSOLICITACAO as prodsol ON prodreq.id_prod_sol = prodsol.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.entradasaida = 'E' AND oc.STATUS = 'A' AND prodoc.produzido < prodoc.quantidade "
                f"ORDER BY oc.numero;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                lanca_tabela(self.table_OC, dados_oc)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def op_pendentes(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"select ordser.numero, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"ordser.quantidade "
                           f"from ordemservico as ordser "
                           f"INNER JOIN produto prod ON ordser.produto = prod.id "
                           f"where ordser.status = 'A' order by ordser.numero;")
            op_abertas = cursor.fetchall()

            if op_abertas:
                lanca_tabela(self.table_OP, op_abertas)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, source, event):
        try:
            dados_tabela_vinculo = extrair_tabela(self.table_Vinculos)

            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_OC.viewport()):
                item = self.table_OC.currentItem()

                num_pi = self.line_Num.text()
                produto = self.combo_Produto.currentText()

                if item is None:
                    return super(QMainWindow, self).eventFilter(source, event)

                if num_pi and produto:
                    item = self.table_OC.currentItem()

                    extrai_recomendados = extrair_tabela(self.table_OC)
                    item_selecionado = extrai_recomendados[item.row()]

                    num_oc, cod, descr, ref, um, qtde, fornecedor = item_selecionado

                    dados = (num_oc, "OC", cod, descr, ref, um)
                    dados_tabela_vinculo.append(dados)

            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_OP.viewport()):
                item = self.table_OP.currentItem()

                num_pi = self.line_Num.text()
                produto = self.combo_Produto.currentText()

                if item is None:
                    return super(QMainWindow, self).eventFilter(source, event)

                if num_pi and produto:
                    item = self.table_OP.currentItem()

                    extrai_recomendados = extrair_tabela(self.table_OP)
                    item_selecionado = extrai_recomendados[item.row()]

                    num_op, cod, descr, ref, um, qtde = item_selecionado

                    dados = (num_op, "OP", cod, descr, ref, um)
                    dados_tabela_vinculo.append(dados)

            if dados_tabela_vinculo:
                lanca_tabela(self.table_Vinculos, dados_tabela_vinculo)


            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPiVincular()
    tela.show()
    qt.exec_()
