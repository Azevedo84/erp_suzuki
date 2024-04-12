import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab, excluir_item_tab, limpa_tabela
from comandos.comando_lines import definir_data_atual
from comandos.comando_cores import cor_amarelo, cor_branco
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_conversoes import valores_para_float, valores_para_virgula
from forms.tela_oc_incluir import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor
from datetime import datetime, date, timedelta
import inspect
import os
from functools import partial


class TelaOcIncluir(QMainWindow, Ui_MainWindow):
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

        self.line_NumOC.editingFinished.connect(self.verifica_line_oc)
        self.date_Emissao.editingFinished.connect(self.verifica_emissao)
        self.line_CodForn.editingFinished.connect(self.verifica_line_fornecedor)
        self.line_Codigo.editingFinished.connect(self.verifica_line_codigo)
        self.line_IDReq.editingFinished.connect(self.verifica_line_idreq)
        self.line_Qtde.editingFinished.connect(self.verifica_line_qtde)
        self.line_Ipi.editingFinished.connect(self.atualiza_mascara_ipi)
        self.line_Unit.editingFinished.connect(self.verifica_line_unit)
        self.line_Frete.editingFinished.connect(self.atualiza_mascara_frete)
        self.line_Desconto.editingFinished.connect(self.atualiza_mascara_desconto)
        self.date_Entrega.editingFinished.connect(self.verifica_entrega)

        self.processando = False

        self.btn_ExcluirTudo.clicked.connect(partial(limpa_tabela, self.table_Produtos))
        self.btn_ExcluirItem.clicked.connect(partial(excluir_item_tab, self.table_Produtos,
                                                         "Produtos Ordem de Compra"))

        self.btn_AdicionarProd.clicked.connect(self.verifica_dados_completos)
        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.definir_validador()
        self.definir_entrega()
        definir_data_atual(self.date_Emissao)
        self.manipula_dados_req()

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
            cor_fonte(self.label_2)
            cor_fonte(self.label_25)
            cor_fonte(self.label_20)
            cor_fonte(self.label_27)
            cor_fonte(self.label_29)
            cor_fonte(self.label_25)
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

    def definir_entrega(self):
        try:
            data_hoje = date.today()
            data_entrega = data_hoje + timedelta(days=14)
            self.date_Entrega.setDate(data_entrega)

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

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_oc(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def verifica_sql_oc(self):
        try:
            num_oc = self.line_NumOC.text()

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, oc.data, oc.status FROM ordemcompra as oc "
                f"where oc.entradasaida = 'E' and oc.numero = {num_oc};")
            dados_oc = cursor.fetchall()

            if dados_oc:
                mensagem_alerta('Este número de OC já existe!')
                self.line_NumOC.clear()
                self.line_NumOC.setFocus()
            else:
                self.date_Emissao.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_emissao(self):
        if not self.processando:
            try:
                self.processando = True

                data_emissao_str = self.date_Emissao.text()

                try:
                    data_emissao = datetime.strptime(data_emissao_str, '%d/%m/%Y')

                    data_atual = date.today()

                    if data_emissao.year < data_atual.year:
                        mensagem_alerta(f'O ano da emissão é inferior '
                                                                    f'a {data_atual.year}!')
                        self.line_CodForn.setFocus()

                    elif data_emissao.year == data_atual.year:
                        if data_emissao.date() <= data_atual:
                            self.line_CodForn.setFocus()

                        else:
                            mensagem_alerta(f'A data de emissão é maior que a atual!')
                            self.line_CodForn.setFocus()

                    else:
                        mensagem_alerta(f'A data de emissão é maior que a atual!')

                except ValueError:
                    msg = f'A data de emissão não está no formato correto (dd/mm/aaaa)!'
                    print(msg)
                    mensagem_alerta(msg)

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_line_fornecedor(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def verifica_sql_fornecedor(self):
        try:
            cod_fornecedor = self.line_CodForn.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, razao FROM fornecedores where registro = {cod_fornecedor};")
            dados_fornecedor = cursor.fetchall()

            if not dados_fornecedor:
                mensagem_alerta('Este Código de Fornecedor não existe!')
                self.line_CodForn.clear()
                self.line_CodForn.setFocus()
            else:
                nom_fornecedor = dados_fornecedor[0][1]
                self.line_NomeForn.setText(nom_fornecedor)
                self.line_Codigo.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_codigo(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

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
            descricao, referencia, un, local, qtde, conj, embalagem = detalhes_produto[0]

            self.line_Descricao.setText(descricao)
            self.line_UM.setText(un)

            cursor = conecta.cursor()
            cursor.execute(f"SELECT COALESCE(prodreq.id, 'X'), COALESCE(prodreq.numero, 'X'), "
                           f"prod.codigo, prod.descricao as DESCRICAO, "
                           f"CASE prod.embalagem when 'SIM' then prodreq.referencia "
                           f"else prod.obs end as REFERENCIA, "
                           f"prod.unidade, prodreq.quantidade "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"WHERE prodreq.status = 'A' AND prod.codigo = {cod_produto};")
            extrair_req = cursor.fetchall()
            if not extrair_req:
                mensagem_alerta('Indique o "ID" do Produto da Requisição!')
                self.line_IDReq.setFocus()

            elif len(extrair_req) > 1:
                mensagem_alerta('Indique o "ID" do Produto da Requisição!')
                id_req, num_req, codigo_item_req, descricao_req, referencia_req, um_req, qtde_req = extrair_req[0]
                self.line_Referencia.setText(referencia_req)
                if embalagem == "SIM":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                elif embalagem == "SER":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                else:
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_branco};")

                self.line_IDReq.setFocus()
            else:
                id_req, num_req, codigo_item_req, descricao_req, referencia_req, um_req, qtde_req = extrair_req[0]
                self.line_Referencia.setText(referencia_req)
                if embalagem == "SIM":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                elif embalagem == "SER":
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_amarelo};")
                else:
                    self.line_Referencia.setStyleSheet(f"background-color: {cor_branco};")

                self.line_IDReq.setText(id_req)
                self.line_Qtde.setText(str(qtde_req))
                self.line_Qtde.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_idreq(self):
        if not self.processando:
            try:
                self.processando = True

                id_req_prod = self.line_IDReq.text()

                if len(id_req_prod) == 0:
                    vai_naovai = False

                    mensagem_alerta('O campo "ID Requis.:" não pode estar vazio')
                    self.line_IDReq.clear()
                    self.line_IDReq.setFocus()
                elif int(id_req_prod) == 0:
                    vai_naovai = False

                    mensagem_alerta('O campo "ID Requis.:" não pode ser "0"')
                    self.line_IDReq.clear()
                    self.line_IDReq.setFocus()
                else:
                    vai_naovai = self.verifica_sql_idreq()

                return vai_naovai

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

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
                vai_naovai = False

                mensagem_alerta('Este "ID" do Produto da Requisição não existe!')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            else:
                vai_naovai = True
                self.line_Qtde.setFocus()

            return vai_naovai

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_line_qtde(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def atualiza_mascara_ipi(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def verifica_line_unit(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

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
        if not self.processando:
            try:
                self.processando = True

                data_entrega_str = self.date_Entrega.text()
                try:
                    data_entrega = datetime.strptime(data_entrega_str, '%d/%m/%Y')

                    data_atual = datetime.combine(date.today(), datetime.min.time())

                    if data_entrega < data_atual:
                        mensagem_alerta(f'A data de entrega não pode ser menor que a '
                                                                    f'atual!')
                    else:
                        self.verifica_dados_completos()

                except ValueError:
                    mensagem_alerta(f'A data de entrega não está no formato correto '
                                                                f'(dd/mm/aaaa)!')

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_dados_completos(self):
        try:
            num_oc = self.line_NumOC.text()
            cod_fornecedor = self.line_CodForn.text()
            cod_produto = self.line_Codigo.text()
            id_req = self.line_IDReq.text()
            qtde = self.line_Qtde.text()
            unit = self.line_Unit.text()

            if not num_oc:
                mensagem_alerta('O campo "Nº OC:" não pode estar vazio')
                self.line_NumOC.clear()
                self.line_NumOC.setFocus()
            elif not cod_fornecedor:
                mensagem_alerta('O campo "Cód. For.:" não pode estar vazio')
                self.line_CodForn.clear()
                self.line_CodForn.setFocus()
            elif not cod_produto:
                mensagem_alerta('O campo "Código:" não pode estar vazio')
                self.line_Codigo.clear()
                self.line_Codigo.setFocus()
            elif not id_req:
                mensagem_alerta('O campo "ID Requis.:" não pode estar vazio')
                self.line_IDReq.clear()
                self.line_IDReq.setFocus()
            elif not qtde:
                mensagem_alerta('O campo "Qtde:" não pode estar vazio')
                self.line_Qtde.clear()
                self.line_Qtde.setFocus()
            elif not unit:
                mensagem_alerta('O campo "R$/Unid:" não pode estar vazio')
                self.line_Unit.clear()
                self.line_Unit.setFocus()
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

            dados = [id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega]

            extrai_produtos = extrair_tabela(self.table_Produtos)

            ja_existe = False
            for i in extrai_produtos:
                id_req_e, cod_produto_e, descr_e, ref_e, um_e, qtde_e, unit_e, ipi_e, total_e, entrega_e = i

                if id_req_e == id_req:
                    ja_existe = True
                    break

            if not ja_existe:
                extrai_produtos.append(dados)
                if extrai_produtos:
                    lanca_tabela(self.table_Produtos, extrai_produtos)

                    self.atualiza_valor_total()
                    self.pinta_tabela()
                    self.limpa_produtos()
                    self.line_Codigo.setFocus()
            else:
                mensagem_alerta(f'O item selecionado já está presente na tabela'
                                                            f'"Produtos OC".')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pinta_tabela(self):
        try:
            dados_tabela = extrair_tabela(self.table_Produtos)

            for index, dados in enumerate(dados_tabela):
                id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega = dados
                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, descricao, embalagem FROM produto where codigo = {cod_produto};")
                dados_produto = cursor.fetchall()
                ides, descr, embalagem = dados_produto[0]
                if embalagem == "SIM":
                    self.table_Produtos.item(index, 3).setBackground(QColor(cor_amarelo))
                elif embalagem == "SER":
                    self.table_Produtos.item(index, 3).setBackground(QColor(cor_amarelo))

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
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def atualiza_mascara_desconto(self):
        if not self.processando:
            try:
                self.processando = True

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

            finally:
                self.processando = False

    def atualiza_valor_total(self):
        try:
            extrai_produtos = extrair_tabela(self.table_Produtos)

            total_mercadorias = 0.00
            total_ipi = 0.00

            for i in extrai_produtos:
                id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega = i

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
                    id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega = itens

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

            emissao_oc = self.date_Emissao.date()
            data_emi = emissao_oc.toString("yyyy-MM-dd")

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
            cursor.execute("select GEN_ID(GEN_ORDEMCOMPRA_ID,0) from rdb$database;")
            ultimo_oc0 = cursor.fetchall()
            ultimo_oc1 = ultimo_oc0[0]
            ultimo_oc = int(ultimo_oc1[0]) + 1

            cursor = conecta.cursor()
            cursor.execute(f"Insert into ordemcompra "
                           f"(ID, ENTRADASAIDA, NUMERO, DATA, STATUS, FORNECEDOR, LOCALESTOQUE, FRETE, DESCONTOS, OBS) "
                           f"values (GEN_ID(GEN_ORDEMCOMPRA_ID,1), "
                           f"'E', {numero_oc_int}, '{data_emi}', 'A', {id_fornecedor}, '1', {frete_oc_float}, "
                           f"{desconto_oc_float}, '{obs_m}');")

            dados_alterados = extrair_tabela(self.table_Produtos)

            for itens in dados_alterados:
                id_req, cod_produto, descr, ref, um, qtde, unit, ipi, total, entrega = itens

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
                               f"values (GEN_ID(GEN_PRODUTOORDEMCOMPRA_ID,1), {ultimo_oc}, "
                               f"{id_produto}, {qtde_item_float}, {valor_unit_float}, {ipi_item_float}, "
                               f"'{entrega_prod}', {numero_oc_int}, '{codigo_int}', 0.0, {id_req_int});")

                cursor = conecta.cursor()
                cursor.execute(f"UPDATE produtoordemrequisicao SET STATUS = 'B', "
                               f"PRODUZIDO = {qtde_item_float} WHERE id = {id_req};")

            conecta.commit()

            mensagem_alerta(f'Ordem de Compra foi lançada com sucesso!')

            self.limpar_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaOcIncluir()
    tela.show()
    qt.exec_()
