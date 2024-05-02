import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import grava_erro_banco
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget_cab
from forms.tela_op_excluir import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import datetime, date
import inspect
import os
import traceback


class TelaOpExcluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_producao.png")
        tamanho_aplicacao(self)
        self.layout_tabela(self.table_Lista)
        cor_widget_cab(self.widget_cabecalho)

        self.table_Lista.viewport().installEventFilter(self)

        self.line_Num.editingFinished.connect(self.verifica_line_op)
        self.verificacao_em_andamento = False

        self.btn_Excluir.clicked.connect(self.verifica_salvamento)
        self.btn_Limpar.clicked.connect(self.limpar_produto)

        self.define_tabela()
        self.line_Num.setFocus()

    def trata_excecao(self, nome_funcao, mensagem, arquivo):
        try:
            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}"\n{mensagem}')
            self.mensagem_alerta(f'Houve um problema no arquivo:\n\n{arquivo}\n\n'
                                 f'Comunique o desenvolvedor sobre o problema descrito abaixo:\n\n'
                                 f'{nome_funcao}: {mensagem}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

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
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def layout_tabela(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 70)
            nome_tabela.setColumnWidth(1, 70)
            nome_tabela.setColumnWidth(2, 40)
            nome_tabela.setColumnWidth(3, 40)
            nome_tabela.setColumnWidth(4, 220)
            nome_tabela.setColumnWidth(5, 120)
            nome_tabela.setColumnWidth(6, 40)
            nome_tabela.setColumnWidth(7, 60)
            nome_tabela.setColumnWidth(8, 60)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_line_op(self):
        try:
            if not self.verificacao_em_andamento:
                self.verificacao_em_andamento = True

                num_op = self.line_Num.text()
                if num_op:
                    if int(num_op) == 0:
                        self.mensagem_alerta('O campo "Código" não pode ser "0"')
                        self.line_Num.clear()
                        self.limpar_produto()
                    else:
                        self.verifica_sql_op()

                self.verificacao_em_andamento = False

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_sql_op(self):
        try:
            num_op = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"select * from ordemservico "
                           f"where numero = {num_op};")
            select_numero = cursor.fetchall()

            if not select_numero:
                self.mensagem_alerta('Este número de OP não existe!')
                self.line_Num.clear()
                self.limpar_produto()
            else:
                self.verifica_status_op()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_status_op(self):
        try:
            num_op = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"select * from ordemservico "
                           f"where numero = {num_op} and status = 'A';")
            select_status = cursor.fetchall()

            if select_status:
                cursor = conecta.cursor()
                cursor.execute(f"select count(id) from produtoos where numero = {num_op};")
                total_itens_consumo = cursor.fetchall()
                itens_consumo_limpa = total_itens_consumo[0]
                itens_consumo = itens_consumo_limpa[0]
                if itens_consumo == 0:
                    self.lanca_dados_op()
                else:
                    self.mensagem_alerta(f'A OP {num_op} tem material consumido e '
                                                                f'não pode ser excluída!')
                    self.line_Num.clear()

            else:
                self.mensagem_alerta('Esta OP está encerrada!')
                self.line_Num.clear()
                self.limpar_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_dados_op(self):
        try:
            num_op = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ord.numero, produto.codigo, produto.descricao, "
                           f"COALESCE(produto.obs, '') as obs, produto.unidade, ord.quantidade, ord.datainicial "
                           f"FROM ordemservico as ord "
                           f"INNER JOIN produto ON ord.produto = produto.id "
                           f"where ord.numero = {num_op};")
            dados_op = cursor.fetchall()
            op, cod, descr, ref, um, qtde, emissao = dados_op[0]

            self.date_Emissao.setDate(emissao)
            self.line_Codigo.setText(cod)
            self.line_Descricao.setText(descr)
            self.line_Referencia.setText(ref)
            self.line_UM.setText(um)
            self.line_Qtde.setText(str(qtde))

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def eventFilter(self, source, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_Lista.viewport()):

                item = self.table_Lista.currentItem()

                extrai_tab_extrusora = extrair_tabela(self.table_Lista)
                item_selecionado = extrai_tab_extrusora[item.row()]
                emissao, previsao, op, cod, descr, ref, um, qtde, est_con = item_selecionado

                posicao = est_con.find("/")
                inicio = posicao + 1
                consumo = est_con[inicio:]
                if consumo == "0":
                    data_obj = datetime.strptime(emissao, "%d/%m/%Y").date()

                    self.line_Num.setText(op)
                    self.date_Emissao.setDate(data_obj)
                    self.line_Codigo.setText(cod)
                    self.line_Descricao.setText(descr)
                    self.line_Referencia.setText(ref)
                    self.line_UM.setText(um)
                    self.line_Qtde.setText(qtde)
                else:
                    self.mensagem_alerta(f'A OP {op} tem material consumido e '
                                                                f'não pdoe ser excluída!')

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def define_tabela(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, prod.codigo, "
                           f"prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"ordser.quantidade "
                           f"from ordemservico as ordser "
                           f"INNER JOIN produto prod ON ordser.produto = prod.id "
                           f"where ordser.status = 'A' order by ordser.numero;")
            op_abertas = cursor.fetchall()
            if op_abertas:
                op_ab_editado = []
                for dados_op in op_abertas:
                    emissao, previsao, op, cod, descr, ref, um, qtde = dados_op

                    data_em_texto = '{}/{}/{}'.format(emissao.day, emissao.month, emissao.year)

                    if previsao:
                        data_prev = '{}/{}/{}'.format(previsao.day, previsao.month, previsao.year)
                    else:
                        data_prev = ''

                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, codigo FROM produto where codigo = {cod};")
                    select_prod = cursor.fetchall()

                    idez, cod = select_prod[0]

                    cursor = conecta.cursor()
                    cursor.execute(f"select count(id) from materiaprima where mestre = {idez};")
                    total_itens_estrutura = cursor.fetchall()
                    itens_estrut_limpa = total_itens_estrutura[0]
                    itens_estrut = itens_estrut_limpa[0]

                    cursor = conecta.cursor()
                    cursor.execute(f"select count(id) from produtoos where numero = {op};")
                    total_itens_consumo = cursor.fetchall()
                    itens_consumo_limpa = total_itens_consumo[0]
                    itens_consumo = itens_consumo_limpa[0]

                    est_con = f"{itens_estrut}/{itens_consumo}"

                    if itens_consumo == 0:
                        dados = (data_em_texto, data_prev, op, cod, descr, ref, um, qtde, est_con)
                        op_ab_editado.append(dados)

                lanca_tabela(self.table_Lista, op_ab_editado)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpar_produto(self):
        try:
            self.line_Num.clear()
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)
            self.line_Codigo.clear()
            self.line_Descricao.clear()
            self.line_Referencia.clear()
            self.line_UM.clear()
            self.line_Qtde.clear()
            self.line_Num.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_salvamento(self):
        try:
            num_op = self.line_Num.text()
            if len(num_op) == 0:
                self.mensagem_alerta('O campo "Código" não pode estar vazio')
                self.line_Num.clear()
            elif int(num_op) == 0:
                self.mensagem_alerta('O campo "Código" não pode ser "0"')
                self.line_Num.clear()
            else:
                cursor = conecta.cursor()
                cursor.execute(f"select * from ordemservico "
                               f"where numero = {num_op};")
                select_numero = cursor.fetchall()

                if not select_numero:
                    self.mensagem_alerta('Este número de OP não existe!')
                    self.line_Num.clear()
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"select * from ordemservico "
                                   f"where numero = {num_op} and status = 'A';")
                    select_status = cursor.fetchall()

                    if select_status:
                        cursor = conecta.cursor()
                        cursor.execute(f"select count(id) from produtoos where numero = {num_op};")
                        total_itens_consumo = cursor.fetchall()
                        itens_consumo_limpa = total_itens_consumo[0]
                        itens_consumo = itens_consumo_limpa[0]
                        if itens_consumo == 0:
                            self.salvar_lista()
                        else:
                            self.mensagem_alerta(f'A OP {num_op} tem material consumido e '
                                                                        f'não pode ser excluída!')
                            self.line_Num.clear()

                    else:
                        self.mensagem_alerta('Esta OP está encerrada!')
                        self.line_Num.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_lista(self):
        try:
            num_op = self.line_Num.text()

            cursor = conecta.cursor()
            cursor.execute(f"DELETE FROM ordemservico WHERE numero = {num_op};")

            conecta.commit()
            self.mensagem_alerta(f'A OP {num_op} foi excluída com sucesso!')
            self.reinicia_tela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def reinicia_tela(self):
        try:
            self.define_tabela()
            self.line_Num.clear()
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)
            self.line_Codigo.clear()
            self.line_Descricao.clear()
            self.line_Referencia.clear()
            self.line_UM.clear()
            self.line_Qtde.clear()
            self.label_54.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaOpExcluir()
    tela.show()
    qt.exec_()
