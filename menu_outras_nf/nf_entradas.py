import sys
from banco_dados.conexao import conecta
from forms.tela_nf_entrada_incluir_alterar import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import layout_cabec_tab, lanca_tabela, extrair_tabela
from comandos.lines import definir_data_atual
from comandos.telas import tamanho_aplicacao, icone
from comandos.conversores import data_pra_data_brasileiro
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback

import socket
import getpass


class TelaNFEntrada(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.processando = False

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        self.nome_computador = socket.gethostname()
        self.username = getpass.getuser()

        icone(self, "menu_compra_sol.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Produtos_NF)

        self.line_CodForn.editingFinished.connect(self.verifica_line_fornecedor)

        self.line_Codigo.editingFinished.connect(self.verifica_line_codigo)

        self.line_Nat_Operacao.editingFinished.connect(self.verifica_line_natureza)

        self.btn_AdicionarProd.clicked.connect(self.verifica_adicionar_produto)

        self.btn_Limpar.clicked.connect(self.limpar_tudo)

        definir_data_atual(self.date_Movimento)
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

    def pergunta_confirmacao(self, mensagem):
        try:
            confirmacao = QMessageBox()
            confirmacao.setIcon(QMessageBox.Question)
            confirmacao.setText(mensagem)
            confirmacao.setWindowTitle("Confirmação")

            sim_button = confirmacao.addButton("Sim", QMessageBox.YesRole)
            nao_button = confirmacao.addButton("Não", QMessageBox.NoRole)

            confirmacao.setDefaultButton(nao_button)

            confirmacao.exec_()

            if confirmacao.clickedButton() == sim_button:
                return True
            else:
                return False

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_bloqueios(self):
        try:
            self.line_NomeForn.setReadOnly(True)

            self.line_Descricao.setReadOnly(True)
            self.line_UM.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_validador(self):
        try:
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Num_NF)
            self.line_Num_NF.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_CodForn)
            self.line_CodForn.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Codigo)
            self.line_Codigo.setValidator(validator)

            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'\d+'), self.line_Nat_Operacao)
            self.line_Nat_Operacao.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.000, 3, self.line_Qtde)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Qtde.setValidator(validator)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_localestoque(self):
        try:
            self.combo_Local_Estoque.clear()

            tabela = []

            branco = ""
            tabela.append(branco)

            cur = conecta.cursor()
            cur.execute(f"SELECT id, nome FROM LOCALESTOQUE order by nome;")
            detalhes = cur.fetchall()

            for dadus in detalhes:
                ides, local = dadus
                msg = f"{ides} - {local}"
                tabela.append(msg)

            self.combo_Local_Estoque.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_fornecedor(self):
        if not self.processando:
            try:
                self.processando = True

                self.limpa_dados_produtos()
                self.line_Obs.clear()

                self.table_Produtos_NF.setRowCount(0)

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

                self.lanca_dados_nf(cod_fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_nf(self, cod_fornecedor):
        try:
            nova_tabela = []

            num_nf = self.line_Num_NF.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()

            id_forn = dados_fornecedor[0][0]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT entr.movimentacao, entr.ordemcompra "
                           f"FROM ENTRADAPROD as entr "
                           f"where entr.FORNECEDOR = {id_forn} "
                           f"and entr.nota = {num_nf};")
            dados_nf_oc = cursor.fetchall()

            if dados_nf_oc:
                id_mov, id_oc = dados_nf_oc[0]

                if id_oc:
                    self.mensagem_alerta("Esta Nota Fiscal tem ordem de compra vinculada!")
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT entr.movimentacao, mov.data, loc.nome, prod.codigo, prod.descricao, "
                                   f"COALESCE(prod.obs, ''), prod.unidade, entr.quantidade, prod.localizacao "
                                   f"FROM ENTRADAPROD as entr "
                                   f"INNER JOIN produto as prod ON entr.produto = prod.id "
                                   f"INNER JOIN movimentacao as mov ON entr.movimentacao = mov.id "
                                   f"INNER JOIN LOCALESTOQUE as loc ON mov.localestoque = loc.id "
                                   f"where entr.FORNECEDOR = {id_forn} "
                                   f"and entr.nota = {num_nf};")
                    dados_nf = cursor.fetchall()

                    if dados_nf:
                        for i in dados_nf:
                            id_mov, data_mov, local_est, cod, descr, ref, um, qtde, local = i

                            data_mov_br = data_pra_data_brasileiro(data_mov)

                            dados = (id_mov, data_mov_br, local_est, cod, descr, ref, um, qtde, local)
                            nova_tabela.append(dados)

                        lanca_tabela(self.table_Produtos_NF, nova_tabela)


        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_codigo(self):
        if not self.processando:
            try:
                self.processando = True

                cod_produto = self.line_Codigo.text()

                self.limpa_dados_produtos()

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
            descricao, referencia, um, local, saldo, conj, embalagem = detalhes_produto[0]

            itens_encontrados = []

            dados_tabela = extrair_tabela(self.table_Produtos_NF)
            for i in dados_tabela:
                if cod_produto in i:
                    id_mov, data_mov_br, local_est, cod, descr, ref, um, qtde, local = i
                    tt = (cod, descr, ref, um, qtde)
                    itens_encontrados.append(tt)

            if itens_encontrados:
                self.mensagem_alerta('O produto já foi adicionado a essa NF!')
                self.limpa_dados_produtos()
                self.line_Codigo.setFocus()
            else:
                self.line_Codigo.setText(cod_produto)
                self.line_Descricao.setText(descricao)
                self.line_Referencia.setText(referencia)
                self.line_UM.setText(um)

                self.line_Local.setText(local)

                self.combo_Local_Estoque.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_natureza(self):
        if not self.processando:
            try:
                self.processando = True

                cod_nat = self.line_Nat_Operacao.text()

                if cod_nat:
                    if int(cod_nat) == 0:
                        self.mensagem_alerta('O campo "Nat. Op.:" não pode ser "0"')
                        self.line_Nat_Operacao.clear()
                        self.line_Nat_Operacao.setFocus()
                    else:
                        self.verifica_sql_natureza(cod_nat)

                else:
                    self.line_Nat_Operacao.clear()
                    self.line_Nat_Operacao.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def verifica_sql_natureza(self, cod_nat):
        try:
            cur = conecta.cursor()
            cur.execute(f"SELECT CFOP, DESCRICAO "
                        f"FROM NATOP "
                        f"where CFOP = {cod_nat};")
            detalhes_natureza = cur.fetchall()

            if not detalhes_natureza:
                self.mensagem_alerta('Este CFOP não existe!')
                self.line_Nat_Operacao.clear()
                self.line_Nat_Operacao.setFocus()
            else:
                descricao = detalhes_natureza[0][1]
                self.label_Natureza.setText(descricao)

                self.btn_AdicionarProd.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_adicionar_produto(self):
        try:
            cod_prod = self.line_Codigo.text()

            qtde = self.line_Qtde.text()

            nat_op = self.line_Nat_Operacao.text()

            if not cod_prod:
                self.mensagem_alerta("O código do produto não foi definido!")
            elif not qtde:
                self.mensagem_alerta("A Quantidade não foi definida!")
            elif not nat_op:
                self.mensagem_alerta("A Natureza de Operação não foi definida!")
            else:
                self.adicionar_produto_na_tabela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def adicionar_produto_na_tabela(self):
        try:
            nova_tabela = []

            emissao_oc = self.date_Movimento.date()
            data_mov = emissao_oc.toString("dd/MM/yyyy")

            cod_prod = self.line_Codigo.text()
            descr = self.line_Descricao.text()
            ref = self.line_Referencia.text()
            um = self.line_UM.text()

            qtde = self.line_Qtde.text()

            local_est = self.combo_Local_Estoque.currentText()

            local = self.line_Local.text()

            dados = ["", data_mov, local_est, cod_prod, descr, ref, um, qtde, local]

            extrai_produtos = extrair_tabela(self.table_Produtos_NF)

            if extrai_produtos:
                for i in extrai_produtos:
                    nova_tabela.append(i)

            nova_tabela.append(dados)

            lanca_tabela(self.table_Produtos_NF, nova_tabela)

            self.table_Produtos_NF.scrollToBottom()

            self.limpa_dados_produtos()

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
            self.line_Nat_Operacao.clear()
            self.definir_combo_localestoque()

            self.line_Qtde.clear()
            self.line_Local.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_dados_fornecedor(self):
        try:
            self.line_CodForn.clear()
            self.line_NomeForn.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpar_tudo(self):
        try:
            self.line_Num_NF.clear()

            self.limpa_dados_produtos()
            self.limpa_dados_fornecedor()
            self.line_Obs.clear()

            self.table_Produtos_NF.setRowCount(0)

            definir_data_atual(self.date_Movimento)

            self.line_Num_NF.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaNFEntrada()
    tela.show()
    qt.exec_()
