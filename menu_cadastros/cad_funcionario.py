import sys
from banco_dados.conexao import conecta
from forms.tela_cad_funcionario import *
from banco_dados.controle_erros import grava_erro_banco
from banco_dados.bc_consultas import definir_proximo_registro
from comandos.tabelas import lanca_tabela, layout_cabec_tab, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from comandos.lines import validador_so_numeros
from comandos.conversores import timestamp_brasileiro
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
from datetime import date
import traceback
from unidecode import unidecode


class TelaCadastroFuncionario(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Lista)

        self.lanca_numero_id()
        self.definir_data_emissao()
        self.manipula_dados_tabela()

        validador_so_numeros(self.line_Num)
        self.line_Num.setReadOnly(True)

        self.table_Lista.viewport().installEventFilter(self)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)
        self.btn_Limpar.clicked.connect(self.reiniciando_tela)
        self.btn_Excluir.clicked.connect(self.excluir_cadastro)

        self.btn_Consulta.clicked.connect(self.procura_palavra)
        self.line_Consulta.returnPressed.connect(lambda: self.procura_palavra())

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
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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

    def lanca_numero_id(self):
        try:
            definir_proximo_registro(self.line_Num, "id", "funcionarios")
            self.line_Descricao.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_data_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela(self):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"select id, criacao, "
                           f"funcionario, COALESCE(ativo, '') "
                           f"from funcionarios "
                           f"where id <> 0 "
                           f"order by funcionario;")
            select_numero = cursor.fetchall()

            if select_numero:
                for i in select_numero:
                    id_func, data, nome, ativo = i

                    data_formatada = timestamp_brasileiro(data)

                    dados = (id_func, data_formatada, nome, ativo)
                    tabela_nova.append(dados)

            if tabela_nova:
                lanca_tabela(self.table_Lista, tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def reiniciando_tela(self):
        try:
            self.line_Descricao.clear()
            self.check_Ativo.setChecked(False)
            self.line_Consulta.clear()

            self.lanca_numero_id()
            self.manipula_dados_tabela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def procura_palavra(self):
        try:
            tabela_nova = []

            palavra_consulta = self.line_Consulta.text()

            if not palavra_consulta:
                self.mensagem_alerta(f'O Campo "Consulta Nome" não pode estar vazio!')
                self.line_Consulta.clear()
            else:
                palavra_maiuscula = palavra_consulta.upper()

                cursor = conecta.cursor()
                cursor.execute(f"SELECT DISTINCT id, criacao, "
                               f"funcionario, COALESCE(ativo, '') "
                               f"FROM funcionarios "
                               f"WHERE funcionario LIKE '%{palavra_maiuscula}%' and id <> 0 "
                               f"ORDER BY funcionario;")
                palavra = cursor.fetchall()

                if not palavra:
                    self.mensagem_alerta(f'Não foi encontrado nenhum item com o nome:\n  "{palavra_consulta}"!')
                    self.line_Consulta.clear()
                else:
                    for i in palavra:
                        id_func, data, nome, ativo = i

                        data_formatada = timestamp_brasileiro(data)

                        dados = (id_func, data_formatada, nome, ativo)
                        tabela_nova.append(dados)

                if tabela_nova:
                    lanca_tabela(self.table_Lista, tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, source, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_Lista.viewport()):
                item = self.table_Lista.currentItem()

                extrai_recomendados = extrair_tabela(self.table_Lista)
                item_selecionado = extrai_recomendados[item.row()]

                id_func, criacao, nome, ativo = item_selecionado

                self.line_Num.setText(id_func)
                self.line_Descricao.setText(nome)

                if ativo == "S":
                    self.check_Ativo.setChecked(True)
                else:
                    self.check_Ativo.setChecked(False)

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_cadastro(self):
        try:
            num_id = self.line_Num.text()
            nome = self.line_Descricao.text()

            if not num_id:
                self.mensagem_alerta('O campo "Código" não pode estar vazio!   ')
                self.line_Num.setFocus()
            elif num_id == "0":
                self.mensagem_alerta('O campo "Código" não pode ser "0"!   ')
                self.line_Num.clear()
                self.line_Num.setFocus()
            elif not nome:
                self.mensagem_alerta('O campo "Descrição" não pode estar vazio!   ')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif nome == "0":
                self.mensagem_alerta('O campo "Descrição" não pode ser "0"!   ')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            else:
                cursor = conecta.cursor()
                cursor.execute(f"select id, criacao, funcionario, COALESCE(ativo, '') "
                               f"from funcionarios where id = {num_id} and id <> 0 ;")
                funcionario = cursor.fetchall()

                cursor = conecta.cursor()
                cursor.execute(f"SELECT * "
                               f"FROM movimentacao "
                               f"WHERE funcionario = {num_id};")
                movimentacao = cursor.fetchall()

                if not funcionario:
                    self.mensagem_alerta(f'O cadastro de Funcionário Nº {num_id} não existe!')
                elif movimentacao:
                    self.mensagem_alerta(f'O cadastro de Funcionário Nº {num_id} não pode ser excluído, '
                                         f'pois existem vínculos com a movimentação!')
                else:
                    msg = f'Tem certeza que deseja excluir o Funcionário {nome}?'
                    if self.pergunta_confirmacao(msg):
                        cursor = conecta.cursor()
                        cursor.execute(f"DELETE FROM funcionarios WHERE id = {num_id};")

                        conecta.commit()

                        self.mensagem_alerta(f"Cadastro do Funcionário {nome} foi excluído com Sucesso!")

                        self.reiniciando_tela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            num_id = self.line_Num.text()
            nome = self.line_Descricao.text()

            if not num_id:
                self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                self.line_Num.setFocus()
            elif num_id == "0":
                self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                self.line_Num.clear()
                self.line_Num.setFocus()
            elif not nome:
                self.mensagem_alerta('O campo "Descrição" não pode estar vazio!   ')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif nome == "0":
                self.mensagem_alerta('O campo "Descrição" não pode ser "0"!   ')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            else:
                self.salvar_dados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_dados(self):
        try:
            num_id = self.line_Num.text()

            descr = self.line_Descricao.text()
            descr_maiuscula = descr.upper()
            descr_sem_acentos = unidecode(descr_maiuscula)

            if self.check_Ativo.isChecked():
                ativo = "S"
            else:
                ativo = "NULL"

            cursor = conecta.cursor()
            cursor.execute(f"select id, criacao, funcionario, COALESCE(ativo, '') "
                           f"from funcionarios where id = {num_id};")
            cliente = cursor.fetchall()

            if cliente:
                num_id_b, criacao_b, func_b, ativ = cliente[0]

                if ativ:
                    if ativ == " ":
                        ativo_b = "NULL"
                    else:
                        ativo_b = ativ
                else:
                    ativo_b = "NULL"

                campos_atualizados = []
                if descr_sem_acentos != func_b:
                    campos_atualizados.append(f"funcionario = '{descr_sem_acentos}'")
                if ativo != ativo_b:
                    if ativo == "NULL":
                        campos_atualizados.append(f"ativo = {ativo}")
                    else:
                        campos_atualizados.append(f"ativo = '{ativo}'")

                if campos_atualizados:
                    msg = f'Deseja realmente atualizar o cadastro do Funcionario?'
                    if self.pergunta_confirmacao(msg):
                        campos_update = ", ".join(campos_atualizados)

                        cursor.execute(f"UPDATE funcionarios SET {campos_update} "
                                       f"WHERE id = {num_id_b};")

                        conecta.commit()

                        msg = f'O cadastro do Funcionario {descr_sem_acentos} foi atualizado com sucesso!'
                        self.mensagem_alerta(msg)

            else:
                msg = f'Deseja realmente cadastrar este Funcionario?'
                if self.pergunta_confirmacao(msg):
                    if ativo == "NULL":
                        cursor = conecta.cursor()
                        cursor.execute(f"Insert into funcionarios (ID, FUNCIONARIO, ATIVO) "
                                       f"values (GEN_ID(GEN_funcionarios_ID,1), '{descr_sem_acentos}', {ativo});")
                    else:
                        cursor = conecta.cursor()
                        cursor.execute(f"Insert into funcionarios (ID, FUNCIONARIO, ATIVO) "
                                       f"values (GEN_ID(GEN_funcionarios_ID,1), '{descr_sem_acentos}', '{ativo}');")

                    conecta.commit()

                    msg = f'O cadastro do Funcionario {descr_sem_acentos} foi criado com sucesso!'
                    self.mensagem_alerta(msg)

            self.reiniciando_tela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaCadastroFuncionario()
    tela.show()
    qt.exec_()
