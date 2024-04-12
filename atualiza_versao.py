from banco_dados.conexao import conecta


cursor = conecta.cursor()
cursor.execute(f"select * from versoes;")
versoes = cursor.fetchall()
for i in versoes:
    ids, versao, data_criacao = i
    print(i)

nome_tabela = 'versoes'
cursor = conecta.cursor()
cursor.execute(f"SELECT RF.RDB$FIELD_NAME FROM RDB$RELATION_FIELDS RF "
               f"WHERE RF.RDB$RELATION_NAME = 'VERSOES' "
               f"ORDER BY RF.RDB$FIELD_POSITION")
nomes_colunas = [row[0] for row in cursor.fetchall()]

cursor = conecta.cursor()
cursor.execute(f"Insert into VERSOES "
               f"(ID, VERSAO) "
               f"values (GEN_ID(GEN_VERSOES_ID,1), '2.0.000');")

conecta.commit()

print("VERSÃO SALVA COM SUCESSO!")
teste

