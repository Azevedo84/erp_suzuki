import sys
from banco_dados.conexao import conecta
from forms.tela_pcp_previsao_prod import *
from comandos.comando_notificacao import grava_erro_banco
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab, limpa_tabela
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget_cab, cor_btn, cor_widget, cor_fonte
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_conversoes import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import timedelta
import inspect
import os
from threading import Thread
import traceback


class TelaPcpPrevisaoProduto(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_producao.png")
        tamanho_aplicacao(self)
        self.layout_tabela_pi(self.table_PI)
        self.layout_tabela_previsao(self.table_Previsao)
        self.layout_proprio()

        self.line_SemanCompra = "1"

        self.line_Codigo_Manu.editingFinished.connect(self.verifica_line_codigo_manual)
        self.processando = False

        self.btn_Atualizar.clicked.connect(self.calculo_1_chamar_funcao)

        self.manipula_dados_pi()

        self.progressBar.setHidden(True)
        self.label_Excel.setText("")

    def trata_excecao(self, nome_funcao, mensagem, arquivo):
        try:
            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}"\n{mensagem}')
            self.mensagem_alerta(f'Houve um problema no arquivo:\n\n{arquivo}\n\n'
                                 f'Comunique o desenvolvedor sobre o problema descrito abaixo:\n\n'
                                 f'{nome_funcao}: {mensagem}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def mensagem_alerta(self, mensagem):
        try:
            print("1")
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            print("2")
            alert.setText(mensagem)
            print("3")
            alert.setWindowTitle("Atenção")
            print("4")
            alert.setStandardButtons(QMessageBox.Ok)
            print("5")
            alert.exec_()
            print("6")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor2)
            cor_widget(self.widget_Cor3)
            cor_widget(self.widget_Cor4)
            cor_widget(self.widget_Cor5)

            cor_fonte(self.label_13)
            cor_fonte(self.label_7)
            cor_fonte(self.label_8)
            cor_fonte(self.label_Excel)
            cor_fonte(self.label_13)
            cor_fonte(self.label_procura1)
            cor_fonte(self.label_25)
            cor_fonte(self.label_38)
            cor_fonte(self.label_49)
            cor_fonte(self.label_54)
            cor_fonte(self.label_52)
            cor_fonte(self.label_55)
            cor_fonte(self.label_61)
            cor_fonte(self.label_8)
            cor_fonte(self.label_9)

            cor_btn(self.btn_Atualizar)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def layout_tabela_pi(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 40)
            nome_tabela.setColumnWidth(1, 60)
            nome_tabela.setColumnWidth(2, 230)
            nome_tabela.setColumnWidth(3, 150)
            nome_tabela.setColumnWidth(4, 40)
            nome_tabela.setColumnWidth(5, 45)
            nome_tabela.setColumnWidth(6, 85)
            nome_tabela.setColumnWidth(7, 85)
            nome_tabela.setColumnWidth(8, 80)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def layout_tabela_previsao(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 40)
            nome_tabela.setColumnWidth(1, 55)
            nome_tabela.setColumnWidth(2, 200)
            nome_tabela.setColumnWidth(3, 110)
            nome_tabela.setColumnWidth(4, 30)
            nome_tabela.setColumnWidth(5, 40)
            nome_tabela.setColumnWidth(6, 80)
            nome_tabela.setColumnWidth(7, 120)
            nome_tabela.setColumnWidth(8, 55)
            nome_tabela.setColumnWidth(9, 220)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_line_codigo_manual(self):
        if not self.processando:
            try:
                self.processando = True

                codigo_produto = self.line_Codigo_Manu.text()

                if not codigo_produto:
                    self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                    self.line_Codigo_Manu.clear()
                elif int(codigo_produto) == 0:
                    self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                    self.line_Codigo_Manu.clear()
                else:
                    self.verifica_sql_produto_manual()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
                grava_erro_banco(nome_funcao, e, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_sql_produto_manual(self):
        try:
            codigo_produto = self.line_Codigo_Manu.text()
            cursor = conecta.cursor()
            cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                           f"FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cursor.fetchall()
            if not detalhes_produto:
                self.mensagem_alerta('Este código de produto não existe!')
                self.line_Codigo_Manu.clear()
            else:
                self.lanca_dados_produto_manual()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_dados_produto_manual(self):
        try:
            codigo_produto = self.line_Codigo_Manu.text()
            cur = conecta.cursor()
            cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                        f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                        f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()
            descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

            self.line_Descricao_Manu.setText(descr)
            self.line_DescrCompl_Manu.setText(compl)
            self.line_Referencia_Manu.setText(ref)
            self.line_UM_Manu.setText(um)
            self.line_Saldo_Manu.setText(str(saldo))

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpa_dados_manual(self):
        try:
            self.line_Codigo_Manu.clear()
            self.line_Descricao_Manu.clear()
            self.line_DescrCompl_Manu.clear()
            self.line_Referencia_Manu.clear()
            self.line_UM_Manu.clear()
            self.line_Saldo_Manu.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def retorna_oc_abertas(self, cod_prod):
        try:
            qtdes_oc = 0

            if cod_prod:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT COALESCE(prodreq.mestre, ''), req.dataemissao, prodreq.quantidade "
                               f"FROM produtoordemsolicitacao as prodreq "
                               f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                               f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                               f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                               f"WHERE prodreq.status = 'A' "
                               f"and prod.codigo = {cod_prod} "
                               f"AND preq.id_prod_sol IS NULL "
                               f"ORDER BY prodreq.mestre;")
                dados_sol = cursor.fetchall()

                if dados_sol:
                    for i_sol in dados_sol:
                        num_sol, emissao_sol, qtde_sol = i_sol
                        qtdes_oc += float(qtde_sol)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT sol.idsolicitacao, prodreq.quantidade, req.data, prodreq.numero, "
                               f"prodreq.destino, prodreq.id_prod_sol "
                               f"FROM produtoordemrequisicao as prodreq "
                               f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                               f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                               f"INNER JOIN produtoordemsolicitacao as prodsol ON prodreq.id_prod_sol = prodsol.id "
                               f"INNER JOIN ordemsolicitacao as sol ON prodsol.mestre = sol.idsolicitacao "
                               f"where prodreq.status = 'A' "
                               f"and prod.codigo = {cod_prod};")
                dados_req = cursor.fetchall()

                if dados_req:
                    for i_req in dados_req:
                        num_sol_req, qtde_req, emissao_req, num_req, destino, id_prod_sol = i_req
                        qtdes_oc += float(qtde_req)

                cursor = conecta.cursor()
                cursor.execute(
                    f"SELECT sol.idsolicitacao, prodreq.numero, oc.data, oc.numero, forn.razao, "
                    f"prodoc.quantidade, prodoc.produzido, prodoc.dataentrega "
                    f"FROM ordemcompra as oc "
                    f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                    f"INNER JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                    f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                    f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                    f"INNER JOIN produtoordemsolicitacao as prodsol ON prodreq.id_prod_sol = prodsol.id "
                    f"INNER JOIN ordemsolicitacao as sol ON prodsol.mestre = sol.idsolicitacao "
                    f"where oc.entradasaida = 'E' "
                    f"AND oc.STATUS = 'A' "
                    f"AND prodoc.produzido < prodoc.quantidade "
                    f"and prod.codigo = {cod_prod}"
                    f"ORDER BY oc.numero;")
                dados_oc = cursor.fetchall()

                if dados_oc:
                    for i_oc in dados_oc:
                        num_sol_oc, id_req_oc, emissao_oc, num_oc, forncec_oc, qtde_oc, prod_oc, entrega_oc = i_oc
                        qtdes_oc += float(qtde_oc)

            return qtdes_oc

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def retorna_ops_saldo_ops_abertas(self, cod_pai, cod_filho):
        try:
            qtde_ops = 0

            if cod_pai:
                cursor = conecta.cursor()
                cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, prod.id, "
                               f"prod.descricao, "
                               f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                               f"ordser.quantidade "
                               f"from ordemservico as ordser "
                               f"INNER JOIN produto prod ON ordser.produto = prod.id "
                               f"where ordser.status = 'A' AND prod.codigo = {cod_pai} "
                               f"order by ordser.numero;")
                op_abertas = cursor.fetchall()

                if op_abertas:
                    for i in op_abertas:
                        num_op = i[2]
                        id_produto = i[3]

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT mat.id, prod.codigo, prod.descricao, "
                                       f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                                       f"((SELECT quantidade FROM ordemservico where numero = {num_op}) * "
                                       f"(mat.quantidade)) AS Qtde, "
                                       f"COALESCE(prod.localizacao, ''), prod.quantidade "
                                       f"FROM materiaprima as mat "
                                       f"INNER JOIN produto as prod ON mat.produto = prod.id "
                                       f"where mat.mestre = {id_produto} and prod.codigo = {cod_filho} "
                                       f"ORDER BY prod.descricao;")
                        select_estrut = cursor.fetchall()
                        if select_estrut:
                            for dados_estrut in select_estrut:
                                id_mat_e, cod_e, descr_e, ref_e, um_e, qtde_e, local_e, saldo_e = dados_estrut

                                cursor = conecta.cursor()
                                cursor.execute(f"SELECT max(mat.id), max(prod.codigo), max(prod.descricao), "
                                               f"sum(prodser.qtde_materia)as total "
                                               f"FROM materiaprima as mat "
                                               f"INNER JOIN produto as prod ON mat.produto = prod.id "
                                               f"INNER JOIN produtoos as prodser ON mat.id = prodser.id_materia "
                                               f"where mat.mestre = {id_produto} "
                                               f"and prodser.numero = {num_op} and mat.id = {id_mat_e} "
                                               f"group by prodser.id_materia;")
                                select_os_resumo = cursor.fetchall()

                                if select_os_resumo:
                                    for dados_res in select_os_resumo:
                                        id_mat_sum, cod_sum, descr_sum, qtde_sum = dados_res

                                        qtde_sum_float = valores_para_float(qtde_sum)

                                        qtde_ops += qtde_sum_float

            return qtde_ops

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def manipula_ordens_compra(self, dados_total):
        try:
            lista_ocs, cod_pai, qtdei_float = dados_total

            qtde_ocs = self.retorna_oc_abertas(cod_pai)

            prod_ocs_encontrado = False
            for cod_oc_p, saldo_p in lista_ocs:
                if cod_oc_p == cod_pai:
                    prod_ocs_encontrado = True
                    break

            if not prod_ocs_encontrado:
                if qtde_ocs > 0:
                    lanca_saldo = (cod_pai, qtde_ocs)
                    lista_ocs.append(lanca_saldo)

                    qtde_float_com_oc = qtdei_float - qtde_ocs
                else:
                    qtde_float_com_oc = qtdei_float
            else:
                qtde_float_com_oc = qtdei_float

            return lista_ocs, qtde_float_com_oc

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def manipula_ordens_producao(self, dados_total):
        try:
            lista_ops, cod_origem, cod_pai, qtdei_float = dados_total

            qtde_ops = self.retorna_ops_saldo_ops_abertas(cod_origem, cod_pai)

            prod_ops_encontrado = False
            for cod_op_p, saldo_p in lista_ops:
                if cod_op_p == cod_pai:
                    prod_ops_encontrado = True
                    break

            if not prod_ops_encontrado:
                if qtde_ops > 0:
                    lanca_saldo = (cod_pai, qtde_ops)
                    lista_ops.append(lanca_saldo)

                    qtde_float_com_op = qtdei_float - qtde_ops
                else:
                    qtde_float_com_op = qtdei_float
            else:
                if qtde_ops > 0:
                    qtde_float_com_op = qtdei_float - qtde_ops
                else:
                    qtde_float_com_op = qtdei_float

            return lista_ops, qtde_float_com_op

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def definir_folgas(self, data_inicio, data_fim):
        try:
            contagem_sabados = 0
            contagem_domingos = 0

            data_atual = data_inicio
            while data_atual <= data_fim:
                if data_atual.weekday() == 5:
                    contagem_sabados += 1
                elif data_atual.weekday() == 6:
                    contagem_domingos += 1

                data_atual += timedelta(days=1)

            return contagem_sabados, contagem_domingos

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def retorna_data_entrega(self, id_pais):
        try:
            tempos_de_entrega = []
            fornecedor = ''
            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.data, oc.numero, prodoc.produto, prodoc.quantidade, mov.data, forn.razao "
                           f"FROM produtoordemcompra as prodoc "
                           f"INNER JOIN entradaprod as ent ON prodoc.mestre = ent.ordemcompra "
                           f"INNER JOIN movimentacao as mov ON ent.movimentacao = mov.id "
                           f"INNER JOIN fornecedores as forn ON ent.fornecedor = forn.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"WHERE prodoc.produto = '{id_pais}' and oc.entradasaida = 'E';")
            extrair_prod = cursor.fetchall()

            if extrair_prod:
                for registro in extrair_prod:
                    data_emissao = registro[0]
                    data_entrega = registro[4]
                    fornecedor = registro[5]

                    tempo_entrega_dias = (data_entrega - data_emissao).days
                    tempos_de_entrega.append(tempo_entrega_dias)
            if tempos_de_entrega:
                media_entrega = sum(tempos_de_entrega) / len(tempos_de_entrega)
            else:
                media_entrega = 0

            entrega = int(media_entrega)

            return entrega, fornecedor

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def manipula_dados_tabela_producao(self, cod_prod):
        try:
            dados_ops = []
            cursor = conecta.cursor()
            cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, prod.codigo, "
                           f"prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"ordser.quantidade "
                           f"from ordemservico as ordser "
                           f"INNER JOIN produto prod ON ordser.produto = prod.id "
                           f"where ordser.status = 'A' and prod.codigo = {cod_prod} "
                           f"order by ordser.numero;")
            op_abertas = cursor.fetchall()
            if op_abertas:
                for dados_op in op_abertas:
                    emissao, previsao, op, cod, descr, ref, um, qtde = dados_op

                    dados = (op, qtde)
                    dados_ops.append(dados)

            return dados_ops

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def manipula_dados_pi(self):
        try:
            tabela_final = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prodint.id_pedidointerno, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, "
                           f"prod.unidade, prodint.qtde, prodint.data_previsao "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where prodint.status = 'A';")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    num_pi, cod, descr, ref, um, qtde, entrega = i

                    dados = (num_pi, cod, descr, ref, um, qtde)

                    tabela_final.append(dados)

            if tabela_final:
                lanca_tabela(self.table_PI, tabela_final)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def calculo_1_chamar_funcao(self):
        try:
            dados = extrair_tabela(self.table_PI)
            cod_manu = self.line_Codigo_Manu.text()

            if not dados:
                self.mensagem_alerta(f'A tabela "Pedidos Internos Pendentes" está vazia!')
            else:
                if cod_manu:
                    self.limpar_tudo()
                    self.progressBar.setHidden(False)

                    Thread(target=self.calculo_2_dados_previsao).start()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def calculo_2_dados_previsao(self):
        try:
            tudo_tudo = []

            cod_manu = self.line_Codigo_Manu.text()

            dados_tabela = extrair_tabela(self.table_PI)

            if dados_tabela:
                saldos = []
                ops = []
                ocs = []

                for i in dados_tabela:
                    num_pi, codigo, descr, ref, um, qtde = i

                    cod_origem = ""
                    descr_origem = ""
                    pacote = ""

                    pcte_p_estrutura = [1, 1, codigo, qtde, cod_origem, descr_origem, saldos, ops, ocs,
                                        codigo, num_pi, pacote]

                    estrutura = self.calculo_3_verifica_estrutura(pcte_p_estrutura)

                    if estrutura:
                        for ii in estrutura:
                            pts_k, niv_k, cod_k, descr_k, ref_k, um_k, qtde_k, cod_or_k, descr_or_k, cod_fat_k, \
                            num_pi_k, pacote_k = ii
                            if cod_k == cod_manu:
                                didi = (pts_k, cod_k, descr_k, ref_k, um_k, qtde_k, cod_fat_k, pacote_k)
                                tudo_tudo.append(didi)

            if tudo_tudo:
                lanca_tabela(self.table_Previsao, tudo_tudo)
            else:
                print(f'Este Plano de produção está concluído!')

                self.limpar_tudo()
                self.label_procura.setHidden(True)
                self.label_procura1.setHidden(True)
                self.label_procura2.setHidden(True)

            self.progressBar.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def calculo_3_verifica_estrutura(self, dados_total):
        try:
            pontos, nivel, codigos, qtdei, cod_or, descr_or, lista_saldos, lista_ops, lista_ocs, cod_fat, \
            num_pi, pacote = dados_total

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.id, prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, "
                           f"prod.unidade, prod.quantidade, tip.tipomaterial "
                           f"FROM produto as prod "
                           f"LEFT JOIN tipomaterial as tip ON prod.tipomaterial = tip.id "
                           f"where prod.codigo = {codigos};")
            detalhes_pai = cursor.fetchall()
            id_pai, cod_pai, descr_pai, ref_pai, um_pai, saldo, tipo = detalhes_pai[0]

            if cod_pai == "19702":
                print(cod_pai)
                print("detalhes_pai[0]", detalhes_pai[0])

            msg1 = "Verificando Estrutura:"
            msg2 = f"Código: {cod_pai}"
            msg3 = f"{descr_pai}"

            self.label_procura.setText(msg1)
            self.label_procura1.setText(msg2)
            self.label_procura2.setText(msg3)

            dadoss = (pontos, nivel, cod_pai, descr_pai, ref_pai, um_pai, qtdei, cod_or, descr_or,
                      cod_fat, num_pi, pacote)
            nov_msg = f"{cod_pai}({qtdei}), "
            pacote += nov_msg

            filhos = [dadoss]

            nivel_plus = nivel + 1
            pts_plus = pontos + 1

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"(mat.quantidade * {qtdei}) as qtde "
                           f"FROM materiaprima as mat "
                           f"INNER JOIN produto prod ON mat.produto = prod.id "
                           f"where mestre = {id_pai};")
            dados_estrutura = cursor.fetchall()

            if dados_estrutura:
                for prod in dados_estrutura:
                    cod_f, descr_f, ref_f, um_f, qtde_f = prod

                    pcte_filho = [pts_plus, nivel_plus, cod_f, qtde_f, cod_pai, descr_pai, lista_saldos,
                                  lista_ops, lista_ocs, cod_fat, num_pi, pacote]
                    filhos.extend(self.calculo_3_verifica_estrutura(pcte_filho))

            return filhos

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpar_tudo(self):
        try:
            self.progressBar.setHidden(True)
            self.widget_Barra.setHidden(False)
            limpa_tabela(self.table_Previsao)
            self.label_Excel.setText("")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPcpPrevisaoProduto()
    tela.show()
    qt.exec_()
