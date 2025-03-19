from banco_dados.conexao import conecta
from datetime import date

data_hoje = date.today()

cod_barras = "SUZ000" + "7183"

cursor = conecta.cursor()
cursor.execute(f"Insert into ordemservico "
               f"(id, produto, numero, quantidade, datainicial, obs, codbarras, status, codigo, "
               f"dataprevisao, id_estrutura) "
               f"values (GEN_ID(GEN_ORDEMSERVICO_ID,1), 35715, 7183, "
               f"'2', '{data_hoje}', '', '{cod_barras}', 'A', "
               f"'20972', '{data_hoje}', 2401);")
conecta.commit()