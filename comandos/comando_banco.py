from banco_dados.conexao import conecta
from comandos.comando_notificacao import tratar_notificar_erros
import os
import inspect

nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
nome_arquivo = os.path.basename(nome_arquivo_com_caminho)


def definir_proximo_generator(nome_line, nome_tabela):
    # QUANDO A TABELA USA GENERATOR (ID) COMO SEQUENCIA NUMÉRICA PRINCIPAL
    try:
        cursor = conecta.cursor()
        cursor.execute(f"select GEN_ID(GEN_{nome_tabela}_ID,0) from rdb$database;")
        dados0 = cursor.fetchall()
        dados1 = dados0[0]
        dados2 = int(dados1[0]) + 1
        dados3 = str(dados2)
        nome_line.setText(dados3)
        nome_line.setReadOnly(True)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)


def definir_proximo_registro(nome_line, nome_coluna, nome_tabela):
    # QUANDO A TABELA USA ALGUMA COLUNA QUAN NÃO É GENERATOR COMO SEQUENCIA NUMÉRICA PRINCIPAL
    try:
        cursor = conecta.cursor()
        cursor.execute(f"select id, {nome_coluna} from {nome_tabela} "
                       f"where {nome_coluna} = (select max({nome_coluna}) from {nome_tabela});")
        select_numero = cursor.fetchall()
        idez, num = select_numero[0]
        proxima_op = int(num) + 1
        proxima_op_str = str(proxima_op)
        nome_line.setText(proxima_op_str)
        nome_line.setReadOnly(True)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        tratar_notificar_erros(e, nome_funcao, nome_arquivo)
