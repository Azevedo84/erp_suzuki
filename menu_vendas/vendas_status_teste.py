import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import lanca_tabela, limpa_tabela, layout_cabec_tab
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget_cab
from comandos.comando_telas import cor_fundo_tela
from forms.tela_vendas_status import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os
from threading import Thread


class TelaVendasStatus(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)
        self.layout_tabela_ov(self.table_OV)
        self.layout_tabela_exp(self.table_Exp)
        self.layout_proprio()

        self.btn_Consultar_PI.clicked.connect(self.verifica_filtro_pi)

        self.btn_Consultar_OV.clicked.connect(self.verifica_filtro_ov)

        self.btn_Status_Exp.clicked.connect(self.manipula_exp_por_status)
        self.btn_Num_Exp.clicked.connect(self.manipula_exp_por_numero)
        self.line_Num_Exp.editingFinished.connect(self.manipula_exp_por_numero)
        self.line_Codigo_Exp.editingFinished.connect(self.manipula_exp_por_produto)
        self.btn_Prod_Exp.clicked.connect(self.manipula_exp_por_produto)

        self.btn_Excel_Exp.setHidden(True)
        self.widget_Progress.setHidden(True)

        self.processando = False

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_ov(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_exp(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_filtro_pi(self):
        try:
            cliente = self.combo_Cliente_PI.currentText()
            if cliente == "TODOS":
                id_cliente = ""
            else:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]

            if self.check_Aberto_PI.isChecked():
                aberto = True
            else:
                aberto = False

            if self.check_Baixado_PI.isChecked():
                baixado = True
            else:
                baixado = False

            if id_cliente:
                if aberto and baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_todos_com_cliente(id_cliente)
                elif aberto and not baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_aberto_com_cliente(id_cliente)
                elif not aberto and baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_baixado_com_cliente(id_cliente)
            else:
                if aberto and baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_aberto()
                    mensagem_alerta("Defina um cliente para filtrar os pedidos!")
                    self.combo_Cliente_PI.setFocus()
                    self.check_Aberto_PI.setChecked(True)
                    self.check_Baixado_PI.setChecked(False)
                elif aberto and not baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_aberto()
                elif not aberto and baixado:
                    self.table_PI.setRowCount(0)
                    self.dados_pi_aberto()
                    mensagem_alerta("Defina um cliente para filtrar os pedidos!")
                    self.combo_Cliente_PI.setFocus()
                    self.check_Aberto_PI.setChecked(True)
                    self.check_Baixado_PI.setChecked(False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_pi_aberto(self):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ped.emissao, ped.id, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodint.qtde, "
                           f"prodint.data_previsao, ped.solicitante, COALESCE(ped.num_req_cliente, '') as req, "
                           f"ped.nome_pc, prodint.status, COALESCE(ped.obs, '') as obs "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where prodint.status = 'A';")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_pi, clie, cod, descr, ref, um, qtde, entrega, solic, num_req, pc, status, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'
                    entreg = f'{entrega.day}/{entrega.month}/{entrega.year}'

                    dados = (emi, num_pi, clie, cod, descr, ref, um, qtde, entreg, solic, num_req, pc, status, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_PI, tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_pi_baixado_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ped.emissao, ped.id, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodint.qtde, "
                           f"prodint.data_previsao, ped.solicitante, COALESCE(ped.num_req_cliente, '') as req, "
                           f"ped.nome_pc, prodint.status, COALESCE(ped.obs, '') as obs "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where prodint.status = 'B' and ped.id_cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_pi, clie, cod, descr, ref, um, qtde, entrega, solic, num_req, pc, status, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'
                    entreg = f'{entrega.day}/{entrega.month}/{entrega.year}'

                    dados = (emi, num_pi, clie, cod, descr, ref, um, qtde, entreg, solic, num_req, pc, status, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_PI, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_pi_aberto_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ped.emissao, ped.id, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodint.qtde, "
                           f"prodint.data_previsao, ped.solicitante, COALESCE(ped.num_req_cliente, '') as req, "
                           f"ped.nome_pc, prodint.status, COALESCE(ped.obs, '') as obs "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where prodint.status = 'A' and ped.id_cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_pi, clie, cod, descr, ref, um, qtde, entrega, solic, num_req, pc, status, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'
                    entreg = f'{entrega.day}/{entrega.month}/{entrega.year}'

                    dados = (emi, num_pi, clie, cod, descr, ref, um, qtde, entreg, solic, num_req, pc, status, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_PI, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_pi_todos_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ped.emissao, ped.id, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodint.qtde, "
                           f"prodint.data_previsao, ped.solicitante, COALESCE(ped.num_req_cliente, '') as req, "
                           f"ped.nome_pc, prodint.status, COALESCE(ped.obs, '') as obs "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where ped.id_cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_pi, clie, cod, descr, ref, um, qtde, entrega, solic, num_req, pc, status, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'
                    entreg = f'{entrega.day}/{entrega.month}/{entrega.year}'

                    dados = (emi, num_pi, clie, cod, descr, ref, um, qtde, entreg, solic, num_req, pc, status, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_PI, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_filtro_ov(self):
        try:
            cliente = self.combo_Cliente_OV.currentText()
            if cliente == "TODOS":
                id_cliente = ""
            else:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]

            if self.check_Aberto_OV.isChecked():
                aberto = True
            else:
                aberto = False

            if self.check_Baixado_OV.isChecked():
                baixado = True
            else:
                baixado = False

            if id_cliente:
                if aberto and baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_todos_com_cliente(id_cliente)
                elif aberto and not baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_aberto_com_cliente(id_cliente)
                elif not aberto and baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_baixado_com_cliente(id_cliente)
            else:
                if aberto and baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_aberto()
                    mensagem_alerta("Defina um cliente para filtrar os pedidos!")
                    self.combo_Cliente_OV.setFocus()
                    self.check_Aberto_OV.setChecked(True)
                    self.check_Baixado_OV.setChecked(False)
                elif aberto and not baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_aberto()
                elif not aberto and baixado:
                    self.table_OV.setRowCount(0)
                    self.dados_ov_aberto()
                    mensagem_alerta("Defina um cliente para filtrar os pedidos!")
                    self.combo_Cliente_OV.setFocus()
                    self.check_Aberto_OV.setChecked(True)
                    self.check_Baixado_OV.setChecked(False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_ov_aberto(self):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.data, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where prodoc.quantidade > prodoc.produzido "
                           f"and oc.status = 'A' "
                           f"and oc.entradasaida = 'S';")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    dados = (emi, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_OV, tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_ov_baixado_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.data, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.status = 'B' "
                           f"and oc.entradasaida = 'S'"
                           f"and oc.cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    dados = (emi, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_OV, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_ov_aberto_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.data, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where prodoc.quantidade > prodoc.produzido "
                           f"and oc.status = 'A' "
                           f"and oc.entradasaida = 'S'"
                           f"and oc.cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    dados = (emi, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_OV, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_ov_todos_com_cliente(self, id_cliente):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.data, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S'"
                           f"and oc.cliente = {id_cliente};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    dados = (emi, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs)
                    tabela_nova.append(dados)
            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela(self.table_OV, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_exp_por_status(self):
        try:
            limpa_tabela(self.table_Exp)

            self.widget_Progress.setHidden(False)

            abertas = self.check_Aberto_Exp.isChecked()
            fechadas = self.check_Baixado_Exp.isChecked()
            cliente = self.combo_Cliente_Exp.currentText()

            if cliente != "TODOS":
                if abertas and fechadas:
                    print("aberto, fechado com cliente")
                    Thread(target=self.dados_exp_total_cliente).start()
                elif abertas:
                    print("aberto com cliente")
                    Thread(target=self.dados_exp_total_aberto_cliente).start()
                elif fechadas:
                    print("fechado com cliente")
                    Thread(target=self.dados_exp_total_baixada_cliente).start()
                else:
                    self.widget_Progress.setHidden(True)

            else:
                if not fechadas:
                    if abertas:
                        print("todos só abertos")
                        Thread(target=self.dados_exp_total_aberto).start()
                    else:
                        self.widget_Progress.setHidden(True)
                else:
                    self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_exp_total_aberto(self):
        try:
            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where prodoc.quantidade > prodoc.produzido "
                           f"and oc.status = 'A' "
                           f"and oc.entradasaida = 'S' "
                           f"and (prodoc.id_expedicao IS NOT NULL OR prodoc.id_expedicao <> 0);")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)

                self.btn_Excel_Exp.setHidden(True)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_exp_total_aberto_cliente(self):
        try:
            cliente = self.combo_Cliente_Exp.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]

            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S' "
                           f"and prodoc.quantidade > prodoc.produzido "
                           f"and oc.status = 'A' "
                           f"and oc.cliente = {id_cliente} "
                           f"and (prodoc.id_expedicao IS NOT NULL OR prodoc.id_expedicao <> 0);")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)

                self.btn_Excel_Exp.setHidden(True)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_exp_total_baixada_cliente(self):
        try:
            cliente = self.combo_Cliente_Exp.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]

            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S' "
                           f"and prodoc.quantidade = prodoc.produzido "
                           f"and oc.cliente = {id_cliente} "
                           f"and (prodoc.id_expedicao IS NOT NULL OR prodoc.id_expedicao <> 0);")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)

                self.btn_Excel_Exp.setHidden(True)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_exp_total_cliente(self):
        try:
            cliente = self.combo_Cliente_Exp.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]

            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S' "
                           f"and oc.cliente = {id_cliente} "
                           f"and (prodoc.id_expedicao IS NOT NULL OR prodoc.id_expedicao <> 0);")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)

                self.btn_Excel_Exp.setHidden(True)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_exp_por_numero(self):
        try:
            self.widget_Progress.setHidden(False)

            num_exp = self.line_Num_Exp.text()

            if num_exp:
                Thread(target=self.exp_total_por_numero).start()
            else:
                self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def exp_total_por_numero(self):
        try:
            num_exp = self.line_Num_Exp.text()

            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S' "
                           f"and prodoc.id_expedicao = {num_exp};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)
                self.btn_Excel_Exp.setHidden(False)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_exp_por_produto(self):
        if not self.processando:
            try:
                self.processando = True

                self.widget_Progress.setHidden(False)

                codigo_produto = self.line_Codigo_Exp.text()

                if codigo_produto:
                    codigo_produto = self.line_Codigo_Exp.text()
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                                   f"FROM produto where codigo = {codigo_produto};")
                    detalhes_produto = cursor.fetchall()
                    if not detalhes_produto:
                        mensagem_alerta('Este código de produto não existe!')
                        self.line_Codigo_Exp.clear()
                        self.widget_Progress.setHidden(True)
                    else:
                        codigo_produto = self.line_Codigo_Exp.text()
                        cur = conecta.cursor()
                        cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                                    f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                                    f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
                        detalhes_produto = cur.fetchall()
                        descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

                        self.line_Descricao_Exp.setText(descr)
                        self.line_Referencia_Exp.setText(ref)
                        self.line_UM_Exp.setText(um)

                        Thread(target=self.exp_total_por_produto).start()
                else:
                    self.widget_Progress.setHidden(True)

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def exp_total_por_produto(self):
        try:
            cod_prod = self.line_Codigo_Exp.text()

            tabela_nova = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT exp.data, prodoc.id_expedicao, oc.numero, cli.razao, prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, '') as ref, prod.unidade, prodoc.quantidade, "
                           f"prodoc.produzido, COALESCE(prodoc.id_pedido, '') as pedi, "
                           f"COALESCE(ped.num_req_cliente, '') as req, "
                           f"COALESCE(oc.obs, '') as obs, oc.status "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"INNER JOIN ordemexpedicao as exp ON prodoc.id_expedicao = exp.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where oc.entradasaida = 'S' "
                           f"and prod.codigo = {cod_prod};")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    emissao, num_exp, num_ov, clie, cod, descr, ref, um, qtde, qtde_entr, nume_pi, num_req, obs, \
                    status = i

                    emi = f'{emissao.day}/{emissao.month}/{emissao.year}'

                    if qtde == qtde_entr:
                        status_f = "B"
                    else:
                        status_f = "A"

                    dados = (emi, num_exp, clie, cod, descr, ref, um, qtde, num_ov, nume_pi, status_f)
                    tabela_nova.append(dados)
            if tabela_nova:
                lanca_tabela(self.table_Exp, tabela_nova)

                self.btn_Excel_Exp.setHidden(True)

            self.widget_Progress.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaVendasStatus()
    tela.show()
    qt.exec_()
