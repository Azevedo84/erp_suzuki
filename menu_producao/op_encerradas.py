import sys
from banco_dados.conexao import conecta
from forms.tela_op_encerradas import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela
from comandos.telas import tamanho_aplicacao, icone
from comandos.lines import validador_so_numeros
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback


class TelaOpEncerradas(QMainWindow, Ui_MainWindow):
    def __init__(self, produto, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_producao.png")
        tamanho_aplicacao(self)

        validador_so_numeros(self.line_Codigo)

        self.line_Codigo.editingFinished.connect(self.verifica_codigo)

        self.processando = False

        if produto:
            self.line_Codigo.setText(produto)

            self.verifica_codigo()

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

    def verifica_codigo(self):
        try:
            self.table_OP.setRowCount(0)

            cod_prod = self.line_Codigo.text()

            cur = conecta.cursor()
            cur.execute(f"SELECT prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                        f"COALESCE(prod.obs, ''), prod.unidade, COALESCE(prod.localizacao, ''), conj.conjunto, "
                        f"prod.quantidade "
                        f"FROM produto as prod "
                        f"LEFT JOIN conjuntos conj ON prod.conjunto = conj.id "
                        f"where prod.codigo = {cod_prod};")
            detalhes_produto = cur.fetchall()
            if detalhes_produto:
                descr, compl, ref, um, local, conjunto, saldo = detalhes_produto[0]

                self.line_Descricao.setText(descr)
                self.line_Referencia.setText(ref)
                self.line_UM.setText(um)

                self.lanca_ops_encerradas()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_ops_encerradas(self):
        try:
            cod = self.line_Codigo.text()

            cursor = conecta.cursor()
            cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, "
                           f"prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"ordser.quantidade, ordser.status, ordser.ID_ESTRUTURA "
                           f"from ordemservico as ordser "
                           f"INNER JOIN produto prod ON ordser.produto = prod.id "
                           f"where prod.codigo = {cod} and ordser.status = 'B' order by ordser.numero;")
            op_abertas = cursor.fetchall()

            self.conversao_manipula_dados(op_abertas)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def conversao_manipula_dados(self, op_abertas):
        try:
            if op_abertas:
                op_ab_editado = []
                for dados_op in op_abertas:
                    emissao, previsao, op, cod, descr, ref, um, qtde, status, id_estrut = dados_op

                    if id_estrut:
                        data_em_texto = '{}/{}/{}'.format(emissao.day, emissao.month, emissao.year)

                        if previsao:
                            data_prev = '{}/{}/{}'.format(previsao.day, previsao.month, previsao.year)
                        else:
                            data_prev = ''

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT id, codigo FROM produto where codigo = {cod};")
                        select_prod = cursor.fetchall()

                        idez, cod = select_prod[0]

                        total_estrut = 0
                        total_consumo = 0

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT estprod.id, "
                                       f"((SELECT quantidade FROM ordemservico where numero = {op}) * "
                                       f"(estprod.quantidade)) AS Qtde "
                                       f"FROM estrutura_produto as estprod "
                                       f"INNER JOIN produto prod ON estprod.id_prod_filho = prod.id "
                                       f"where estprod.id_estrutura = {id_estrut};")
                        itens_estrutura = cursor.fetchall()

                        for dads in itens_estrutura:
                            ides, quantidade = dads
                            total_estrut += 1

                            cursor = conecta.cursor()
                            cursor.execute(f"SELECT max(prodser.ID_ESTRUT_PROD), "
                                           f"sum(prodser.QTDE_ESTRUT_PROD) as total "
                                           f"FROM estrutura_produto as estprod "
                                           f"INNER JOIN produto prod ON estprod.id_prod_filho = prod.id "
                                           f"INNER JOIN produtoos as prodser ON estprod.id = prodser.ID_ESTRUT_PROD "
                                           f"where prodser.numero = {op} and estprod.id = {ides} "
                                           f"group by prodser.ID_ESTRUT_PROD;")
                            itens_consumo = cursor.fetchall()
                            for duds in itens_consumo:
                                id_mats, qtde_mats = duds
                                if ides == id_mats and quantidade == qtde_mats:
                                    total_consumo += 1

                        msg = f"{total_estrut}/{total_consumo}"

                        dados = (data_em_texto, data_prev, op, cod, descr, ref, um, qtde, msg)
                        op_ab_editado.append(dados)

                if op_ab_editado:
                    lanca_tabela(self.table_OP, op_ab_editado)

            else:
                self.mensagem_alerta("Não foi encontrado nenhum resultado para esta pesquisa")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaOpEncerradas("")
    tela.show()
    qt.exec_()
