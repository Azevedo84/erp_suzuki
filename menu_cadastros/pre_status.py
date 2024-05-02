import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import tratar_notificar_erros
from comandos.comando_tabelas import lanca_tabela, layout_cabec_tab
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte
from comandos.comando_telas import cor_fundo_tela
from forms.tela_pre_status import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os


class TelaPreStatus(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        self.layout_tabela(self.table_Produto)
        self.layout_proprio()

        self.inicio_manipula_pendentes()

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor1)

            cor_fonte(self.label_13)
            cor_fonte(self.label_Titulo)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def inicio_manipula_pendentes(self):
        try:
            tabela = []
            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, registro, obs, descricao, descr_compl, referencia, um, ncm, "
                           f"kg_mt, fornecedor, data_criacao, codigo "
                           f"FROM PRODUTOPRELIMINAR "
                           f"order by data_criacao;")
            dados_banco = cursor.fetchall()

            if dados_banco:
                for i in dados_banco:
                    id_pre, registro, obs, descr, compl, ref, um, ncm, kg_mt, forn, emissao, codigo = i

                    datis = emissao.strftime("%d/%m/%Y")

                    dados = (datis, registro, obs, descr, compl, ref, um, ncm, kg_mt, forn)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Produto, tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPreStatus()
    tela.show()
    qt.exec_()
