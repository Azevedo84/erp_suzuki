from banco_dados.conexao import conecta

id_mov = 100941

cur = conecta.cursor()
cur.execute(f"SELECT data, produto, tipo, quantidade, localestoque from movimentacao where id = {id_mov};")
detalhes_mov = cur.fetchall()

if detalhes_mov:
    data, id_prod, tipo, qtde, local_estoque = detalhes_mov[0]

    cur = conecta.cursor()
    cur.execute(f"SELECT descricao, obs, quantidade from produto where id = {id_prod};")
    dados_produto = cur.fetchall()
    descr, ref, saldo_total = dados_produto[0]

    cur = conecta.cursor()
    cur.execute(f"SELECT nome, negativo, usarestoque from LOCALESTOQUE where id = {local_estoque};")
    dados_local_estoque = cur.fetchall()
    nome_local, negativo, usar_estoque = dados_local_estoque[0]

    cur = conecta.cursor()
    cur.execute(f"SELECT local_estoque, saldo from SALDO_ESTOQUE "
                f"where produto_id = {id_prod} "
                f"and local_estoque = {local_estoque};")
    saldos_produto = cur.fetchall()
    num_saldo_local, saldo_local = saldos_produto[0]

    print(nome_local, descr, ref, saldo_total)

    cur = conecta.cursor()
    cur.execute(f"SELECT id, movimentacao from entradaprod where movimentacao = {id_mov};")
    entrada_prod = cur.fetchall()
    if entrada_prod:
        for i in entrada_prod:
            print("entradaprod", i)

    cur = conecta.cursor()
    cur.execute(f"SELECT id, mestre from produtoos where movimentacao = {id_mov};")
    produto_os = cur.fetchall()
    if produto_os:
        for i in produto_os:
            id_produto_os, id_op = i
            print("produtoos", i)

            cur = conecta.cursor()
            cur.execute(f"SELECT id, produto, numero, status, movimentacao from ordemservico where id = {id_op};")
            dados_op = cur.fetchall()
            id_op, id_produto, num_op, status, id_mov_op = dados_op[0]

            if status == "B":
                print("ordem encerrada")

                cursor = conecta.cursor()
                cursor.execute(f"DELETE FROM movimentacao WHERE id = {id_mov_op};")
                print("removido mov")

                conecta.commit()

            cursor = conecta.cursor()
            cursor.execute(f"DELETE FROM produtoos WHERE id = {id_produto_os};")
            print("removido produto os")

            conecta.commit()

    cur = conecta.cursor()
    cur.execute(f"SELECT id, movimentacao from produtoservico where movimentacao = {id_mov};")
    produto_servico = cur.fetchall()
    if produto_servico:
        for i in produto_servico:
            print("produtoservico", i)

    cur = conecta.cursor()
    cur.execute(f"SELECT id, movimentacao from saidaprod where movimentacao = {id_mov};")
    saida_prod = cur.fetchall()
    if saida_prod:
        for i in saida_prod:
            print("saidaprod", i)

    cursor = conecta.cursor()
    cursor.execute(f"DELETE FROM movimentacao WHERE id = {id_mov};")
    print("removido mov")

    conecta.commit()
