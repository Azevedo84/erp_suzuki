import sys
from forms.tela_prod_desenho import *
from banco_dados.controle_erros import grava_erro_banco
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
import inspect
import os
import traceback

import fitz  # PyMuPDF
from PyQt5.QtGui import QPixmap, QImage


class TelaProjeto(QMainWindow, Ui_MainWindow):
    produto_escolhido = pyqtSignal(str)

    def __init__(self, projeto, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        self.setMinimumSize(900, 600)
        self.resize(900, 600)

        if ".png" in projeto:
            self.abrir_png(projeto)
        elif projeto:
            self.abrir_pdf(projeto)

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

    def abrir_png(self, caminho_png):
        try:
            self.label.clear()

            pixmap = QPixmap(caminho_png)
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)

            self.resize(900, 600)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def abrir_pdf(self, caminho_pdf):
        try:
            self.label.clear()

            doc = fitz.open(caminho_pdf)
            page = doc.load_page(0)  # primeira página
            pix = page.get_pixmap(matrix=fitz.Matrix(1.4, 1.2))  # zoom 2x para melhor resolução

            # Converter para QImage
            image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)

            # Mostrar no QLabel criado no Qt Designer (nomeado "label")
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaProjeto("")
    tela.show()
    qt.exec_()
