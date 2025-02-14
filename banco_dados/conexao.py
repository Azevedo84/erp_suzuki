import fdb
import inspect
import os

nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

caminho_teste = r"C:\Users\Anderson\Documents\Banco de Dados Backup\ESTOQUE.GDB"

caminho_oficial = r'C:\HallSys\db\Horus\Suzuki\ESTOQUE.GDB'

try:
    conecta = fdb.connect(database=r"C:\HallSys\db\Horus\Suzuki\ESTOQUE.GDB",
                          host='PUBLICO',
                          port=3050,
                          user='sysdba',
                          password='masterkey',
                          charset='ANSI')

    conecta_robo = fdb.connect(database=r'C:\HallSys\db\Horus\Suzuki\ROBOZINHO.GDB',
                               host='PUBLICO',
                               port=3050,
                               user='sysdba',
                               password='masterkey',
                               charset='ANSI')

except Exception as e:
    print(e)
