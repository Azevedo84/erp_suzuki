import sys
from banco_dados.conexao import conecta
from forms.tela_exp_incluir_v2 import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela_v2, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone, cor_fundo_tela
from comandos.conversores import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import socket
import traceback
from datetime import date, datetime
import getpass


class TelaExpedicaoV2(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.nome_computador = socket.gethostname()
        self.username = getpass.getuser()

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)

        self.tela_embalagem = []

        self.dados_de_volumes = []
        self.responsavel_volumes = []

        self.definir_combo_operacao()
        self.definir_combo_cliente_vendas()

        self.definir_combo_funcionario()
        self.definir_combo_veiculo()

        self.btn_Embalagens.clicked.connect(self.confere_responsavel)

        self.table_Vendas_Pendentes.viewport().installEventFilter(self)

        self.combo_Operacao.activated.connect(self.selecionar_operacao)

        self.combo_Resp_Frete.activated.connect(self.selecionar_responsavel)

        self.combo_Cliente_Vendas.activated.connect(self.lanca_vendas_pendentes)

        self.selecionar_operacao()

        self.stacked_Responsavel.setCurrentWidget(self.page)

        self.definir_emissao()
        self.definir_num_exp()

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

    def trata_excecao(self, nome_funcao, mensagem, arquivo, excecao):
        try:
            tb = traceback.extract_tb(excecao)
            num_linha_erro = tb[-1][1]

            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}"\n{mensagem} {num_linha_erro}')
            self.mensagem_alerta(f'Houve um problema no arquivo:\n\n{arquivo}\n\n'
                                 f'Comunique o desenvolvedor sobre o problema descrito abaixo:\n\n'
                                 f'{nome_funcao}: {mensagem}')

            grava_erro_banco(nome_funcao, mensagem, arquivo, num_linha_erro)

        except Exception as e:
            nome_funcao_trat = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            tb = traceback.extract_tb(exc_traceback)
            num_linha_erro = tb[-1][1]
            print(f'Houve um problema no arquivo: {self.nome_arquivo} na função: "{nome_funcao_trat}"\n'
                  f'{e} {num_linha_erro}')
            grava_erro_banco(nome_funcao_trat, e, self.nome_arquivo, num_linha_erro)

    def mensagem_alerta(self, mensagem):
        try:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setText(mensagem)
            alert.setWindowTitle("Atenção")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def pergunta_confirmacao(self, mensagem):
        try:
            confirmacao = QMessageBox()
            confirmacao.setIcon(QMessageBox.Question)
            confirmacao.setText(mensagem)
            confirmacao.setWindowTitle("Confirmação")

            sim_button = confirmacao.addButton("Sim", QMessageBox.YesRole)
            nao_button = confirmacao.addButton("Não", QMessageBox.NoRole)

            confirmacao.setDefaultButton(nao_button)

            confirmacao.exec_()

            if confirmacao.clickedButton() == sim_button:
                return True
            else:
                return False

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_num_exp(self):
        try:
            cursor = conecta.cursor()
            cursor.execute("select GEN_ID(GEN_ORDEMEXPEDICAO_ID,0) from rdb$database;")
            ultimo_id_req0 = cursor.fetchall()
            ultimo_id_req1 = ultimo_id_req0[0]
            ultimo_id_req2 = int(ultimo_id_req1[0]) + 1
            ultimo_id_req = str(ultimo_id_req2)
            self.line_Num_Exp.setText(ultimo_id_req)
            self.line_Num_Exp.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_operacao(self):
        try:
            tabela = []

            self.combo_Operacao.clear()

            #detalhes = ["VENDAS (COM PI/OV)", "INDUSTRIALIZAÇÃO", "CONSERTO", "RETORNOS DE REMESSAS", "NF MANUAL"]

            detalhes = ["VENDAS (COM PI/OV)"]

            for dadus in detalhes:
                tabela.append(dadus)

            self.combo_Operacao.addItems(tabela)

            self.combo_Operacao.setCurrentText("VENDAS (COM PI/OV)")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def selecionar_operacao(self):
        try:
            operacao = self.combo_Operacao.currentText()

            if operacao:
                if operacao == "VENDAS (COM PI/OV)":
                    self.stacked_Operacao.setCurrentWidget(self.page_vendas)
                elif operacao == "INDUSTRIALIZAÇÃO":
                    self.stacked_Operacao.setCurrentWidget(self.page_Indust)
                elif operacao == "CONSERTO":
                    self.stacked_Operacao.setCurrentWidget(self.page_Conserto)
                elif operacao == "RETORNOS DE REMESSAS":
                    self.stacked_Operacao.setCurrentWidget(self.page_Retornos)
                elif operacao == "NF MANUAL":
                    self.stacked_Operacao.setCurrentWidget(self.page_Manual)
                else:
                    self.stacked_Operacao.setCurrentWidget(self.page_Vazio)
            else:
                self.stacked_Operacao.setCurrentWidget(self.page_Vazio)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_cliente_vendas(self):
        try:
            self.combo_Cliente_Vendas.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute("SELECT id, razao FROM clientes where venda = 'S' order by razao;")
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Cliente_Vendas.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_vendas_pendentes(self):
        try:
            self.table_Vendas_Pendentes.setRowCount(0)
            self.table_Expedicao.setRowCount(0)

            tabela_nova = []

            cliente = self.combo_Cliente_Vendas.currentText()

            if cliente:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]

                cursor = conecta.cursor()
                cursor.execute(f"SELECT ped.id, prod.codigo, prod.descricao, "
                               f"COALESCE(prod.obs, '') as obs, "
                               f"prod.unidade, prodint.qtde, prodint.data_previsao, prod.quantidade, "
                               f"prod.localizacao, cli.razao "
                               f"FROM PRODUTOPEDIDOINTERNO as prodint "
                               f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                               f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                               f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                               f"where prodint.status = 'A' "
                               f"and ped.id_cliente = {id_cliente};")
                dados_interno = cursor.fetchall()

                if dados_interno:
                    for i in dados_interno:
                        num_ped, cod, descr, ref, um, qtde, entrega, saldo, local, cliente = i

                        qtde_float = valores_para_float(qtde)
                        saldo_float = valores_para_float(saldo)

                        if saldo_float >= qtde_float:
                            dados = (f"PI {num_ped}", cod, descr, ref, um, qtde_float, local, saldo_float, cliente)
                            tabela_nova.append(dados)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT oc.numero, prod.codigo, prod.descricao, COALESCE(prod.obs, ''), "
                               f"prod.unidade, prodoc.quantidade, "
                               f"prodoc.produzido, prod.quantidade, prod.localizacao, cli.razao "
                               f"FROM PRODUTOORDEMCOMPRA as prodoc "
                               f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                               f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                               f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                               f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                               f"where prodoc.quantidade > prodoc.produzido "
                               f"and oc.status = 'A' "
                               f"and oc.entradasaida = 'S'"
                               f"and oc.cliente = {id_cliente} "
                               f"and prod.quantidade > 0;")
                dados_interno = cursor.fetchall()
                if dados_interno:
                    for i in dados_interno:
                        num_ov, cod, descr, ref, um, qtde_total, qtde_entr, saldo, local, cliente = i

                        total_float = float(qtde_total)
                        entregue_float = float(qtde_entr)
                        saldo_float = float(saldo)

                        falta_ent = total_float - entregue_float
                        falta_arr = round(valores_para_float(falta_ent), 2)

                        if saldo_float >= falta_ent:
                            dados = (f"OV {num_ov}", cod, descr, ref, um, falta_arr, local, saldo_float, cliente)
                            tabela_nova.append(dados)

            else:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT ped.id, prod.codigo, prod.descricao, "
                               f"COALESCE(prod.obs, '') as obs, "
                               f"prod.unidade, prodint.qtde, prodint.data_previsao, prod.quantidade, "
                               f"prod.localizacao, cli.razao "
                               f"FROM PRODUTOPEDIDOINTERNO as prodint "
                               f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                               f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                               f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                               f"where prodint.status = 'A';")
                dados_interno = cursor.fetchall()

                if dados_interno:
                    for i in dados_interno:
                        num_ped, cod, descr, ref, um, qtde, entrega, saldo, local, cliente = i

                        qtde_float = valores_para_float(qtde)
                        saldo_float = valores_para_float(saldo)

                        if saldo_float >= qtde_float:
                            dados = (f"PI {num_ped}", cod, descr, ref, um, qtde_float, local, saldo_float, cliente)
                            tabela_nova.append(dados)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT oc.numero, prod.codigo, prod.descricao, COALESCE(prod.obs, ''), "
                               f"prod.unidade, prodoc.quantidade, "
                               f"prodoc.produzido, prod.quantidade, prod.localizacao, cli.razao "
                               f"FROM PRODUTOORDEMCOMPRA as prodoc "
                               f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                               f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                               f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                               f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                               f"where prodoc.quantidade > prodoc.produzido "
                               f"and oc.status = 'A' "
                               f"and oc.entradasaida = 'S'"
                               f"and prod.quantidade > 0;")
                dados_interno = cursor.fetchall()
                if dados_interno:
                    for i in dados_interno:
                        num_ov, cod, descr, ref, um, qtde_total, qtde_entr, saldo, local, cliente = i

                        total_float = float(qtde_total)
                        entregue_float = float(qtde_entr)
                        saldo_float = float(saldo)

                        falta_ent = total_float - entregue_float
                        falta_arr = round(valores_para_float(falta_ent), 2)

                        if saldo_float >= falta_ent:
                            dados = (f"OV {num_ov}", cod, descr, ref, um, falta_arr, local, saldo_float, cliente)
                            tabela_nova.append(dados)

            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[8])
                lanca_tabela_v2(self.table_Vendas_Pendentes, lista_de_listas_ordenada)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, source, event):
        try:
            tabela_vendas_pendentes = self.table_Vendas_Pendentes
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is tabela_vendas_pendentes.viewport()):
                item = tabela_vendas_pendentes.currentItem()

                cliente = self.combo_Cliente_Vendas.currentText()

                if item and cliente:
                    extrai_recomendados = extrair_tabela(tabela_vendas_pendentes)
                    item_selecionado = extrai_recomendados[item.row()]

                    self.manipula_venda_exp(item_selecionado)

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_venda_exp(self, item_selecionado):
        try:
            num, cod, desc, ref, um, qtde, local, saldo, cliente = item_selecionado

            extrai_produtos = extrair_tabela(self.table_Expedicao)

            dados = [cod, desc, ref, um, qtde, num]

            ja_existe = False

            for iii in extrai_produtos:
                cod_e, desc_e, ref_e, um_e, qtde_e, num_e = iii

                if cod == cod_e and num == num_e:
                    ja_existe = True
                    break

            if not ja_existe:
                extrai_produtos.append(dados)

            lanca_tabela_v2(self.table_Expedicao, extrai_produtos)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def confere_responsavel(self):
        dados_exp = extrair_tabela(self.table_Expedicao)

        responsavel = self.combo_Resp_Frete.currentText()
        cif_fob = self.combo_Frete.currentText()

        if dados_exp and responsavel and cif_fob:
            if self.responsavel_volumes and self.responsavel_volumes != responsavel:
                msg = (f'Deseja realmente alterar o responsável pelo frete?\n'
                       f'Ao alterar, todos os volumes cadastrados serão removidos.')
                if self.pergunta_confirmacao(msg):
                    self.dados_de_volumes = {}

                    self.spin_Volume.setValue(0)
                    self.line_Peso_Bruto.setText(f"{0}")
                    self.line_Peso_Liquido.setText(f"{0}")

                    dados = (self.dados_de_volumes, responsavel)
                    self.abrir_tela_embalagem(dados)
            else:
                dados = (self.dados_de_volumes, responsavel)
                self.abrir_tela_embalagem(dados)

    def abrir_tela_embalagem(self, dados):
        from menu_vendas.exp_embalagem import TelaExpedicaoEmbalagem

        self.tela_embalagem = TelaExpedicaoEmbalagem(dados)
        self.tela_embalagem.volumes.connect(self.atualizar_dados_volumes)
        self.tela_embalagem.show()

    def atualizar_dados_volumes(self, dados):
        self.dados_de_volumes = dados["volumes"]
        self.responsavel_volumes = dados["responsavel"]

        self.somar_volumes()

    def somar_volumes(self):
        try:
            peso_total_final = 0
            peso_liq_total = 0
            qtde_itens = len(self.dados_de_volumes)

            if self.dados_de_volumes and self.responsavel_volumes:
                if self.responsavel_volumes == "SUZUKI MÁQUINAS":
                    for i in self.dados_de_volumes:
                        num_vol, tipo, embalagem, peso_total, peso_liq = i

                        peso_total_valor = valores_para_float(peso_total)
                        peso_total_final += peso_total_valor

                        peso_liq_valor = valores_para_float(peso_liq)
                        peso_liq_total += peso_liq_valor

                elif self.responsavel_volumes == "LOGÍSTICA":
                    for i in self.dados_de_volumes:
                        num_vol, altura, largura, compr, tipo, embalagem, peso_total, peso_liq = i

                        peso_total_valor = valores_para_float(peso_total)
                        peso_total_final += peso_total_valor

                        peso_liq_valor = valores_para_float(peso_liq)
                        peso_liq_total += peso_liq_valor

                else:
                    for i in self.dados_de_volumes:
                        num_vol, tipo, embalagem, peso_total, peso_liq = i

                        peso_total_valor = valores_para_float(peso_total)
                        peso_total_final += peso_total_valor

                        peso_liq_valor = valores_para_float(peso_liq)
                        peso_liq_total += peso_liq_valor

            self.spin_Volume.setValue(qtde_itens)

            peso_liquido = round(peso_liq_total, 2)
            peso_bruto = round(peso_total_final, 2)

            self.line_Peso_Bruto.setText(f"{peso_bruto}")
            self.line_Peso_Liquido.setText(f"{peso_liquido}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_funcionario(self):
        try:
            tabela = []

            self.combo_Motorista_Maq.clear()
            tabela.append("")

            cur = conecta.cursor()
            cur.execute(f"SELECT id, funcionario FROM funcionarios "
                        f"where ativo = 'S' AND CPF IS NOT NULL  "
                        f"order by funcionario;")
            detalhes_func = cur.fetchall()

            for dadus in detalhes_func:
                ides, func = dadus
                tabela.append(f"{ides} - {func}")

            self.combo_Motorista_Maq.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_veiculo(self):
        try:
            tabela = []

            self.combo_Placa_Maq.clear()
            tabela.append("")

            cur = conecta.cursor()
            cur.execute(f"SELECT id, descricao, placa FROM PLACA_VEICULO order by descricao;")
            detalhes_func = cur.fetchall()

            for dadus in detalhes_func:
                ides, veiculo, placa = dadus
                tabela.append(f"{ides} - {veiculo} - {placa}")

            self.combo_Placa_Maq.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def selecionar_responsavel(self):
        try:
            responsavel = self.combo_Resp_Frete.currentText()

            if responsavel:
                if responsavel == "SUZUKI MÁQUINAS":
                    self.stacked_Responsavel.setCurrentWidget(self.page_Maquinas)
                elif responsavel == "LOGÍSTICA":
                    self.stacked_Responsavel.setCurrentWidget(self.page_Logistica)
                else:
                    self.stacked_Responsavel.setCurrentWidget(self.page_Terceiros)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            print("salvaMENTO")
            num_exp = self.line_Num_Exp.text()

            responsavel = self.combo_Resp_Frete.currentText()

            cliente = self.combo_Cliente_Vendas.currentText()

            dados_exp = extrair_tabela(self.table_Expedicao)

            cif_fob = self.combo_Frete.currentText()

            volume = self.spin_Volume.value()

            peso_liquido = self.line_Peso_Liquido.text()
            peso_bruto = self.line_Peso_Bruto.text()

            restricao = self.combo_Entrega.currentText()

            if not dados_exp:
                self.mensagem_alerta(f'A tabela "Expedição" está vazia!')
            elif not num_exp:
                self.mensagem_alerta(f'O campo "Nº EXP" não pode estar vazio!')
            elif not cliente:
                self.mensagem_alerta(f'O campo "Cliente" não pode estar vazio!')
            elif not responsavel:
                self.mensagem_alerta(f'O campo "Responsável Frete" não pode estar vazio!')
            elif not cif_fob:
                self.mensagem_alerta(f'O campo "Tipo Frete" não pode estar vazio!')
            elif not peso_bruto or peso_bruto <= "0":
                self.mensagem_alerta(f'O campo "Peso Bruto" não pode estar vazio!')
            elif not peso_liquido or peso_liquido <= "0":
                self.mensagem_alerta(f'O campo "Peso Líq." não pode estar vazio!')
            elif volume == 0 or not volume:
                self.mensagem_alerta(f'O campo "Volume" não pode estar vazio!')
            elif not self.dados_de_volumes:
                self.mensagem_alerta(f'Não foi registrado dados dos volumes!')
            elif not restricao:
                self.mensagem_alerta(f'O campo "PROGRAMAR ENTREGA" precisa ser preenchido!')
            else:
                if responsavel == "SUZUKI MÁQUINAS":
                    placa = self.combo_Placa_Maq.currentText()
                    motorista = self.combo_Motorista_Maq.currentText()
                elif responsavel == "LOGÍSTICA":
                    placa = "NÃO VAI"
                    motorista = "NÃO VAI"
                else:
                    placa = self.line_Placa_Ter.text()
                    motorista = self.line_Motorista_Ter.text()

                if not placa or not motorista:
                    self.mensagem_alerta(f'Preencha os dados do motorista.')
                else:
                    obs = self.line_Obs_Embalagem.text()
                    if not obs:
                        if restricao == "POSSUI RESTRIÇÃO":
                            self.mensagem_alerta(f'O campo "OBSERVAÇÃO" precisa ser preenchido com a restrição definida!')
                        else:
                            self.salvar_expedicao_venda()
                    else:
                        self.salvar_expedicao_venda()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_expedicao_venda(self):
        try:
            print("salvar")
            responsavel = self.combo_Resp_Frete.currentText()

            if responsavel == "SUZUKI MÁQUINAS":
                placa = self.combo_Placa_Maq.currentText()
                motorista = self.combo_Motorista_Maq.currentText()
            elif responsavel == "LOGÍSTICA":
                placa = None
                motorista = None
            else:
                placa = self.line_Placa_Ter.text()
                motorista = self.line_Motorista_Ter.text()

            tipo_operacao = self.combo_Operacao.currentText()

            cliente = self.combo_Cliente_Vendas.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]

            cif_fob = self.combo_Frete.currentText()
            cif_fobtete = cif_fob.find(" - ")
            cif_limpo = cif_fob[:cif_fobtete]

            volume = self.spin_Volume.value()

            peso_liquido = self.line_Peso_Liquido.text()
            peso_liquid_float = valores_para_float(peso_liquido)

            peso_bruto = self.line_Peso_Bruto.text()
            peso_bruto_float = valores_para_float(peso_bruto)

            obs = self.line_Obs_Embalagem.text()
            if not obs:
                obs = None

            datamov = self.date_Emissao.text()
            date_mov = datetime.strptime(datamov, '%d/%m/%Y').date()
            data_mov_certa = str(date_mov)

            cursor = conecta.cursor()
            cursor.execute("select GEN_ID(GEN_ORDEMEXPEDICAO_ID,0) from rdb$database;")
            ultimo_ped0 = cursor.fetchall()
            ultimo_ped1 = ultimo_ped0[0]
            ultimo_ped = int(ultimo_ped1[0]) + 1

            cursor = conecta.cursor()
            cursor.execute(f"Insert into ORDEMEXPEDICAO (EMISSAO, ID_CLIENTE, TIPO_OPERACAO, "
                           f"RESPONSAVEL_FRETE, TIPO_FRETE, PESO_BRUTO, PESO_LIQUIDO, "
                           f"VOLUME, MOTORISTA, VEICULO, OBS_RESTRICAO, STATUS, NOME_PC) "
                           f"values ('{data_mov_certa}', "
                           f"'{id_cliente}', '{tipo_operacao}', '{responsavel}', '{cif_limpo}', '{peso_bruto_float}', "
                           f"'{peso_liquid_float}', {volume}, '{motorista}', '{placa}', '{obs}',  "
                           f"'A', '{self.nome_computador}');")

            dados_exp = extrair_tabela(self.table_Expedicao)
            for itens in dados_exp:
                cod_prod, descricao, ref, um, qtde, num = itens

                qtde_float = valores_para_float(qtde)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, codigo, embalagem FROM produto where codigo = '{cod_prod}';")
                dados_produto = cursor.fetchall()
                id_produto, codigo, embalagem = dados_produto[0]

                numtete = num.find(" ")
                tipo_venda = num[:numtete]
                num_venda = num[numtete + 1:]

                cursor.execute(
                    """
                    INSERT INTO PRODUTOORDEMEXPEDICAO
                    (ID_PRODUTO, ID_ORDEM_EXPEDICAO, QTDE, UNITARIO, TIPO_ORIGEM, ID_ORIGEM)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (id_produto, ultimo_ped, qtde_float, None, tipo_venda, num_venda)
                )

                if tipo_venda == "PI":
                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE produtopedidointerno SET STATUS = 'B' "
                                   f"WHERE id_produto = {id_produto} "
                                   f"and id_pedidointerno = {num_venda};")

                if tipo_venda == "OV":
                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE PRODUTOORDEMCOMPRA SET PRODUZIDO = '{qtde_float}' "
                                   f"WHERE PRODUTO = {id_produto} "
                                   f"and MESTRE = {num_venda};")

                cur = conecta.cursor()
                cur.execute(f"SELECT funcionario_id, descricao, nome_usuario FROM ENVIA_PC "
                            f"where descricao = '{self.nome_computador}' "
                            f"and nome_usuario = '{self.username}';")
                dados_usuario = cur.fetchall()

                if dados_usuario:
                    id_func = dados_usuario[0][0]
                else:
                    id_func = 11

                cursor = conecta.cursor()
                cursor.execute(f"Insert into MOVIMENTACAO (ID, PRODUTO, OBS, TIPO, QUANTIDADE, "
                               f"DATA, CODIGO, FUNCIONARIO, LOCALESTOQUE) values "
                               f"(GEN_ID(GEN_MOVIMENTACAO_ID,1), {id_produto}, 'EXP {ultimo_ped}', '230', "
                               f"{qtde_float}, '{data_mov_certa}', {cod_prod}, {id_func}, 20);")


            if self.responsavel_volumes == "SUZUKI MÁQUINAS":
                for i in self.dados_de_volumes:
                    num_vol, tipo, embalagem, peso_total, peso_liq = i

                    peso_total_float = valores_para_float(peso_total)
                    peso_liq_float = valores_para_float(peso_liq)

                    cursor = conecta.cursor()
                    cursor.execute(f"Insert into VOLUMEORDEMEXPEDICAO (NUM_VOLUME, EMBALAGEM, "
                                   f"PESO_BRUTO, PESO_LIQUIDO) "
                                   f"values ({int(num_vol)}, '{embalagem}', "
                                   f"'{peso_total_float}', '{peso_liq_float}');")

            elif self.responsavel_volumes == "LOGÍSTICA":
                for i in self.dados_de_volumes:
                    num_vol, altura, largura, compr, tipo, embalagem, peso_total, peso_liq = i

                    peso_total_float = valores_para_float(peso_total)
                    peso_liq_float = valores_para_float(peso_liq)

                    altura_float = valores_para_float(altura)
                    largura_float = valores_para_float(largura)
                    compr_float = valores_para_float(compr)

                    cursor = conecta.cursor()
                    cursor.execute(f"Insert into VOLUMEORDEMEXPEDICAO (NUM_VOLUME, EMBALAGEM, "
                                   f"PESO_BRUTO, PESO_LIQUIDO, ALTURA, LARGURA, COMPRIMENTO) "
                                   f"values ({int(num_vol)}, '{embalagem}', "
                                   f"'{peso_total_float}', '{peso_liq_float}', "
                                   f"{altura_float}, {largura_float}, {compr_float});")
            else:
                for i in self.dados_de_volumes:
                    num_vol, tipo, embalagem, peso_total, peso_liq = i

                    peso_total_float = valores_para_float(peso_total)
                    peso_liq_float = valores_para_float(peso_liq)

                    cursor = conecta.cursor()
                    cursor.execute(f"Insert into VOLUMEORDEMEXPEDICAO (NUM_VOLUME, EMBALAGEM, "
                                   f"PESO_BRUTO, PESO_LIQUIDO) "
                                   f"values ({int(num_vol)}, '{embalagem}', "
                                   f"'{peso_total_float}', '{peso_liq_float}');")

            conecta.commit()

            self.mensagem_alerta("Ordem de Expedição salva com sucesso!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaExpedicaoV2()
    tela.show()
    qt.exec_()