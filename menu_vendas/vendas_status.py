import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import lanca_tabela
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from forms.tela_vendas_status import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os


class TelaVendasStatus(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)
        self.layout_proprio()

        self.btn_Consultar_PI.clicked.connect(self.verifica_filtro_pi)
        self.dados_pi_aberto()

        self.btn_Consultar_OV.clicked.connect(self.verifica_filtro_ov)
        self.dados_ov_aberto()
        
    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor1)
            cor_widget(self.widget_Cor2)
            cor_widget(self.widget_Cor3)
            cor_widget(self.widget_Cor4)

            cor_fonte(self.label_13)
            cor_fonte(self.label_3)
            cor_fonte(self.label_14)
            cor_fonte(self.label_15)
            cor_fonte(self.label_2)
            cor_fonte(self.label_5)
            cor_fonte(self.label_56)
            cor_fonte(self.label_54)
            cor_fonte(self.label_58)
            cor_fonte(self.label_55)
            cor_fonte(self.label_59)
            cor_fonte(self.label_57)
            cor_fonte(self.label_6)
            cor_fonte(self.label_8)
            cor_fonte(self.label_9)

            cor_fonte(self.check_Aberto_PI)
            cor_fonte(self.check_Aberto_OV)
            cor_fonte(self.check_Baixado_OV)
            cor_fonte(self.check_Baixado_PI)

            cor_btn(self.btn_Consultar_PI)
            cor_btn(self.btn_Consultar_OV)

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
                lanca_tabela(self.table_PI, tabela_nova, edita_largura=False)

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
                lanca_tabela(self.table_PI, lista_de_listas_ordenada, edita_largura=False)

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
                lanca_tabela(self.table_PI, lista_de_listas_ordenada, edita_largura=False)

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
                lanca_tabela(self.table_PI, lista_de_listas_ordenada, edita_largura=False)

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
                lanca_tabela(self.table_OV, tabela_nova, edita_largura=False)

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
                lanca_tabela(self.table_OV, lista_de_listas_ordenada, edita_largura=False)

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
                lanca_tabela(self.table_OV, lista_de_listas_ordenada, edita_largura=False)

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
                lanca_tabela(self.table_OV, lista_de_listas_ordenada, edita_largura=False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaVendasStatus()
    tela.show()
    qt.exec_()
