from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from comandos.comando_notificacao import tratar_notificar_erros
from datetime import date
import os
import inspect

nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
nome_arquivo = os.path.basename(nome_arquivo_com_caminho)


def validador_decimal(nome_line, numero, decimal=3):
    try:
        validator = QDoubleValidator(0, numero, decimal, nome_line)
        locale = QLocale("pt_BR")
        validator.setLocale(locale)
        validator.setBottom(0.001)

        nome_line.setValidator(validator)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def validador_inteiro(nome_line, numero):
    try:
        validator = QIntValidator(0, numero, nome_line)
        locale = QLocale("pt_BR")
        validator.setLocale(locale)
        nome_line.setValidator(validator)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def definir_data_atual(nome_line):
    try:
        data_hoje = date.today()
        nome_line.setDate(data_hoje)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)
