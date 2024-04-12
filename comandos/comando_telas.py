from arquivos.chamar_arquivos import definir_caminho_arquivo
from comandos.comando_notificacao import tratar_notificar_erros
from comandos.comando_cores import cabecalho_tela, widgets, textos, fonte_botao, fundo_botao, widgets_escuro
from comandos.comando_cores import fundo_tela, fundo_tela_menu
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon
import os
import inspect

nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
nome_arquivo = os.path.basename(nome_arquivo_com_caminho)


def icone(self, nome_imagem):
    try:
        camino = os.path.join('..', 'arquivos', 'icones', nome_imagem)
        caminho_arquivo = definir_caminho_arquivo(camino)

        self.setWindowIcon(QIcon(caminho_arquivo))

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def tamanho_aplicacao(self):
    try:
        monitor = QDesktopWidget().screenGeometry()
        monitor_width = monitor.width()
        monitor_height = monitor.height()

        if monitor_width > 1919 and monitor_height > 1079:
            interface_width = 1300
            interface_height = 750

        elif monitor_width > 1365 and monitor_height > 767:
            interface_width = 1050
            interface_height = 585
        else:
            interface_width = monitor_width - 165
            interface_height = monitor_height - 90

        x = (monitor_width - interface_width) // 2
        y = (monitor_height - interface_height) // 2

        self.setGeometry(x, y, interface_width, interface_height)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_widget_cab(nome_widget):
    try:
        nome_widget.setStyleSheet(f"background-color: {cabecalho_tela};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_widget(nome_widget):
    try:
        nome_widget.setStyleSheet(f"background-color: {widgets};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_widget_escuro(nome_widget):
    try:
        nome_widget.setStyleSheet(f"background-color: {widgets_escuro};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_fonte(nome_campo):
    try:
        nome_campo.setStyleSheet(f"color: {textos};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_btn(nome_botao):
    try:
        nome_botao.setStyleSheet(f"background-color: {fundo_botao}; color: {fonte_botao};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_fundo_tela(nome_widget):
    try:
        nome_widget.setStyleSheet(f"background-color: {fundo_tela};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def cor_fundo_tela_menu(nome_widget):
    try:
        nome_widget.setStyleSheet(f"background-color: {fundo_tela_menu};")

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)
