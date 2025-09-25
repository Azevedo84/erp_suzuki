import sys
from banco_dados.conexao import conecta
from forms.tela_pi_rastreio import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import layout_cabec_tab, lanca_tabela, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from comandos.lines import validador_inteiro
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import date
import inspect
import os
import traceback

from menu_cadastros.tela_projeto import TelaProjeto


class TelaPiRastreio(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Compras)
        layout_cabec_tab(self.table_OP)

        self.definir_line_bloqueados()
        self.definir_emissao()

        self.escolher_produto = []

        validador_inteiro(self.line_Num_Ped, 123456789)
        self.line_Num_Ped.setFocus()

        self.line_Num_Ped.returnPressed.connect(self.verifica_line_num_pi)

        self.combo_Produto.activated.connect(self.lanca_dados_tabelas)

        self.table_OP.viewport().installEventFilter(self)

        self.processando = False

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

    def definir_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_line_bloqueados(self):
        try:
            self.date_Emissao.setReadOnly(True)
            self.line_Cliente.setReadOnly(True)
            self.line_Solicitante.setReadOnly(True)
            self.line_Req_Cliente.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_line_num_pi(self):
        if not self.processando:
            try:
                self.processando = True

                num_ped = self.line_Num_Ped.text()
                if num_ped:
                    if int(num_ped) == 0:
                        self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                        self.line_Num_Ped.clear()
                    else:
                        self.verifica_sql_pi()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def verifica_sql_pi(self):
        try:
            num_ped = self.line_Num_Ped.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT * FROM pedidointerno where id = {num_ped};")
            detalhes = cursor.fetchall()
            if not detalhes:
                self.mensagem_alerta('Este número de pedido não existe!')
                self.line_Num_Ped.clear()
            else:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                               f"COALESCE(prod.obs, ''), prodint.qtde "
                               f"FROM PRODUTOPEDIDOINTERNO as prodint "
                               f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                               f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                               f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                               f"where ped.id = {num_ped} and prodint.status = 'A';")
                dados_produtos = cursor.fetchall()
                if not dados_produtos:
                    self.mensagem_alerta("Este pedido está encerrado!")
                    self.line_Num_Ped.clear()
                else:
                    self.lanca_dados_pi()
                    self.lanca_combo_produtos()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_pi(self):
        try:
            num_ped = self.line_Num_Ped.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT pi.emissao, cli.razao, pi.solicitante, "
                           f"COALESCE(pi.num_req_cliente, '') as req, "
                           f"pi.nome_pc, pi.status, COALESCE(pi.obs, '') as obs "
                           f"FROM PEDIDOINTERNO as pi "
                           f"INNER JOIN clientes as cli ON pi.id_cliente = cli.id "
                           f"where pi.id = {num_ped};")
            dados_interno = cursor.fetchall()

            emissao, cliente, solicitante, num_req, pc, status, obs = dados_interno[0]

            self.date_Emissao.setDate(emissao)

            self.line_Req_Cliente.setText(num_req)
            self.line_Solicitante.setText(solicitante)
            self.line_Obs.setText(obs)
            self.line_Cliente.setText(cliente)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_produtos(self):
        try:
            tabela_nova = []

            self.combo_Produto.clear()

            num_ped = self.line_Num_Ped.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.obs, ''), prodint.qtde "
                           f"FROM PRODUTOPEDIDOINTERNO as prodint "
                           f"INNER JOIN produto as prod ON prodint.id_produto = prod.id "
                           f"INNER JOIN pedidointerno as ped ON prodint.id_pedidointerno = ped.id "
                           f"INNER JOIN clientes as cli ON ped.id_cliente = cli.id "
                           f"where ped.id = {num_ped} and prodint.status = 'A';")
            dados_produtos = cursor.fetchall()
            if dados_produtos:
                qtde_de_itens = len(dados_produtos)

                if qtde_de_itens == 1:
                    for i in dados_produtos:
                        cod, descricao, ref, qtde = i

                        dados = f"{cod} - {descricao} - {ref} - {qtde}"

                        tabela_nova.append(dados)

                    self.combo_Produto.addItems(tabela_nova)
                    self.combo_Produto.activated.emit(0)
                else:
                    tabela_nova.append("")

                    for i in dados_produtos:
                        cod, descricao, ref, qtde = i

                        dados = f"{cod} - {descricao} - {ref} - {qtde}"

                        tabela_nova.append(dados)

                    self.combo_Produto.addItems(tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_tabelas(self):
        try:
            dados_tabela_op = []
            dados_tabela_compras = []

            self.table_OP.setRowCount(0)
            self.table_Compras.setRowCount(0)

            num_ped = self.line_Num_Ped.text()
            produto = self.combo_Produto.currentText()
            if num_ped and produto:
                produtotete = produto.find(" - ")
                cod_produto = produto[:produtotete]

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, codigo, embalagem FROM produto where codigo = '{cod_produto}';")
                dados_produto = cursor.fetchall()
                id_produto, codigo, embalagem = dados_produto[0]

                cursor = conecta.cursor()
                cursor.execute(f"SELECT vinc.ID_PEDIDOINTERNO, vinc.tipo, vinc.numero, prod.codigo "
                               f"from VINCULO_PRODUTO_PI as vinc "
                               f"INNER JOIN produto as prod ON vinc.id_produto = prod.id "
                               f"where ID_PEDIDOINTERNO = {num_ped} "
                               f"and ID_PRODUTO_PI = {id_produto};")
                dados_interno = cursor.fetchall()
                if dados_interno:
                    for i in dados_interno:
                        num_pi, tipo, num_op_oc_req, cod_prod_oc_req = i

                        if tipo == "OP":
                            dados = self.manipula_dados_tabela_producao(cod_prod_oc_req, num_op_oc_req)
                            if dados:
                                for inin in dados:
                                    dados_tabela_op.append(inin)

                        if tipo == "OC":
                            dados = self.manipula_dados_tabela_oc(cod_prod_oc_req, num_op_oc_req)
                            if dados:
                                dados_tabela_compras.append(dados)

                        if tipo == "SOL":
                            dados = self.manipula_dados_tabela_sol(cod_prod_oc_req, num_op_oc_req)
                            if dados:
                                dados_tabela_compras.append(dados)

                        if tipo == "REQ":
                            dados = self.manipula_dados_tabela_req(cod_prod_oc_req, num_op_oc_req)
                            if dados:
                                dados_tabela_compras.append(dados)


                if dados_tabela_op:
                    ordem = {'CONJUNTO': 0, 'INDUSTRIALIZACAO': 1, 'USINAGEM': 2}

                    dados_ordenados = sorted(dados_tabela_op, key=lambda x: ordem[x[-1]])
                    lanca_tabela(self.table_OP, dados_ordenados)
                if dados_tabela_compras:
                    lanca_tabela(self.table_Compras, dados_tabela_compras)


        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela_producao(self, cod_prod, num_op):
        try:
            dados_finais = []
            adiciona_industrializados = []

            cursor = conecta.cursor()
            cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, prod.codigo, "
                           f"prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"ordser.quantidade, ordser.id_estrutura, COALESCE(tip.tipomaterial, '') "
                           f"from ordemservico as ordser "
                           f"INNER JOIN produto prod ON ordser.produto = prod.id "
                           f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                           f"where ordser.status = 'A' "
                           f"and prod.codigo = {cod_prod} "
                           f"and ordser.numero = {num_op} "
                           f"order by ordser.numero;")
            op_abertas = cursor.fetchall()
            if op_abertas:
                emissao, previsao, op, cod, descr, ref, um, qtde, id_estrut, tipo = op_abertas[0]

                if id_estrut:

                    total_estrut = 0
                    total_consumo = 0

                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT estprod.id, "
                                   f"((SELECT quantidade FROM ordemservico where numero = {op}) * "
                                   f"(estprod.quantidade)) AS Qtde, prod.tipomaterial, prod.codigo "
                                   f"FROM estrutura_produto as estprod "
                                   f"INNER JOIN produto prod ON estprod.id_prod_filho = prod.id "
                                   f"where estprod.id_estrutura = {id_estrut};")
                    itens_estrutura = cursor.fetchall()

                    for dads in itens_estrutura:
                        ides, quantidade, tipo_filho, cod_filho = dads
                        total_estrut += 1

                        consumo_op_ind = 0

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT max(prodser.ID_ESTRUT_PROD), "
                                       f"sum(prodser.QTDE_ESTRUT_PROD) as total "
                                       f"FROM estrutura_produto as estprod "
                                       f"INNER JOIN produto prod ON estprod.id_prod_filho = prod.id "
                                       f"INNER JOIN produtoos as prodser ON estprod.id = prodser.ID_ESTRUT_PROD "
                                       f"where prodser.numero = {op} and estprod.id = {ides} "
                                       f"group by prodser.ID_ESTRUT_PROD;")
                        itens_consumo = cursor.fetchall()
                        for duds in itens_consumo:
                            id_mats, qtde_mats = duds

                            if ides == id_mats and quantidade == qtde_mats:
                                total_consumo += 1
                                consumo_op_ind += qtde_mats

                        if tipo_filho == 119 and quantidade != consumo_op_ind:
                            pipis = (cod_filho, tipo_filho)
                            adiciona_industrializados.append(pipis)
                    if tipo == "CONJUNTO":
                        if total_estrut != total_consumo:
                            dados = (num_op, cod, descr, ref, um, qtde, tipo)
                            dados_finais.append(dados)
                    else:
                        dados = (num_op, cod, descr, ref, um, qtde, tipo)
                        dados_finais.append(dados)

                if adiciona_industrializados:
                    for titi in adiciona_industrializados:
                        codis, tipis = titi

                        cursor = conecta.cursor()
                        cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, ''), "
                                       f"COALESCE(tip.tipomaterial, '') "
                                       f"FROM produto as prod "
                                       f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                                       f"where prod.codigo = '{codis}';")
                        dados_produto = cursor.fetchall()
                        codigo, descricao, referencia, tipu = dados_produto[0]

                        dados = ("IND", codigo, descricao, referencia, um,  0, tipu)
                        dados_finais.append(dados)

                if dados_finais:
                    return dados_finais


        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela_oc(self, cod_prod, num_oc):
        try:
            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, forn.razao, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade,"
                f"prodoc.quantidade, COALESCE(tip.tipomaterial, '') "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"LEFT JOIN produtoordemrequisicao as prodreq ON prodoc.id_prod_req = prodreq.id "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                f"INNER JOIN fornecedores as forn ON oc.fornecedor = forn.id "
                f"LEFT JOIN produtoordemsolicitacao as prodsol ON prodreq.id_prod_sol = prodsol.id "
                f"LEFT JOIN ordemsolicitacao as sol ON prodsol.mestre = sol.idsolicitacao "
                f"where oc.entradasaida = 'E' "
                f"AND oc.STATUS = 'A' "
                f"AND prodoc.produzido < prodoc.quantidade "
                f"and prod.codigo = {cod_prod} and oc.numero = {num_oc} "
                f"ORDER BY oc.numero;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                num_oc, forncec_oc, descr, ref, um, qtde_oc, tipo = dados_oc[0]

                dados = (f"OC {num_oc}", cod_prod, descr, um, qtde_oc, forncec_oc)

                return dados

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela_sol(self, cod_prod, num_sol):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT prodreq.mestre, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"COALESCE(tip.tipomaterial, ''), prodreq.quantidade "
                           f"FROM produtoordemsolicitacao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                           f"INNER JOIN ordemsolicitacao as req ON prodreq.mestre = req.idsolicitacao "
                           f"LEFT JOIN produtoordemrequisicao as preq ON prodreq.id = preq.id_prod_sol "
                           f"WHERE prodreq.status = 'A' "
                           f"and prod.codigo = {cod_prod} "
                           f"and prodreq.mestre = {num_sol} "
                           f"AND preq.id_prod_sol IS NULL "
                           f"ORDER BY prodreq.mestre;")
            dados_sol = cursor.fetchall()

            if dados_sol:
                num_oc, descr, ref, um, tipo, qtde_sol = dados_sol[0]

                dados = (f"SOL {num_oc}", cod_prod, descr, um, qtde_sol, "")

                return dados

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela_req(self, cod_prod, num_req):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT prodreq.numero, prodreq.quantidade, prod.descricao, "
                           f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                           f"COALESCE(tip.tipomaterial, '') "
                           f"FROM produtoordemrequisicao as prodreq "
                           f"INNER JOIN produto as prod ON prodreq.produto = prod.ID "
                           f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                           f"INNER JOIN ordemrequisicao as req ON prodreq.mestre = req.id "
                           f"LEFT JOIN produtoordemsolicitacao as prodsol ON prodreq.id_prod_sol = prodsol.id "
                           f"LEFT JOIN ordemsolicitacao as sol ON prodsol.mestre = sol.idsolicitacao "
                           f"where prodreq.status = 'A' "
                           f"and prodreq.numero = {num_req} "
                           f"and prod.codigo = {cod_prod};")
            dados_req = cursor.fetchall()

            if dados_req:
                num_req, qtde, descr, ref, um, tipo = dados_req[0]

                dados = (f"REQ {num_req}", cod_prod, descr, um, qtde, "")

                return dados

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, source, event):
        try:
            qtable_widget = self.table_OP

            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is qtable_widget.viewport()):

                item = qtable_widget.currentItem()

                extrai_recomendados = extrair_tabela(qtable_widget)
                item_selecionado = extrai_recomendados[item.row()]

                num_op, cod, desc, ref, um, qtde, tipo = item_selecionado

                import re

                s = re.sub(r"[^\d.]", "", ref)  # remove tudo que não é número ou ponto
                s = re.sub(r"\.+$", "", s)
                print(s)  # saída: 47.00.014.07

                caminho_pdf = rf"\\Publico\C\OP\Projetos\{s}.pdf"

                if os.path.exists(caminho_pdf):
                    self.abrir_tela_alteracao_prod(caminho_pdf)
                else:
                    self.mensagem_alerta("O desenho deste produto não foi encontrado!")


            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def abrir_tela_alteracao_prod(self, caminho):
        try:
            from menu_cadastros import tela_projeto

            self.escolher_produto = TelaProjeto(caminho)
            self.escolher_produto.show()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPiRastreio()
    tela.show()
    qt.exec_()
