import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab, excluir_item_tab, limpa_tabela
from comandos.comando_lines import definir_data_atual
from comandos.comando_cores import cor_amarelo, cor_branco, cor_cinza_claro
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_conversoes import valores_para_float, valores_para_virgula
from forms.tela_oc_alterar import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtGui import QColor, QKeySequence
from PyQt5.QtCore import Qt
from datetime import datetime, date, timedelta
import inspect
import os
from functools import partial


class TelaOcAlterar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_compra_sol.png")
        tamanho_aplicacao(self)
        self.layout_tabela_requisicao(self.table_ReqAbertas)
        self.layout_tabela_oc(self.table_Produtos)
        self.layout_proprio()

        self.tab_shortcut = QShortcut(QKeySequence(Qt.Key_Tab), self)
        self.tab_shortcut.activated.connect(self.manipula_tab)

        self.definir_botoes_e_comandos()
        self.definir_validador()
        self.definir_entrega()
        definir_data_atual(self.date_Emissao)
        self.manipula_dados_req()

        self.table_Produtos.cellChanged.connect(self.atualiza_valores_tabela_prod)

        self.btn_ExcluirTudo.clicked.connect(partial(limpa_tabela, self.table_Produtos))
        self.btn_ExcluirItem.clicked.connect(partial(excluir_item_tab, self.table_Produtos,
                                                     "Produtos Ordem de Compra"))

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

            cor_fonte(self.label)
            cor_fonte(self.label_16)
            cor_fonte(self.label_12)
            cor_fonte(self.label_18)
            cor_fonte(self.label_19)
            cor_fonte(self.label_25)
            cor_fonte(self.label_20)
            cor_fonte(self.label_27)
            cor_fonte(self.label_29)
            cor_fonte(self.label_31)
            cor_fonte(self.label_37)
            cor_fonte(self.label_39)
            cor_fonte(self.label_4)
            cor_fonte(self.label_43)
            cor_fonte(self.label_44)
            cor_fonte(self.label_46)
            cor_fonte(self.label_47)
            cor_fonte(self.label_48)
            cor_fonte(self.label_45)
            cor_fonte(self.label_49)
            cor_fonte(self.label_50)
            cor_fonte(self.label_51)
            cor_fonte(self.label_55)
            cor_fonte(self.label_52)
            cor_fonte(self.label_54)
            cor_fonte(self.label_6)
            cor_fonte(self.label_7)
            cor_fonte(self.label_9)
            cor_fonte(self.label_titulo_2)

            cor_btn(self.btn_Salvar)
            cor_btn(self.btn_ExcluirItem)
            cor_btn(self.btn_ExcluirTudo)
            cor_btn(self.btn_Limpar)
            cor_btn(self.btn_AdicionarProd)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_requisicao(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 50)
            nome_tabela.setColumnWidth(1, 50)
            nome_tabela.setColumnWidth(2, 40)
            nome_tabela.setColumnWidth(3, 220)
            nome_tabela.setColumnWidth(4, 130)
            nome_tabela.setColumnWidth(5, 40)
            nome_tabela.setColumnWidth(6, 65)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela_oc(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 55)
            nome_tabela.setColumnWidth(1, 40)
            nome_tabela.setColumnWidth(2, 240)
            nome_tabela.setColumnWidth(3, 140)
            nome_tabela.setColumnWidth(4, 40)
            nome_tabela.setColumnWidth(5, 90)
            nome_tabela.setColumnWidth(6, 95)
            nome_tabela.setColumnWidth(7, 70)
            nome_tabela.setColumnWidth(8, 95)
            nome_tabela.setColumnWidth(9, 90)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def dados_banco_convertidos(self, id_oc):
        try:
            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT ocprod.numero, ocprod.dataentrega, prod.codigo, prod.descricao, prod.embalagem, "
                f"prod.obs, prod.unidade, "
                f"ocprod.quantidade, ocprod.unitario, "
                f"ocprod.ipi, ocprod.id_prod_req, ocprod.produzido "
                f"FROM produtoordemcompra as ocprod "
                f"INNER JOIN produto as prod ON ocprod.produto = prod.ID "
                f"where ocprod.mestre = {id_oc};")
            dados_produtos = cursor.fetchall()

            tabela = []
            erros = 0
            for i in dados_produtos:
                numero, entrega, cod, descr, embal, ref, um, qtde, unit, ipi, id_req, qtde_nf = i

                if not id_req:
                    mensagem_alerta(f'O Código {cod} está sem a requisição '
                                    f'vinculada com a OC!')
                    erros += 1
                else:
                    data_for = entrega.strftime('%d/%m/%Y')

                    if qtde_nf:
                        qtde_nf_float = float(qtde_nf)
                        qtde_nf_vi = valores_para_virgula(str(qtde_nf_float))
                    else:
                        qtde_nf_vi = "0,00"

                    if qtde:
                        qtde_float = float(qtde)
                        qtde_virg = valores_para_virgula(str(qtde_float))
                    else:
                        qtde_float = 0.00
                        qtde_virg = "0,00"

                    if unit:
                        unit_float = float(unit)
                        unit_2casas = ("%.4f" % unit_float)
                        unit_string = valores_para_virgula(unit_2casas)
                        unit_fim = "R$ " + unit_string
                    else:
                        unit_float = 0.00
                        unit_fim = "R$ 0,0000"

                    if ipi:
                        ipi_float = valores_para_float(ipi)
                        ipi_2casas = ("%.2f" % ipi_float)
                        ipi_string = valores_para_virgula(ipi_2casas)
                        ipi_fim = ipi_string + "%"
                    else:
                        ipi_fim = "0,00%"

                    total_float = qtde_float * unit_float
                    total_2casas = ("%.2f" % total_float)
                    total_string = valores_para_virgula(total_2casas)
                    total_fim = "R$ " + total_string

                    dados = (id_req, cod, descr, ref, um, qtde_virg, unit_fim, ipi_fim, total_fim, data_for, qtde_nf_vi)
                    tabela.append(dados)

            return tabela

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_tab(self):
        try:
            if self.line_NumOC.hasFocus():
                self.verifica_line_oc()

            elif self.date_Emissao.hasFocus():
                self.verifica_emissao()

            elif self.line_CodForn.hasFocus():
                self.verifica_line_fornecedor()

            elif self.line_Codigo.hasFocus():
                self.verifica_line_codigo()

            elif self.line_IDReq.hasFocus():
                self.verifica_line_idreq()

            elif self.line_Qtde.hasFocus():
                self.verifica_line_qtde()

            elif self.line_Unit.hasFocus():
                self.verifica_line_unit()

            elif self.line_Ipi.hasFocus():
                self.atualiza_mascara_ipi()

            elif self.date_Entrega.hasFocus():
                self.verifica_entrega()

            elif self.line_Frete.hasFocus():
                self.atualiza_mascara_frete()

            elif self.line_Desconto.hasFocus():
                self.atualiza_mascara_desconto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def definir_botoes_e_comandos(self):
        try:
            self.line_NumOC.returnPressed.connect(lambda: self.verifica_line_oc())
            self.line_CodForn.returnPressed.connect(lambda: self.verifica_line_fornecedor())
            self.line_Codigo.returnPressed.connect(lambda: self.verifica_line_codigo())
            self.line_IDReq.returnPressed.connect(lambda: self.verifica_line_idreq())
            self.line_Qtde.returnPressed.connect(lambda: self.verifica_line_qtde())
            self.line_Ipi.returnPressed.connect(lambda: self.atualiza_mascara_ipi())
            self.line_Unit.returnPressed.connect(lambda: self.verifica_line_unit())
            self.btn_AdicionarProd.clicked.connect(self.verifica_entrega)

            self.line_Frete.returnPressed.connect(lambda: self.atualiza_mascara_frete())
            self.line_Desconto.returnPressed.connect(lambda: self.atualiza_mascara_desconto())

            self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def definir_validador(self):
        try:
            validator = QtGui.QIntValidator(0, 1234567, self.line_NumOC)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_NumOC.setValidator(validator)

            validator = QtGui.QIntValidator(0, 1234567, self.line_CodForn)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_CodForn.setValidator(validator)

            validator = QtGui.QIntValidator(0, 1234567, self.line_Codigo)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Codigo.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.000, 3, self.line_Qtde)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Qtde.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 999.00, 2, self.line_Ipi)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Ipi.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.0000, 4, self.line_Unit)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Unit.setValidator(validator)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def definir_entrega(self):
        try:
            data_hoje = date.today()
            data_entrega = data_hoje + timedelta(days=14)
            self.date_Entrega.setDate(data_entrega)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_oc(self):
        try:
            num_oc = self.line_NumOC.text()
            if len(num_oc) == 0:
                mensagem_alerta('O campo "Nº OC:" não pode estar vazio')
                self.line_NumOC.clear()
                self.line_NumOC.setFocus()
            elif int(num_oc) == 0:
                mensagem_alerta('O campo "Nº OC:" não pode ser "0"')
                self.line_NumOC.clear()
                self.line_NumOC.setFocus()
            else:
                self.verifica_sql_oc()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_sql_oc(self):
        try:
            num_oc = self.line_NumOC.text()

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.id, oc.numero, oc.data, oc.fornecedor "
                f"FROM ordemcompra as oc "
                f"where oc.entradasaida = 'E' and oc.numero = {num_oc} and oc.status = 'A';")
            dados_oc = cursor.fetchall()

            if not dados_oc:
                mensagem_alerta('Este número de OC não existe ou já foi encerrada!')
                self.line_NumOC.clear()
            else:
                self.lanca_dados_ordemcompra()

                id_oc = dados_oc[0][0]

                cursor = conecta.cursor()
                cursor.execute(
                    f"SELECT ocprod.numero, ocprod.dataentrega, prod.codigo, prod.descricao, prod.embalagem, "
                    f"prod.obs, prod.unidade, "
                    f"ocprod.quantidade, ocprod.unitario, "
                    f"ocprod.ipi, ocprod.id_prod_req, ocprod.produzido "
                    f"FROM produtoordemcompra as ocprod "
                    f"INNER JOIN produto as prod ON ocprod.produto = prod.ID "
                    f"where ocprod.mestre = {id_oc};")
                dados_produtos = cursor.fetchall()

                if dados_produtos:
                    self.lanca_dados_produtoordemcompra(dados_produtos)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def lanca_dados_ordemcompra(self):
        try:
            num_oc = self.line_NumOC.text()

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, oc.data, oc.fornecedor, oc.frete, oc.descontos, oc.obs "
                f"FROM ordemcompra as oc "
                f"where oc.entradasaida = 'E' and oc.numero = {num_oc} and oc.status = 'A';")
            dados_oc = cursor.fetchall()

            emissao = dados_oc[0][1]
            id_forn = dados_oc[0][2]
            frete = dados_oc[0][3]
            desconto = dados_oc[0][4]
            obs = dados_oc[0][5]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, registro, razao FROM fornecedores where id = {id_forn};")
            dados_fornecedor = cursor.fetchall()

            cod_fornecedor = str(dados_fornecedor[0][1])
            nom_fornecedor = dados_fornecedor[0][2]

            self.date_Emissao.setDate(emissao)
            self.line_CodForn.setText(cod_fornecedor)
            self.line_NomeForn.setText(nom_fornecedor)

            self.line_Frete.setText(str(frete))
            self.atualiza_mascara_frete()

            self.line_Desconto.setText(str(desconto))
            self.atualiza_mascara_desconto()

            self.line_Obs.setText(obs)

            self.line_Codigo.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def lanca_dados_produtoordemcompra(self, dados_produtos):
        try:
            tabela = []
            erros = 0
            for i in dados_produtos:
                numero, entrega, cod, descr, embal, ref, um, qtde, unit, ipi, id_req, qtde_nf = i

                if not id_req:
                    mensagem_alerta(f'O Código {cod} está sem a requisição '
                                                                f'vinculada com a OC!')
                    erros += 1
                else:
                    data_for = entrega.strftime('%d/%m/%Y')

                    if qtde_nf:
                        qtde_nf_float = float(qtde_nf)
                        qtde_nf_vi = valores_para_virgula(str(qtde_nf_float))
                    else:
                        qtde_nf_vi = "0,00"

                    if qtde:
                        qtde_float = float(qtde)
                        qtde_virg = valores_para_virgula(str(qtde_float))
                    else:
                        qtde_float = 0.00
                        qtde_virg = "0,00"

                    if unit:
                        unit_float = float(unit)
                        unit_2casas = ("%.4f" % unit_float)
                        unit_string = valores_para_virgula(unit_2casas)
                        unit_fim = "R$ " + unit_string
                    else:
                        unit_float = 0.00
                        unit_fim = "R$ 0,0000"

                    if ipi:
                        ipi_float = valores_para_float(ipi)
                        ipi_2casas = ("%.2f" % ipi_float)
                        ipi_string = valores_para_virgula(ipi_2casas)
                        ipi_fim = ipi_string + "%"
                    else:
                        ipi_fim = "0,00%"

                    total_float = qtde_float * unit_float
                    total_2casas = ("%.2f" % total_float)
                    total_string = valores_para_virgula(total_2casas)
                    total_fim = "R$ " + total_string

                    dados = (id_req, cod, descr, ref, um, qtde_virg, unit_fim, ipi_fim, total_fim, data_for, qtde_nf_vi)
                    tabela.append(dados)

            if erros == 0:
                if tabela:
                    lanca_tabela(self.table_Produtos, tabela, zebra=False)

                    self.bloqueios_tabela_produtos(tabela)
                    self.atualiza_valor_total()
                    self.pinta_tabela()
                    self.limpa_produtos()
                    self.line_Codigo.setFocus()
            else:
                self.limpar_tudo()
                self.line_NumOC.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_emissao(self):
        try:
            data_emissao_str = self.date_Emissao.text()

            try:
                data_emissao = datetime.strptime(data_emissao_str, '%d/%m/%Y')

                data_atual = date.today()

                if data_emissao.year < data_atual.year:
                    mensagem_alerta(f'O ano da emissão não pode ser inferior '
                                                                f'a {data_atual.year}!')
                elif data_emissao.year == data_atual.year:
                    if data_emissao.date() <= data_atual:
                        self.line_CodForn.setFocus()
                    else:
                        mensagem_alerta(f'A data de emissão não pode ser maior que a atual!')
                else:
                    mensagem_alerta(f'A data de emissão não pode ser maior que a atual!')
            except ValueError:
                print("A data de emissão não está no formato correto (dd/mm/aaaa).")
                mensagem_alerta(f'A data de emissão não está no formato correto (dd/mm/aaaa)!')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_fornecedor(self):
        try:
            cod_fornecedor = self.line_CodForn.text()
            if len(cod_fornecedor) == 0:
                mensagem_alerta('O campo "Cód. For.:" não pode estar vazio')
                self.line_CodForn.clear()
                self.line_CodForn.setFocus()
            elif int(cod_fornecedor) == 0:
                mensagem_alerta('O campo "Cód. For.:" não pode ser "0"')
                self.line_CodForn.clear()
                self.line_CodForn.setFocus()
            else:
                self.verifica_sql_fornecedor()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_sql_fornecedor(self):
        try:
            cod_fornecedor = self.line_CodForn.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()

            if not dados_fornecedor:
                mensagem_alerta('Este Código de Fornecedor não existe!')
                self.line_CodForn.clear()
            else:
                nom_fornecedor = dados_fornecedor[0][1]
                self.line_NomeForn.setText(nom_fornecedor)
                self.line_Codigo.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_codigo(self):
        try:
            cod_produto = self.line_Codigo.text()

            if len(cod_produto) == 0:
                mensagem_alerta('O campo "Código:" não pode estar vazio')
                self.line_Codigo.clear()
                self.line_Codigo.setFocus()
            elif int(cod_produto) == 0:
                mensagem_alerta('O campo "Código:" não pode ser "0"')
                self.line_Codigo.clear()
                self.line_Codigo.setFocus()
            else:
                self.verifica_sql_codigo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_sql_codigo(self):
        try:
            cod_produto = self.line_Codigo.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                           f"FROM produto where codigo = {cod_produto};")
            detalhes_produto = cursor.fetchall()

            if not detalhes_produto:
                mensagem_alerta('Este Código de Produto não existe!')
                self.line_CodForn.clear()
            else:
                self.lanca_dados_codigo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def lanca_dados_codigo(self):
        try:
            cod_produto = self.line_Codigo.text()

            cur = conecta.cursor()
            cur.execute(f"SELECT prod.descricao, COALESCE(prod.obs, ' ') as obs, prod.unidade, "
                        f"prod.localizacao, prod.quantidade, conj.conjunto, prod.embalagem "
                        f"FROM produto as prod "
                        f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                        f"where codigo = {cod_produto};")
            detalhes_produto = cur.fetchall()
            descricao, referencia, un, local, saldo, conj, embalagem = detalhes_produto[0]

            self.line_Descricao.setText(descricao)
            self.line_UM.setText(un)

            itens_encontrados = []

            dados_req_abertas = extrair_tabela(self.table_ReqAbertas)
            for i in dados_req_abertas:
                if cod_produto in i:
                    id_prod_req, num_req, cod, descr, ref, um, qtde = i
                    tt = (id_prod_req, num_req, cod, descr, ref, um, qtde)
                    itens_encontrados.append(tt)

            if not itens_encontrados:
                mensagem_alerta('Indique o "ID" do Produto da Requisição!')
                self.line_IDReq.setFocus()

            elif len(itens_encontrados) > 1:
                mensagem_alerta('Indique o "ID" do Produto da Requisição!')
                self.line_Referencia.setText(referencia)
                if embalagem == "SIM":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                elif embalagem == "SER":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                else:
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_branco};")

                self.line_IDReq.setFocus()

            else:
                for dados in itens_encontrados:
                    id_prod_reqs, num_reqs, cods, descrs, refs, ums, qtdes = dados

                    self.line_Referencia.setText(refs)

                    if embalagem == "SIM":
                        self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                    elif embalagem == "SER":
                        self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                    else:
                        self.line_Referencia.setStyleSheet(f"background-color: {cor_branco};")

                    self.line_IDReq.setText(id_prod_reqs)
                    self.line_Qtde.setText(str(qtdes))
                    self.line_Qtde.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_idreq(self):
        try:
            id_req_prod = self.line_IDReq.text()

            if len(id_req_prod) == 0:
                mensagem_alerta('O campo "ID Requis.:" não pode estar vazio')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            elif int(id_req_prod) == 0:
                mensagem_alerta('O campo "ID Requis.:" não pode ser "0"')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            else:
                self.verifica_sql_idreq()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_sql_idreq(self):
        try:
            id_req_prod = self.line_IDReq.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT COALESCE(prodreq.id, 'X'), COALESCE(prodreq.numero, 'X'), "
                           f"prod.codigo, prod.descricao as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then prodreq.referencia "
                           f"else prod.obs end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"WHERE prodreq.status = 'A' AND prodreq.id = {id_req_prod};")
            extrair_req = cursor.fetchall()
            if not extrair_req:
                mensagem_alerta('Este "ID" do Produto da Requisição não existe!')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            else:
                self.line_Qtde.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_qtde(self):
        try:
            qtde = self.line_Qtde.text()

            if len(qtde) == 0:
                mensagem_alerta('O campo "Qtde:" não pode estar vazio')
                self.line_Qtde.clear()
                self.line_Qtde.setFocus()
            elif qtde == "0":
                mensagem_alerta('O campo "Qtde:" não pode ser "0"')
                self.line_Qtde.clear()
                self.line_Qtde.setFocus()
            else:
                qtde_com_virgula = valores_para_virgula(qtde)

                self.line_Qtde.setText(qtde_com_virgula)
                self.line_Unit.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_mascara_ipi(self):
        try:
            ipi = self.line_Ipi.text()

            ipi_float = valores_para_float(ipi)
            ipi_2casas = ("%.2f" % ipi_float)
            valor_string = valores_para_virgula(ipi_2casas)
            valor_final = valor_string + "%"
            self.line_Ipi.setText(valor_final)

            self.date_Entrega.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_unit(self):
        try:
            unit = self.line_Unit.text()

            if len(unit) == 0:
                mensagem_alerta('O campo "R$/Unid:" não pode estar vazio')
                self.line_Unit.clear()
                self.line_Unit.setFocus()
            elif unit == "0":
                mensagem_alerta('O campo "R$/Unid:" não pode ser "0"')
                self.line_Unit.clear()
                self.line_Unit.setFocus()
            else:
                self.atualiza_mascara_unit()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_mascara_unit(self):
        try:
            unit = self.line_Unit.text()

            unit_float = valores_para_float(unit)
            unit_2casas = ("%.4f" % unit_float)
            valor_string = valores_para_virgula(unit_2casas)
            valor_final = "R$ " + valor_string
            self.line_Unit.setText(valor_final)

            self.calcular_valor_total_prod()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def calcular_valor_total_prod(self):
        try:
            qtde = self.line_Qtde.text()
            unit = self.line_Unit.text()

            if not qtde:
                mensagem_alerta('O campo "Qtde:" não pode estar vazio')
                self.line_Qtde.setFocus()
            elif not unit:
                mensagem_alerta('O campo "R$/Unid:" não pode estar vazio')
                self.line_Unit.setFocus()
            else:
                qtde_float = valores_para_float(qtde)

                unit_float = valores_para_float(unit)

                valor_total = qtde_float * unit_float

                total_2casas = ("%.2f" % valor_total)
                valor_string = valores_para_virgula(total_2casas)

                valor_final = "R$ " + valor_string
                self.line_ValorTotal.setText(valor_final)

                self.line_Ipi.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_entrega(self):
        try:
            data_entrega_str = self.date_Entrega.text()
            try:
                data_entrega = datetime.strptime(data_entrega_str, '%d/%m/%Y')

                data_atual = datetime.combine(date.today(), datetime.min.time())

                if data_entrega < data_atual:
                    mensagem_alerta(f'A data de entrega não pode ser menor que a atual!')
                else:
                    self.verifica_id_req()

            except ValueError:
                mensagem_alerta(f'A data de entrega não está no formato correto '
                                                            f'(dd/mm/aaaa)!')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_id_req(self):
        try:
            id_req_prod = self.line_IDReq.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT COALESCE(prodreq.id, 'X'), COALESCE(prodreq.numero, 'X'), "
                           f"prod.codigo, prod.descricao as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then prodreq.referencia "
                           f"else prod.obs end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"WHERE prodreq.status = 'A' AND prodreq.id = {id_req_prod};")
            extrair_req = cursor.fetchall()
            if not extrair_req:
                mensagem_alerta('Este "ID" do Produto da Requisição não existe!')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            else:
                self.verifica_dados_completos()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_dados_completos(self):
        try:
            num_oc = self.line_NumOC.text()
            cod_fornecedor = self.line_CodForn.text()
            cod_produto = self.line_Codigo.text()
            id_req = self.line_IDReq.text()
            qtde = self.line_Qtde.text()
            unit = self.line_Unit.text()

            if not num_oc:
                self.verifica_line_oc()
            elif not cod_fornecedor:
                self.verifica_line_fornecedor()
            elif not cod_produto:
                self.verifica_line_codigo()
            elif not id_req:
                self.verifica_line_idreq()
            elif not qtde:
                self.verifica_line_qtde()
            elif not unit:
                self.verifica_line_unit()
            else:
                self.manipula_dados_tabela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_dados_tabela(self):
        try:
            self.calcular_valor_total_prod()

            id_req = self.line_IDReq.text()

            cod_produto = self.line_Codigo.text()
            descr = self.line_Descricao.text()
            ref = self.line_Referencia.text()
            um = self.line_UM.text()

            qtde = self.line_Qtde.text()
            unit = self.line_Unit.text()
            ipi = self.line_Ipi.text()
            total = self.line_ValorTotal.text()
            entrega = self.date_Entrega.text()
            qtde_nf = "0,00"

            dados = [id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf]

            extrai_produtos = extrair_tabela(self.table_Produtos)

            ja_existe = False
            for i in extrai_produtos:
                id_req_e, cod_produto_e, descr_e, ref_e, um_e, qtde_e, unit_e, ipi_e, total_e, entrega_e, qtde_nf_e = i

                if id_req_e == id_req:
                    ja_existe = True
                    break

            if not ja_existe:
                extrai_produtos.append(dados)
                if extrai_produtos:
                    lanca_tabela(self.table_Produtos, extrai_produtos, zebra=False)

                self.bloqueios_tabela_produtos(extrai_produtos)
                self.atualiza_valor_total()
                self.pinta_tabela()
                self.limpa_produtos()
                self.line_Codigo.setFocus()

                tabela_req = []

                dados_req_abertas = extrair_tabela(self.table_ReqAbertas)
                for i in dados_req_abertas:
                    if id_req in i:
                        pass
                    else:
                        id_prod_req, num_req, cod, descr, ref, um, qtde = i
                        tt = (id_prod_req, num_req, cod, descr, ref, um, qtde)
                        tabela_req.append(tt)

                if tabela_req:
                    lanca_tabela(self.table_ReqAbertas, tabela_req)
            else:
                mensagem_alerta(f'O item selecionado já está presente na tabela'
                                                            f'"Produtos OC".')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def bloqueios_tabela_produtos(self, dados_tabela):
        try:
            for index, dados in enumerate(dados_tabela):
                id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = dados

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, codigo, embalagem FROM produto where codigo = '{cod_produto}';")
                dados_produto = cursor.fetchall()
                id_produto, codigo, embalagem = dados_produto[0]

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][0]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 0, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 1, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][2]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 2, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][3]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 3, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][4]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 4, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][8]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 8, item)

                item = QtWidgets.QTableWidgetItem(str(dados_tabela[index][10]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table_Produtos.setItem(index, 10, item)

                if embalagem == "SIM" or embalagem == "SER":
                    self.table_Produtos.item(index, 2).setBackground(QColor(cor_amarelo))

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pinta_tabela(self):
        try:
            dados_tabela = extrair_tabela(self.table_Produtos)

            for index, dados in enumerate(dados_tabela):
                id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = dados

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, descricao, embalagem FROM produto where codigo = {cod_produto};")
                dados_produto = cursor.fetchall()
                ides, descr, embalagem = dados_produto[0]
                if embalagem == "SIM":
                    self.table_Produtos.item(index, 3).setBackground(QColor(cor_amarelo))
                elif embalagem == "SER":
                    self.table_Produtos.item(index, 3).setBackground(QColor(cor_amarelo))

                qtde_nf_float = valores_para_float(qtde_nf)

                if qtde_nf_float > 0.00:
                    num_colunas = len(dados_tabela[0])
                    for i in range(num_colunas):
                        self.table_Produtos.item(index, i).setBackground(QColor(cor_cinza_claro))

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_dados_req(self):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT COALESCE(prodreq.id, ''), COALESCE(prodreq.numero, ''), "
                           f"prod.codigo, prod.descricao as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then COALESCE(prodreq.referencia, '') "
                           f"else COALESCE(prod.obs, '') end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"WHERE prodreq.status = 'A' ORDER BY DESCRICAO;")
            extrair_req = cursor.fetchall()

            if extrair_req:
                lanca_tabela(self.table_ReqAbertas, extrair_req)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_mascara_frete(self):
        try:
            frete = self.line_Frete.text()

            frete_float = valores_para_float(frete)
            frete_2casas = ("%.2f" % frete_float)
            valor_string = valores_para_virgula(frete_2casas)
            valor_final = "R$ " + valor_string
            self.line_Frete.setText(valor_final)

            self.atualiza_valor_total()
            self.line_Desconto.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_mascara_desconto(self):
        try:
            desconto = self.line_Desconto.text()

            desconto_float = valores_para_float(desconto)
            desconto_2casas = ("%.2f" % desconto_float)
            valor_string = valores_para_virgula(desconto_2casas)
            valor_final = "R$ " + valor_string
            self.line_Desconto.setText(valor_final)

            self.atualiza_valor_total()
            self.line_Obs.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_valor_total(self):
        try:
            extrai_produtos = extrair_tabela(self.table_Produtos)

            total_mercadorias = 0.00
            total_ipi = 0.00

            if extrai_produtos:
                for i in extrai_produtos:
                    id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = i

                    qtde_float = valores_para_float(qtde)

                    unit_float = valores_para_float(unit)

                    ipi_float = valores_para_float(ipi)

                    total_ipi += qtde_float * (unit_float * (ipi_float / 100))
                    total_mercadorias += qtde_float * unit_float

            frete = self.line_Frete.text()
            frete_float = valores_para_float(frete)

            desconto = self.line_Desconto.text()
            desconto_float = valores_para_float(desconto)

            total_geral = total_ipi + total_mercadorias + frete_float - desconto_float

            total_ipi_2casas = ("%.2f" % total_ipi)
            valor_ipi_string = valores_para_virgula(total_ipi_2casas)
            valor_ipi_final = "R$ " + valor_ipi_string
            self.line_Total_Ipi.setText(valor_ipi_final)

            total_merc_2casas = ("%.2f" % total_mercadorias)
            valor_merc_string = valores_para_virgula(total_merc_2casas)
            valor_merc_final = "R$ " + valor_merc_string
            self.line_Total_Merc.setText(valor_merc_final)

            total_geral_2casas = ("%.2f" % total_geral)
            valor_geral_string = valores_para_virgula(total_geral_2casas)
            valor_geral_final = "R$ " + valor_geral_string
            self.line_Total_Geral.setText(valor_geral_final)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_valores_tabela_prod(self, row, column):
        try:
            if column == 5 or column == 6 or column == 7:
                self.verifica_nf_entrada(row)
                self.atualiza_valor_total()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_nf_entrada(self, row):
        try:
            item_qtde_nf = self.table_Produtos.item(row, 10)

            if item_qtde_nf:
                qtde_nf = item_qtde_nf.text()

                if qtde_nf != "0,00":
                    item_qtde = self.table_Produtos.item(row, 5)
                    if item_qtde:
                        qtde = item_qtde.text()
                        qtde_float = valores_para_float(qtde)

                        qtde_nf_float = valores_para_float(qtde_nf)
                        if qtde_float >= qtde_nf_float:
                            item_unit = self.table_Produtos.item(row, 6)
                            if item_unit:
                                unit = item_unit.text()
                                unit_float = valores_para_float(unit)
                                valor_total = qtde_float * unit_float

                                total_2casas = ("%.2f" % valor_total)
                                valor_string = valores_para_virgula(total_2casas)
                                valor_final = "R$ " + valor_string

                                item_total = self.table_Produtos.item(row, 8)
                                if item_total:
                                    item_total.setText(valor_final)
                        else:
                            mensagem_alerta(f'A quantidade da oc não pode ser menor que a '
                                                                        f'quantidade lançada na NF de compra!')
                            item_qtde.setText(qtde_nf)
                else:
                    self.atualiza_unitario(row)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualiza_unitario(self, row):
        try:
            item_qtde = self.table_Produtos.item(row, 5)
            if item_qtde:
                qtde = item_qtde.text()
                qtde_float = valores_para_float(qtde)

                if qtde_float > 0.00:
                    item_unit = self.table_Produtos.item(row, 6)
                    if item_unit:
                        unit = item_unit.text()
                        unit_float = valores_para_float(unit)

                        if unit_float > 0.00:
                            valor_total = qtde_float * unit_float

                            total_2casas = ("%.2f" % valor_total)
                            valor_string = valores_para_virgula(total_2casas)
                            valor_final = "R$ " + valor_string

                            item_total = self.table_Produtos.item(row, 8)
                            if item_total:
                                item_total.setText(valor_final)
                        else:
                            mensagem_alerta(f'O "R$/Unid." da oc não pode ser 0!')
                            item_unit.setText("R$ 1,0000")
                else:
                    mensagem_alerta(f'A quantidade da oc não pode ser 0!')
                    item_qtde.setText("1,00")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def limpa_produtos(self):
        try:
            self.line_IDReq.clear()

            self.line_Codigo.clear()
            self.line_Descricao.clear()
            self.line_Referencia.clear()
            self.line_UM.clear()

            self.line_Qtde.clear()
            self.line_Unit.clear()
            self.line_Ipi.clear()
            self.line_ValorTotal.clear()

            self.line_Referencia.setStyleSheet(f"background-color: {cor_branco};")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def limpar_tudo(self):
        try:
            self.line_NumOC.clear()

            self.line_IDReq.clear()

            self.line_Codigo.clear()
            self.line_Descricao.clear()
            self.line_Referencia.clear()
            self.line_UM.clear()

            self.line_Qtde.clear()
            self.line_Unit.clear()
            self.line_Ipi.clear()
            self.line_ValorTotal.clear()

            self.line_CodForn.clear()
            self.line_NomeForn.clear()

            self.line_Frete.clear()
            self.line_Desconto.clear()
            self.line_Total_Ipi.setText("R$ 0,00")
            self.line_Total_Merc.setText("R$ 0,00")
            self.line_Total_Geral.setText("R$ 0,00")
            self.line_Obs.clear()

            self.table_Produtos.setRowCount(0)
            self.table_ReqAbertas.setRowCount(0)

            self.definir_entrega()
            definir_data_atual(self.date_Emissao)
            self.manipula_dados_req()

            self.line_NumOC.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_salvamento(self):
        try:
            cod_fornecedor = self.line_CodForn.text()
            nome_fornecedor = self.line_NomeForn.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()

            if not dados_fornecedor:
                mensagem_alerta(f'O Fornecedor {nome_fornecedor} não está cadastrado!')
            else:
                testar_erros = 0
                dados_alterados = extrair_tabela(self.table_Produtos)
                for itens in dados_alterados:
                    id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = itens

                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, descricao FROM produto where codigo = {cod_produto};")
                    dados_produto = cursor.fetchall()
                    if not dados_produto:
                        mensagem_alerta(f'O produto {descr} não está cadastrado')
                        testar_erros = testar_erros + 1
                        break

                if testar_erros == 0:
                    self.salvar_ordem()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def salvar_ordem(self):
        try:
            cod_fornecedor = self.line_CodForn.text()

            numero_oc = self.line_NumOC.text()
            numero_oc_int = int(numero_oc)

            frete = self.line_Frete.text()
            frete_oc_float = valores_para_float(frete)

            desconto = self.line_Desconto.text()
            desconto_oc_float = valores_para_float(desconto)

            obs = self.line_Obs.text()
            obs_m = obs.upper()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()
            id_fornecedor, razao = dados_fornecedor[0]

            cursor = conecta.cursor()
            cursor.execute(f"UPDATE ordemcompra SET FORNECEDOR = {id_fornecedor}, FRETE = {frete_oc_float}, "
                           f"DESCONTOS = {desconto_oc_float}, OBS = '{obs_m}' WHERE numero = {numero_oc};")

            dados_alterados = extrair_tabela(self.table_Produtos)

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.id, oc.numero, oc.data, oc.fornecedor "
                f"FROM ordemcompra as oc "
                f"where oc.entradasaida = 'E' and oc.numero = {numero_oc} and oc.status = 'A';")
            dados_oc = cursor.fetchall()

            print("passou pelo update")

            if not dados_oc:
                mensagem_alerta('Este número de OC não existe ou já foi encerrada!')
                self.line_NumOC.clear()
            else:

                self.lanca_dados_ordemcompra()

                id_oc = dados_oc[0][0]
                dados_banco = self.dados_banco_convertidos(id_oc)

                conj_banco = set(map(tuple, dados_banco))
                conj_dados = set(map(tuple, dados_alterados))

                itens_a_excluir = conj_banco - conj_dados
                itens_a_inserir = conj_dados - conj_banco

                itens_a_excluir = list(itens_a_excluir)
                itens_a_inserir = list(itens_a_inserir)

                if itens_a_excluir:
                    for item in itens_a_excluir:
                        print("entrou no delete produto")
                        id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = item

                        id_req_int = int(id_req)

                        cur = conecta.cursor()
                        cur.execute(f"SELECT id, NUMERO "
                                    f"FROM produtoordemcompra where NUMERO = {numero_oc_int} "
                                    f"and ID_PROD_REQ = {id_req_int};")
                        det_prod = cur.fetchall()
                        ids, numero_oc = det_prod[0]

                        cursor = conecta.cursor()
                        cursor.execute(f"DELETE FROM produtoordemcompra WHERE ID = {ids};")

                        cursor = conecta.cursor()
                        cursor.execute(f"UPDATE produtoordemrequisicao SET STATUS = 'A', "
                                       f"PRODUZIDO = 0 WHERE id = {id_req};")

                        print("passei pelo delete prod")

                if itens_a_inserir:
                    for item in itens_a_inserir:
                        print("entrou no insert produto")
                        id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega, qtde_nf = item
                        codigo_int = int(cod_produto)

                        entrega_prod = datetime.strptime(entrega, '%d/%m/%Y').date()

                        qtde_item_float = valores_para_float(qtde)

                        valor_unit_float = valores_para_float(unit)

                        ipi_item_float = valores_para_float(ipi)

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT id, descricao FROM produto where codigo = {codigo_int};")
                        dados_produto = cursor.fetchall()

                        id_produto, descricao = dados_produto[0]

                        id_req_int = int(id_req)

                        cursor = conecta.cursor()
                        cursor.execute(f"Insert into produtoordemcompra (ID, MESTRE, PRODUTO, QUANTIDADE, UNITARIO, "
                                       f"IPI, DATAENTREGA, NUMERO, CODIGO, PRODUZIDO, ID_PROD_REQ) "
                                       f"values (GEN_ID(GEN_PRODUTOORDEMCOMPRA_ID,1), {id_oc}, "
                                       f"{id_produto}, {qtde_item_float}, {valor_unit_float}, {ipi_item_float}, "
                                       f"'{entrega_prod}', {numero_oc_int}, '{codigo_int}', 0.0, {id_req_int});")

                        print("passei pelo insert prod")

                        cursor = conecta.cursor()
                        cursor.execute(f"UPDATE produtoordemrequisicao SET STATUS = 'B', "
                                       f"PRODUZIDO = {qtde_item_float} WHERE id = {id_req};")

                print("passou pelo insert")
            conecta.commit()

            mensagem_alerta(f'Ordem de Compra foi alterada com sucesso!')

            self.limpar_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaOcAlterar()
    tela.show()
    qt.exec_()
