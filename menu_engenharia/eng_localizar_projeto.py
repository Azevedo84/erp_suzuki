import sys
from banco_dados.conexao import conecta_engenharia
from forms.tela_eng_localiza_projeto import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.telas import tamanho_aplicacao, icone
from comandos.tabelas import lanca_tabela, layout_cabec_tab, extrair_tabela
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal
import inspect
import os
import traceback


class TelaLocalizaProjeto(QMainWindow, Ui_MainWindow):
    produto_escolhido = pyqtSignal(str)
    def __init__(self, outra_tela, texto_desenho, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.outra_tela = outra_tela

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu.png")
        layout_cabec_tab(self.table_Arquivos)

        self.timer_busca = QTimer()
        self.timer_busca.setSingleShot(True)  # dispara uma vez só
        self.timer_busca.timeout.connect(self.buscar_produto)

        self.line_Filtro_Desenho.textChanged.connect(self.iniciar_timer_busca)

        self.table_Arquivos.viewport().installEventFilter(self)

        if texto_desenho:
            self.line_Filtro_Desenho.setText(texto_desenho)

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

    def iniciar_timer_busca(self):
        try:
            self.timer_busca.start(400)  # 400 ms (ajuste se quiser)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def atualizar_produto_entry(self, produto):
        try:
            self.line_Filtro_Desenho.setText(produto)

            self.buscar_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def buscar_produto(self):
        try:
            texto = self.line_Filtro_Desenho.text().strip()

            if texto:
                self.lanca_dados_num_desenho(texto)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_num_desenho(self, desenho):
        try:
            self.table_Arquivos.setRowCount(0)

            cursor = conecta_engenharia.cursor()
            cursor.execute("""
                SELECT ID, ARQUIVO, CAMINHO
                FROM ARQUIVOS
                WHERE NOME_BASE LIKE ? 
                  AND TIPO_ARQUIVO IN ('IPT', 'IAM')
                  ORDER BY ARQUIVO ASC
            """, (f"%{desenho}%",))
            dados_arquivo = cursor.fetchall()

            if dados_arquivo:
                lanca_tabela(self.table_Arquivos, dados_arquivo)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def consulta_propriedade_ipt_iam(self, id_arquivo, propr):
        try:
            propriedade_escolhida = ""

            cursor_eng = conecta_engenharia.cursor()
            sql = f"""
                SELECT ipt.id_arquivo, ipt.{propr}
                FROM PROPRIEDADES_IPT ipt
                WHERE ipt.id_arquivo = ?
            """
            cursor_eng.execute(sql, (id_arquivo,))
            dados_ipt = cursor_eng.fetchall()
            if dados_ipt:
                for i in dados_ipt:
                    propriedade_escolhida = i[1].strip()

            sql = f"""
                SELECT iam.id_arquivo, iam.{propr}
                FROM PROPRIEDADES_IAM iam
                WHERE iam.id_arquivo = ?
            """
            cursor_eng.execute(sql, (id_arquivo,))
            dados_iam = cursor_eng.fetchall()

            if dados_iam:
                for ii in dados_iam:
                    propriedade_escolhida = ii[1].strip()

            return propriedade_escolhida

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, sources, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    sources is self.table_Arquivos.viewport()):

                if self.outra_tela:
                    item = self.table_Arquivos.currentItem()
                    extrai_total = extrair_tabela(self.table_Arquivos)
                    item_selecionado = extrai_total[item.row()]

                    id_arq = item_selecionado[0]

                    self.produto_escolhido.emit(id_arq)
                    self.close()

            return super(QMainWindow, self).eventFilter(sources, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaLocalizaProjeto(False, "")
    tela.show()
    qt.exec_()
