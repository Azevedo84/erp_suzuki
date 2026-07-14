import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton
)

# IMPORTA TUA TELA DO QT
from forms.tela_exp_incluir_v3 import *


class TelaTeste(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.teste_groupbox()

    def teste_groupbox(self):

        print("TESTE")

        print(self.group_Volumes.geometry())

        # PEGA O LAYOUT EXISTENTE
        layout = self.group_Volumes.layout()

        print(layout)

        # SE NÃO EXISTIR, CRIA
        if layout is None:

            layout = QVBoxLayout()

            self.group_Volumes.setLayout(layout)

        # LIMPA O QUE EXISTIR
        while layout.count():

            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

        # CRIA BOTÃO TESTE
        botao = QPushButton("BOTÃO TESTE")

        botao.setMinimumHeight(200)

        # ADICIONA NO GROUPBOX
        layout.addWidget(botao)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    tela = TelaTeste()

    tela.show()

    sys.exit(app.exec_())