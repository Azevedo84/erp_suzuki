import sys
from banco_dados.conexao import conecta
from forms.tela_nf_compra_incluir import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela, layout_cabec_tab, extrair_tabela
from comandos.lines import definir_data_atual
from comandos.telas import tamanho_aplicacao, icone
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback


class TelaNFCompraIncluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.processando = False

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_compra_sol.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_OC_Abertas)
        layout_cabec_tab(self.table_Produtos_NF)

        self.line_CodForn.editingFinished.connect(self.verifica_line_fornecedor)
        self.line_Codigo.editingFinished.connect(self.verifica_line_codigo)

        self.table_OC_Abertas.viewport().installEventFilter(self)

        definir_data_atual(self.date_Entrega)
        self.definir_validador()
        self.definir_bloqueios()
        self.definir_combo_localestoque()

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

    def definir_bloqueios(self):
        try:
            self.line_NomeForn.setReadOnly(True)

            self.line_Descricao.setReadOnly(True)
            self.line_UM.setReadOnly(True)
            self.line_ValorTotal.setReadOnly(True)

            self.line_Total_Merc.setReadOnly(True)
            self.line_Total_Ipi.setReadOnly(True)
            self.line_Total_Geral.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_validador(self):
        try:
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Num_NF)
            self.line_Num_NF.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Num_OC)
            self.line_Num_OC.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_CodForn)
            self.line_CodForn.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Codigo)
            self.line_Codigo.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.000, 3, self.line_Qtde)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Qtde.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 999.00, 2, self.line_Ipi)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Ipi.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.0000, 4, self.line_Unit)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Unit.setValidator(validator)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_localestoque(self):
        try:
            tabela = []
            cur = conecta.cursor()
            cur.execute(f"SELECT id, nome FROM LOCALESTOQUE order by nome;")
            detalhes = cur.fetchall()

            for dadus in detalhes:
                ides, local = dadus
                tabela.append(local)

            self.combo_Local_Estoque.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_fornecedor(self):
        if not self.processando:
            try:
                self.processando = True

                cod_fornecedor = self.line_CodForn.text()
                if not cod_fornecedor:
                    self.mensagem_alerta('O campo "Cód. For.:" não pode estar vazio')
                    self.line_CodForn.clear()
                    self.line_CodForn.setFocus()
                elif int(cod_fornecedor) == 0:
                    self.mensagem_alerta('O campo "Cód. For.:" não pode ser "0"')
                    self.line_CodForn.clear()
                    self.line_CodForn.setFocus()
                else:
                    self.verifica_sql_fornecedor()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def verifica_sql_fornecedor(self):
        try:
            cod_fornecedor = self.line_CodForn.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()

            if not dados_fornecedor:
                self.mensagem_alerta('Este Código de Fornecedor não existe!')
                self.line_CodForn.clear()
                self.line_CodForn.setFocus()
            else:
                nom_fornecedor = dados_fornecedor[0][1].strip()
                self.line_NomeForn.setText(nom_fornecedor)
                self.line_Codigo.setFocus()

            self.oc_total_aberto_por_fornec(cod_fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def oc_total_aberto_por_fornec(self, cod_fornecedor):
        try:
            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, prodoc.item, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"LEFT JOIN produtoordemSOLICITACAO as prodsol ON prodreq.id_prod_sol = prodsol.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.entradasaida = 'E' "
                f"AND oc.STATUS = 'A' "
                f"AND prodoc.produzido < prodoc.quantidade and forn.registro = {cod_fornecedor} "
                f"ORDER BY oc.numero;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    oc, item_oc, cod, descr, ref, um, qtde = i

                    dados = (oc, item_oc, cod, descr, ref, um, qtde)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC_Abertas, tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, sources, event):
        try:
            nome_tabela = self.table_OC_Abertas

            if (event.type() == QtCore.QEvent.MouseButtonDblClick and event.buttons() == QtCore.Qt.LeftButton
                    and sources is nome_tabela.viewport()):

                item = nome_tabela.currentItem()

                if item:
                    extrai_recomendados = extrair_tabela(nome_tabela)
                    item_sel = extrai_recomendados[item.row()]

                    num_oc, item_oc, cod_prod, descr, ref, um, qtde = item_sel

                    self.line_Codigo.setText(cod_prod)
                    self.line_Descricao.setText(descr)
                    self.line_Referencia.setText(ref)
                    self.line_UM.setText(um)

                    self.line_Num_OC.setText(num_oc)
                    self.line_Item_OC.setText(item_oc)

                    self.line_NCM.setFocus()

            return super(QMainWindow, self).eventFilter(sources, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_codigo(self):
        if not self.processando:
            try:
                self.processando = True

                print("entrei")

                cod_produto = self.line_Codigo.text()

                self.line_Descricao.clear()
                self.line_Referencia.clear()
                self.line_UM.clear()
                self.line_Qtde.clear()
                self.line_Unit.clear()
                self.line_Ipi.clear()
                self.line_ValorTotal.clear()

                if cod_produto:
                    if int(cod_produto) == 0:
                        self.mensagem_alerta('O campo "Código:" não pode ser "0"')
                        self.limpa_dados_produtos()
                        self.line_Codigo.setFocus()
                    else:
                        self.verifica_sql_codigo(cod_produto)

                else:
                    self.limpa_dados_produtos()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def verifica_sql_codigo(self, cod_produto):
        try:
            cur = conecta.cursor()
            cur.execute(f"SELECT prod.descricao, COALESCE(prod.obs, '') , prod.unidade, "
                        f"prod.localizacao, prod.quantidade, conj.conjunto, prod.embalagem "
                        f"FROM produto as prod "
                        f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                        f"where codigo = {cod_produto};")
            detalhes_produto = cur.fetchall()

            if not detalhes_produto:
                self.mensagem_alerta('Este Código de Produto não existe!')
                self.limpa_dados_produtos()
                self.line_Codigo.setFocus()
            else:
                self.lanca_dados_codigo(cod_produto, detalhes_produto)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_codigo(self, cod_produto, detalhes_produto):
        try:
            descricao, referencia, un, local, saldo, conj, embalagem = detalhes_produto[0]

            self.line_Descricao.setText(descricao)
            self.line_UM.setText(un)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_dados_produtos(self):
        try:
            self.line_Codigo.clear()
            self.line_Descricao.clear()
            self.line_Referencia.clear()
            self.line_UM.clear()

            self.line_Qtde.clear()
            self.line_Unit.clear()
            self.line_Ipi.clear()
            self.line_ValorTotal.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaNFCompraIncluir()
    tela.show()
    qt.exec_()
