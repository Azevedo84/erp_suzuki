from comandos.comando_notificacao import tratar_notificar_erros
from unidecode import unidecode
import os
import inspect

nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
nome_arquivo = os.path.basename(nome_arquivo_com_caminho)


def remover_acentos(string):
    try:
        return unidecode(string)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)
