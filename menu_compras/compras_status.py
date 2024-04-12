import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import lanca_tabela, layout_cabec_tab
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from forms.tela_compras_status import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os
from threading import Thread


class TelaComprasStatus(QMainWindow, Ui_Consulta_Sol):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_compra_sol.png")
        tamanho_aplicacao(self)
        self.layout_tabela_solicitacao(self.table_Solicitacao)
        self.layout_tabela_requisicao(self.table_Requisicao)
        self.layout_tabela_oc(self.table_OC)
        self.layout_proprio()

        self.btn_Status_Sol.clicked.connect(self.manipula_sol_por_status)
        self.btn_Num_Sol.clicked.connect(self.manipula_sol_por_numero)
        self.line_Num_Sol.editingFinished.connect(self.manipula_sol_por_numero)
        self.line_Codigo_Sol.editingFinished.connect(self.manipula_sol_por_produto)
        self.btn_Prod_Sol.clicked.connect(self.manipula_sol_por_produto)

        self.btn_Status_Req.clicked.connect(self.manipula_req_por_status)
        self.btn_Num_Req.clicked.connect(self.manipula_req_por_numero)
        self.line_Num_Req.editingFinished.connect(self.manipula_req_por_numero)
        self.line_Codigo_Req.editingFinished.connect(self.manipula_req_por_produto)
        self.btn_Prod_Req.clicked.connect(self.manipula_req_por_produto)

        self.btn_Status_OC.clicked.connect(self.manipula_oc_por_status)
        self.line_Num_Fornec.editingFinished.connect(self.manipula_oc_por_status)
        self.btn_Num_OC.clicked.connect(self.manipula_oc_por_numero)
        self.line_Num_OC.editingFinished.connect(self.manipula_oc_por_numero)
        self.line_Codigo_OC.editingFinished.connect(self.manipula_oc_por_produto)
        self.btn_Prod_OC.clicked.connect(self.manipula_oc_por_produto)

        self.progress.setHidden(True)

        self.processando = False

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor1)
            cor_widget(self.widget_Cor2)
            cor_widget(self.widget_Cor3)
            cor_widget(self.widget_Cor4)
            cor_widget(self.widget_Cor5)
            cor_widget(self.widget_Cor6)
            cor_widget(self.widget_Cor7)
            cor_widget(self.widget_Cor8)
            cor_widget(self.widget_Cor9)
            cor_widget(self.widget_Cor10)
            cor_widget(self.widget_Cor11)
            cor_widget(self.widget_Cor12)
            cor_widget(self.widget_Progress)

            cor_fonte(self.label)
            cor_fonte(self.label_16)
            cor_fonte(self.label_18)
            cor_fonte(self.label_19)
            cor_fonte(self.label_13)
            cor_fonte(self.label_11)
            cor_fonte(self.label_14)
            cor_fonte(self.label_15)
            cor_fonte(self.label_10)
            cor_fonte(self.label_25)
            cor_fonte(self.label_27)
            cor_fonte(self.label_29)
            cor_fonte(self.label_26)
            cor_fonte(self.label_28)
            cor_fonte(self.label_21)
            cor_fonte(self.label_22)
            cor_fonte(self.label_3)
            cor_fonte(self.label_30)
            cor_fonte(self.label_4)
            cor_fonte(self.label_58)
            cor_fonte(self.label_57)
            cor_fonte(self.label_53)
            cor_fonte(self.label_56)
            cor_fonte(self.label_51)
            cor_fonte(self.label_55)
            cor_fonte(self.label_52)
            cor_fonte(self.label_54)
            cor_fonte(self.label_61)
            cor_fonte(self.label_62)
            cor_fonte(self.label_63)
            cor_fonte(self.label_64)
            cor_fonte(self.label_65)
            cor_fonte(self.label_66)
            cor_fonte(self.label_69)
            cor_fonte(self.label_6)
            cor_fonte(self.label_71)
            cor_fonte(self.label_73)
            cor_fonte(self.label_74)
            cor_fonte(self.label_76)
            cor_fonte(self.label_78)
            cor_fonte(self.label_79)
            cor_fonte(self.label_9)

            cor_fonte(self.check_Baixado_Sol)
            cor_fonte(self.check_Aberto_Sol)
            cor_fonte(self.check_Aberto_Req)
            cor_fonte(self.check_Baixado_Req)
            cor_fonte(self.check_Aberto_OC)
            cor_fonte(self.check_Baixado_OC)

            cor_btn(self.btn_Status_Sol)
            cor_btn(self.btn_Prod_Sol)
            cor_btn(self.btn_Num_Sol)
            cor_btn(self.btn_Status_Req)
            cor_btn(self.btn_Prod_Req)
            cor_btn(self.btn_Num_Req)
            cor_btn(self.btn_Status_OC)
            cor_btn(self.btn_Prod_OC)
            cor_btn(self.btn_Num_OC)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_solicitacao(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 65)
            nome_tabela.setColumnWidth(1, 50)
            nome_tabela.setColumnWidth(2, 40)
            nome_tabela.setColumnWidth(3, 210)
            nome_tabela.setColumnWidth(4, 140)
            nome_tabela.setColumnWidth(5, 35)
            nome_tabela.setColumnWidth(6, 50)
            nome_tabela.setColumnWidth(7, 210)
            nome_tabela.setColumnWidth(8, 50)
            nome_tabela.setColumnWidth(9, 100)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_requisicao(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 65)
            nome_tabela.setColumnWidth(1, 50)
            nome_tabela.setColumnWidth(2, 40)
            nome_tabela.setColumnWidth(3, 210)
            nome_tabela.setColumnWidth(4, 140)
            nome_tabela.setColumnWidth(5, 35)
            nome_tabela.setColumnWidth(6, 50)
            nome_tabela.setColumnWidth(7, 210)
            nome_tabela.setColumnWidth(8, 45)
            nome_tabela.setColumnWidth(9, 50)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_oc(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 65)
            nome_tabela.setColumnWidth(1, 50)
            nome_tabela.setColumnWidth(2, 40)
            nome_tabela.setColumnWidth(3, 210)
            nome_tabela.setColumnWidth(4, 140)
            nome_tabela.setColumnWidth(5, 35)
            nome_tabela.setColumnWidth(6, 50)
            nome_tabela.setColumnWidth(7, 80)
            nome_tabela.setColumnWidth(8, 210)
            nome_tabela.setColumnWidth(9, 50)
            nome_tabela.setColumnWidth(10, 50)
            nome_tabela.setColumnWidth(11, 50)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_sol_por_status(self):
        try:
            self.progress.setHidden(False)

            abertas = self.check_Aberto_Sol.isChecked()
            fechadas = self.check_Baixado_Sol.isChecked()

            if abertas and fechadas:
                Thread(target=self.sol_total).start()
            elif abertas:
                Thread(target=self.sol_total_aberto).start()
            elif fechadas:
                Thread(target=self.sol_total_baixada).start()
            else:
                self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def sol_total_aberto(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.dataemissao)||'-'||extract(month from req.dataemissao)||'-'||"
                           f"extract(year from req.dataemissao)) AS DATA, "
                           f"COALESCE(prodreq.mestre, ''), prod.codigo, "
                           f"CASE prod.id when 28761 then prodreq.descricao else prod.descricao end as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade, COALESCE(prodreq.destino, ''), prodreq.status, "
                           f"COALESCE(req.nome_pc, '') "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"WHERE prodreq.status = 'A' AND preq.id_prod_sol IS NULL ORDER BY prodreq.mestre;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_Solicitacao, extrair_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def sol_total_baixada(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.dataemissao)||'-'||extract(month from req.dataemissao)||'-'||"
                           f"extract(year from req.dataemissao)) AS DATA, "
                           f"COALESCE(prodreq.mestre, ''), prod.codigo, "
                           f"CASE prod.id when 28761 then prodreq.descricao else prod.descricao end as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade, COALESCE(prodreq.destino, ''), prodreq.status, "
                           f"COALESCE(req.nome_pc, '') "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"WHERE prodreq.status = 'B' ORDER BY prodreq.mestre;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_Solicitacao, extrair_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def sol_total(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.dataemissao)||'-'||extract(month from req.dataemissao)||'-'||"
                           f"extract(year from req.dataemissao)) AS DATA, "
                           f"COALESCE(prodreq.mestre, ''), prod.codigo, "
                           f"CASE prod.id when 28761 then prodreq.descricao else prod.descricao end as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade, COALESCE(prodreq.destino, ''), prodreq.status, "
                           f"COALESCE(req.nome_pc, '') "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"ORDER BY prodreq.mestre;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_Solicitacao, extrair_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_sol_por_numero(self):
        try:
            self.progress.setHidden(False)

            num_sol = self.line_Num_Sol.text()

            if num_sol:
                Thread(target=self.sol_total_por_numero).start()
            else:
                self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def sol_total_por_numero(self):
        try:
            num_sol = self.line_Num_Sol.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.dataemissao)||'-'||extract(month from req.dataemissao)||'-'||"
                           f"extract(year from req.dataemissao)) AS DATA, "
                           f"COALESCE(prodreq.mestre, ''), prod.codigo, "
                           f"CASE prod.id when 28761 then prodreq.descricao else prod.descricao end as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade, COALESCE(prodreq.destino, ''), prodreq.status, "
                           f"COALESCE(req.nome_pc, '') "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"WHERE prodreq.mestre = {num_sol}"
                           f"ORDER BY prodreq.mestre;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_Solicitacao, extrair_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_sol_por_produto(self):
        if not self.processando:
            try:
                self.processando = True

                self.progress.setHidden(False)

                codigo_produto = self.line_Codigo_Sol.text()

                if codigo_produto:
                    codigo_produto = self.line_Codigo_Sol.text()
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                                   f"FROM produto where codigo = {codigo_produto};")
                    detalhes_produto = cursor.fetchall()
                    if not detalhes_produto:
                        mensagem_alerta('Este código de produto não existe!')
                        self.line_Codigo_Sol.clear()
                    else:
                        codigo_produto = self.line_Codigo_Sol.text()
                        cur = conecta.cursor()
                        cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                                    f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                                    f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
                        detalhes_produto = cur.fetchall()
                        descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

                        self.line_Descricao_Sol.setText(descr)
                        self.line_Referencia_Sol.setText(ref)
                        self.line_UM_Sol.setText(um)

                        Thread(target=self.sol_total_por_produto).start()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def sol_total_por_produto(self):
        try:
            cod_prod = self.line_Codigo_Sol.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.dataemissao)||'-'||extract(month from req.dataemissao)||'-'||"
                           f"extract(year from req.dataemissao)) AS DATA, "
                           f"COALESCE(prodreq.mestre, ''), prod.codigo, "
                           f"CASE prod.id when 28761 then prodreq.descricao else prod.descricao end as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade, COALESCE(prodreq.destino, ''), prodreq.status, "
                           f"COALESCE(req.nome_pc, '') "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"WHERE prod.codigo = {cod_prod}"
                           f"ORDER BY prodreq.mestre;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_Solicitacao, extrair_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_req_por_status(self):
        try:
            self.progress.setHidden(False)

            abertas = self.check_Aberto_Req.isChecked()
            fechadas = self.check_Baixado_Req.isChecked()

            if abertas and fechadas:
                Thread(target=self.req_total).start()
            elif abertas:
                Thread(target=self.req_total_aberto).start()
            elif fechadas:
                Thread(target=self.req_total_baixada).start()
            else:
                self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_req_por_numero(self):
        try:
            self.progress.setHidden(False)

            num_req = self.line_Num_Req.text()

            if num_req:
                Thread(target=self.req_total_por_numero).start()
            else:
                self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_req_por_produto(self):
        if not self.processando:
            try:
                self.processando = True

                self.progress.setHidden(False)

                codigo_produto = self.line_Codigo_Req.text()

                if codigo_produto:
                    codigo_produto = self.line_Codigo_Req.text()
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                                   f"FROM produto where codigo = {codigo_produto};")
                    detalhes_produto = cursor.fetchall()
                    if not detalhes_produto:
                        mensagem_alerta('Este código de produto não existe!')
                        self.line_Codigo_Req.clear()
                        self.progress.setHidden(True)
                    else:
                        codigo_produto = self.line_Codigo_Req.text()
                        cur = conecta.cursor()
                        cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                                    f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                                    f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
                        detalhes_produto = cur.fetchall()
                        descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

                        self.line_Descricao_Req.setText(descr)
                        self.line_Referencia_Req.setText(ref)
                        self.line_UM_Req.setText(um)

                        Thread(target=self.req_total_por_produto).start()
                else:
                    self.progress.setHidden(True)

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def req_total_aberto(self):
        try:
            dados_man_req = []
            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.data)||'-'||"
                           f"extract(month from req.data)||'-'||"
                           f"extract(year from req.data)) AS DATA, "
                           f"prodreq.numero, prodreq.produto, prodreq.quantidade, "
                           f"prodreq.destino, prodreq.id_prod_sol, prodreq.status "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"where prodreq.status = 'A';")
            select_req = cursor.fetchall()

            for dados_req in select_req:
                data, numero, produto, qtde, destino, id_prod_sol, status = dados_req

                cur = conecta.cursor()
                cur.execute(f"SELECT codigo, descricao, COALESCE(obs, ' ') as obs, unidade "
                            f"FROM produto where id = {produto};")
                detalhes_produtos = cur.fetchall()
                cod, descr, ref, um = detalhes_produtos[0]

                if id_prod_sol is None:
                    num_sol = "X"
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, mestre "
                                   f"FROM produtoordemsolicitacao "
                                   f"WHERE id = {id_prod_sol};")
                    extrair_sol = cursor.fetchall()
                    id_sol, num_so = extrair_sol[0]

                    if not extrair_sol:
                        num_sol = "X"
                    else:
                        num_sol = num_so

                dados = (data, numero, cod, descr, ref, um, qtde, destino, num_sol, status)
                dados_man_req.append(dados)

            if dados_man_req:
                lanca_tabela(self.table_Requisicao, dados_man_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def req_total_baixada(self):
        try:
            dados_man_req = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.data)||'-'||"
                           f"extract(month from req.data)||'-'||"
                           f"extract(year from req.data)) AS DATA, "
                           f"prodreq.numero, prodreq.produto, prodreq.quantidade, "
                           f"prodreq.destino, prodreq.id_prod_sol, prodreq.status "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"where prodreq.status = 'B' "
                           f"ORDER BY prodreq.numero;")
            select_req = cursor.fetchall()

            for dados_req in select_req:
                data, numero, produto, qtde, destino, id_prod_sol, status = dados_req

                cur = conecta.cursor()
                cur.execute(f"SELECT codigo, descricao, COALESCE(obs, ' ') as obs, unidade "
                            f"FROM produto where id = {produto};")
                detalhes_produtos = cur.fetchall()
                cod, descr, ref, um = detalhes_produtos[0]

                if id_prod_sol is None:
                    num_sol = "X"
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, mestre "
                                   f"FROM produtoordemsolicitacao "
                                   f"WHERE id = {id_prod_sol};")
                    extrair_sol = cursor.fetchall()
                    id_sol, num_so = extrair_sol[0]

                    if not extrair_sol:
                        num_sol = "X"
                    else:
                        num_sol = num_so

                dados = (data, numero, cod, descr, ref, um, qtde, destino, num_sol, status)
                dados_man_req.append(dados)

            if dados_man_req:
                lanca_tabela(self.table_Requisicao, dados_man_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def req_total(self):
        try:
            dados_man_req = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.data)||'-'||"
                           f"extract(month from req.data)||'-'||"
                           f"extract(year from req.data)) AS DATA, "
                           f"prodreq.numero, prodreq.produto, prodreq.quantidade, "
                           f"prodreq.destino, prodreq.id_prod_sol, prodreq.status "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"ORDER BY prodreq.numero;")
            select_req = cursor.fetchall()

            for dados_req in select_req:
                data, numero, produto, qtde, destino, id_prod_sol, status = dados_req

                cur = conecta.cursor()
                cur.execute(f"SELECT codigo, descricao, COALESCE(obs, ' ') as obs, unidade "
                            f"FROM produto where id = {produto};")
                detalhes_produtos = cur.fetchall()
                cod, descr, ref, um = detalhes_produtos[0]

                if id_prod_sol is None:
                    num_sol = "X"
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, mestre "
                                   f"FROM produtoordemsolicitacao "
                                   f"WHERE id = {id_prod_sol};")
                    extrair_sol = cursor.fetchall()
                    id_sol, num_so = extrair_sol[0]

                    if not extrair_sol:
                        num_sol = "X"
                    else:
                        num_sol = num_so

                dados = (data, numero, cod, descr, ref, um, qtde, destino, num_sol, status)
                dados_man_req.append(dados)

            if dados_man_req:
                lanca_tabela(self.table_Requisicao, dados_man_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def req_total_por_numero(self):
        try:
            num_req = self.line_Num_Req.text()

            dados_man_req = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.data)||'-'||"
                           f"extract(month from req.data)||'-'||"
                           f"extract(year from req.data)) AS DATA, "
                           f"prodreq.numero, prodreq.produto, prodreq.quantidade, "
                           f"prodreq.destino, prodreq.id_prod_sol, prodreq.status "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"WHERE prodreq.numero = {num_req}"
                           f"ORDER BY prodreq.numero;")
            select_req = cursor.fetchall()

            for dados_req in select_req:
                data, numero, produto, qtde, destino, id_prod_sol, status = dados_req

                cur = conecta.cursor()
                cur.execute(f"SELECT codigo, descricao, COALESCE(obs, ' ') as obs, unidade "
                            f"FROM produto where id = {produto};")
                detalhes_produtos = cur.fetchall()
                cod, descr, ref, um = detalhes_produtos[0]

                if id_prod_sol is None:
                    num_sol = "X"
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, mestre "
                                   f"FROM produtoordemsolicitacao "
                                   f"WHERE id = {id_prod_sol};")
                    extrair_sol = cursor.fetchall()
                    id_sol, num_so = extrair_sol[0]

                    if not extrair_sol:
                        num_sol = "X"
                    else:
                        num_sol = num_so

                dados = (data, numero, cod, descr, ref, um, qtde, destino, num_sol, status)
                dados_man_req.append(dados)

            if dados_man_req:
                lanca_tabela(self.table_Requisicao, dados_man_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def req_total_por_produto(self):
        try:
            cod_prod = self.line_Codigo_Req.text()

            dados_man_req = []

            cur = conecta.cursor()
            cur.execute(f"SELECT id, codigo FROM produto where codigo = {cod_prod};")
            detalhes_produtos0 = cur.fetchall()
            id_prod0, cod0 = detalhes_produtos0[0]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT (extract(day from req.data)||'-'||"
                           f"extract(month from req.data)||'-'||"
                           f"extract(year from req.data)) AS DATA, "
                           f"prodreq.numero, prodreq.produto, prodreq.quantidade, "
                           f"prodreq.destino, prodreq.id_prod_sol, prodreq.status "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"WHERE prodreq.produto = {id_prod0}"
                           f"ORDER BY prodreq.numero;")
            select_req = cursor.fetchall()

            for dados_req in select_req:
                data, numero, produto, qtde, destino, id_prod_sol, status = dados_req

                cur = conecta.cursor()
                cur.execute(f"SELECT codigo, descricao, COALESCE(obs, ' ') as obs, unidade "
                            f"FROM produto where id = {produto};")
                detalhes_produtos = cur.fetchall()
                cod, descr, ref, um = detalhes_produtos[0]

                if id_prod_sol is None:
                    num_sol = "X"
                else:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, mestre "
                                   f"FROM produtoordemsolicitacao "
                                   f"WHERE id = {id_prod_sol};")
                    extrair_sol = cursor.fetchall()
                    id_sol, num_so = extrair_sol[0]

                    if not extrair_sol:
                        num_sol = "X"
                    else:
                        num_sol = num_so

                dados = (data, numero, cod, descr, ref, um, qtde, destino, num_sol, status)
                dados_man_req.append(dados)

            if dados_man_req:
                lanca_tabela(self.table_Requisicao, dados_man_req)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_oc_por_status(self):
        try:
            self.progress.setHidden(False)

            abertas = self.check_Aberto_OC.isChecked()
            fechadas = self.check_Baixado_OC.isChecked()
            num_fonec = self.line_Num_Fornec.text()

            if num_fonec:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {num_fonec};")
                dados_fornecedor = cursor.fetchall()

                if not dados_fornecedor:
                    mensagem_alerta('Este código de Fornecedor não existe!')
                    self.line_Num_Fornec.clear()
                    self.progress.setHidden(True)
                else:
                    if abertas and fechadas:
                        Thread(target=self.oc_total_forn).start()
                    elif abertas:
                        Thread(target=self.oc_total_aberto_fornc).start()
                    elif fechadas:
                        Thread(target=self.oc_total_baixada_fornc).start()
                    else:
                        self.progress.setHidden(True)
            else:
                if abertas and fechadas:
                    Thread(target=self.oc_total).start()
                elif abertas:
                    Thread(target=self.oc_total_aberto).start()
                elif fechadas:
                    Thread(target=self.oc_total_baixada).start()
                else:
                    self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_aberto(self):
        try:
            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"INNER JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.entradasaida = 'E' AND oc.STATUS = 'A' AND prodoc.produzido < prodoc.quantidade "
                f"ORDER BY oc.numero;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")
                    entrega = entr_dt.strftime("%d/%m/%Y")

                    falta_ent = float(qtde) - float(prod)
                    if falta_ent == int(falta_ent):
                        casas_decimais = falta_ent
                    else:
                        casas_decimais = "%.3f" % falta_ent

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_baixada(self):
        try:
            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.entradasaida = 'E' AND oc.STATUS = 'B' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")
                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    dados = (emissao, oc, cod, descr, ref, um, qtde, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total(self):
        try:
            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.entradasaida = 'E' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")

                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    if status == "A":
                        falta_ent = float(qtde) - float(prod)
                        if falta_ent == int(falta_ent):
                            casas_decimais = falta_ent
                        else:
                            casas_decimais = "%.3f" % falta_ent
                    else:
                        casas_decimais = qtde

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_aberto_fornc(self):
        try:
            num_fonec = self.line_Num_Fornec.text()

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"INNER JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where forn.registro = {num_fonec} "
                f"and oc.entradasaida = 'E' "
                f"AND oc.STATUS = 'A' "
                f"AND prodoc.produzido < prodoc.quantidade "
                f"ORDER BY oc.numero;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")
                    entrega = entr_dt.strftime("%d/%m/%Y")

                    falta_ent = float(qtde) - float(prod)
                    if falta_ent == int(falta_ent):
                        casas_decimais = falta_ent
                    else:
                        casas_decimais = "%.3f" % falta_ent

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_baixada_fornc(self):
        try:
            num_fonec = self.line_Num_Fornec.text()

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where forn.registro = {num_fonec} "
                f"and oc.entradasaida = 'E' "
                f"AND oc.STATUS = 'B' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")
                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    dados = (emissao, oc, cod, descr, ref, um, qtde, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_forn(self):
        try:
            num_fonec = self.line_Num_Fornec.text()

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where forn.registro = {num_fonec} "
                f"and oc.entradasaida = 'E' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")

                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    if status == "A":
                        falta_ent = float(qtde) - float(prod)
                        if falta_ent == int(falta_ent):
                            casas_decimais = falta_ent
                        else:
                            casas_decimais = "%.3f" % falta_ent
                    else:
                        casas_decimais = qtde

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_oc_por_numero(self):
        try:
            self.progress.setHidden(False)

            num_oc = self.line_Num_OC.text()

            if num_oc:
                Thread(target=self.oc_total_por_numero).start()
            else:
                self.progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def oc_total_por_numero(self):
        try:
            num_oc = self.line_Num_OC.text()

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where oc.numero = {num_oc} "
                f"and oc.entradasaida = 'E' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")

                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    if status == "A":
                        falta_ent = float(qtde) - float(prod)
                        if falta_ent == int(falta_ent):
                            casas_decimais = falta_ent
                        else:
                            casas_decimais = "%.3f" % falta_ent
                    else:
                        casas_decimais = qtde

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_oc_por_produto(self):
        if not self.processando:
            try:
                self.processando = True

                self.progress.setHidden(False)

                codigo_produto = self.line_Codigo_OC.text()

                if codigo_produto:
                    codigo_produto = self.line_Codigo_OC.text()
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                                   f"FROM produto where codigo = {codigo_produto};")
                    detalhes_produto = cursor.fetchall()
                    if not detalhes_produto:
                        mensagem_alerta('Este código de produto não existe!')
                        self.line_Codigo_OC.clear()
                        self.progress.setHidden(True)
                    else:
                        codigo_produto = self.line_Codigo_OC.text()
                        cur = conecta.cursor()
                        cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                                    f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                                    f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
                        detalhes_produto = cur.fetchall()
                        descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

                        self.line_Descricao_OC.setText(descr)
                        self.line_Referencia_OC.setText(ref)
                        self.line_UM_OC.setText(um)

                        Thread(target=self.oc_total_por_produto).start()
                else:
                    self.progress.setHidden(True)

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def oc_total_por_produto(self):
        try:
            cod_prod = self.line_Codigo_OC.text()

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT COALESCE(prodreq.numero, ''), oc.data, oc.numero, forn.razao, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prodoc.quantidade, prodoc.produzido, prodoc.dataentrega, "
                f"COALESCE(prodreq.id_prod_sol, ''), oc.STATUS "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"where prodoc.codigo = '{cod_prod}' "
                f"and oc.entradasaida = 'E' "
                f"ORDER BY oc.data;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_req, data, oc, forncec, cod, descr, ref, um, qtde, prod, entr_dt, id_sol, status = i

                    emissao = data.strftime("%d/%m/%Y")

                    if entr_dt:
                        entrega = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entrega = ""

                    if status == "A":
                        falta_ent = float(qtde) - float(prod)
                        if falta_ent == int(falta_ent):
                            casas_decimais = falta_ent
                        else:
                            casas_decimais = "%.3f" % falta_ent
                    else:
                        casas_decimais = qtde

                    dados = (emissao, oc, cod, descr, ref, um, casas_decimais, entrega, forncec, id_req, id_sol, status)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_OC, tabela)

            self.progress.setHidden(True)
            self.layout_proprio()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    telasolicitaconsulta = TelaComprasStatus()
    telasolicitaconsulta.show()
    qt.exec_()
