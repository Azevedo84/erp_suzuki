from banco_dados.conexao import conecta

id_mov = 100665

cur = conecta.cursor()
cur.execute(f"SELECT data, produto, tipo, localestoque from movimentacao where id = {id_mov};")
detalhes_mov = cur.fetchall()

if detalhes_mov:
    data = detalhes_mov[0][0]
    id_prod = detalhes_mov[0][1]
    tipo = detalhes_mov[0][2]
    local_estoque = detalhes_mov[0][3]

    cur = conecta.cursor()
    cur.execute(f"SELECT * from produto where id = {id_prod};")
    dados_produto = cur.fetchall()
    print(dados_produto)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from LOCALESTOQUE where id = {local_estoque};")
    dados_local_estoque = cur.fetchall()
    print(dados_local_estoque)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from SALDO_ESTOQUE where produto_id = {id_prod} and local_estoque = {local_estoque};")
    saldos_produto = cur.fetchall()
    print(saldos_produto)

    if tipo == 210:
        print("EXCLUIR CONSUMO OP", data)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from entradaprod where movimentacao = {id_mov};")
    entrada_prod = cur.fetchall()
    print(entrada_prod)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from produtoos where movimentacao = {id_mov};")
    produto_os = cur.fetchall()
    print(produto_os)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from produtoservico where movimentacao = {id_mov};")
    produto_servico = cur.fetchall()
    print(produto_servico)

    cur = conecta.cursor()
    cur.execute(f"SELECT * from saidaprod where movimentacao = {id_mov};")
    saida_prod = cur.fetchall()
    print(saida_prod)
