import sys
from banco_dados.conexao import conecta
from forms.tela_prod_vendas import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela, layout_cabec_tab, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from comandos.cores import cor_cinza_claro
from comandos.conversores import valores_para_float, float_para_moeda_reais, float_para_porcentagem
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QColor
import inspect
import os
import traceback
from threading import Thread


class TelaProdutoVendas(QMainWindow, Ui_MainWindow):
    def __init__(self, produto, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        if produto:
            self.verifica_codigo(produto)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)

        layout_cabec_tab(self.table_Vendas)

        self.definir_line_bloqueados()

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

    def definir_line_bloqueados(self):
        try:
            self.line_Codigo.setReadOnly(True)
            self.line_Descricao.setReadOnly(True)
            self.line_DescrCompl.setReadOnly(True)
            self.line_Referencia.setReadOnly(True)
            self.line_UM.setReadOnly(True)
            self.line_Conjunto.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_codigo(self, codigo_produto):
        try:
            cur = conecta.cursor()
            cur.execute(f"SELECT prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                        f"COALESCE(prod.obs, ''), prod.unidade, COALESCE(prod.localizacao, ''), conj.conjunto, "
                        f"prod.quantidade "
                        f"FROM produto as prod "
                        f"LEFT JOIN conjuntos conj ON prod.conjunto = conj.id "
                        f"where prod.codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()
            if detalhes_produto:
                descr, compl, ref, um, local, conjunto, saldo = detalhes_produto[0]

                self.line_Codigo.setText(codigo_produto)
                self.line_Descricao.setText(descr)
                self.line_DescrCompl.setText(compl)
                self.line_Referencia.setText(ref)
                self.line_UM.setText(um)
                self.line_Conjunto.setText(conjunto)
                self.line_Saldo.setText(str(saldo))

                Thread(target=self.oc_total_por_produto(codigo_produto)).start()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def oc_total_por_produto(self, cod_prod):
        try:
            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT oc.id, COALESCE(prodoc.id_pedido, ''), oc.data, oc.numero, cli.registro, "
                           f"cli.razao, prodoc.quantidade, prodoc.unitario, prodoc.ipi, "
                           f"prodoc.produzido, prodoc.dataentrega "
                           f"FROM PRODUTOORDEMCOMPRA as prodoc "
                           f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                           f"INNER JOIN ordemcompra as oc ON prodoc.mestre = oc.id "
                           f"INNER JOIN clientes as cli ON oc.cliente = cli.id "
                           f"LEFT JOIN pedidointerno as ped ON prodoc.id_pedido = ped.id "
                           f"where prodoc.quantidade = prodoc.produzido "
                           f"and oc.entradasaida = 'S' "
                           f"and prod.codigo = {cod_prod};")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    id_oc, id_ped, data, oc, num_c, cliente, qtde, unit, ipi, produ, entr_dt = i

                    n_c = num_c.strip()
                    clie = cliente.strip()

                    qtde_float = valores_para_float(qtde)
                    produ_float = valores_para_float(produ)
                    unit_float = valores_para_float(unit)

                    ipi_float = valores_para_float(ipi)
                    ipi_porc = float_para_porcentagem(ipi_float)

                    valor_total = qtde_float * unit_float

                    unit_rs = float_para_moeda_reais(unit_float)
                    tot_rs = float_para_moeda_reais(valor_total)

                    emissao = data.strftime("%d/%m/%Y")

                    if entr_dt:
                        entr = entr_dt.strftime("%d/%m/%Y")
                    else:
                        entr = ""

                    cursor = conecta.cursor()
                    cursor.execute(
                        f"SELECT id, numero, quantidade "
                        f"FROM SAIDAPROD "
                        f"where ordemcompra = {id_oc} and codigo = '{cod_prod}';")
                    dados_nfs = cursor.fetchall()

                    if qtde_float != produ_float and produ_float > 0:
                        if dados_nfs:
                            for iii in dados_nfs:
                                id_entrada, nota_ent, qtde_ent = iii

                                qtde_ent_float = valores_para_float(qtde_ent)
                                valor_ent = qtde_ent_float * unit_float
                                rs_ent = float_para_moeda_reais(valor_ent)

                                dados = (entr, nota_ent, oc, qtde_ent_float, unit_rs, ipi_porc, rs_ent,
                                         emissao, n_c, clie, id_ped)
                                tabela.append(dados)

                            qtde_fif = qtde_float - produ_float

                            valor_dif = qtde_float * unit_float
                            rs_dif = float_para_moeda_reais(valor_dif)

                            dados = (entr, "", oc, qtde_fif, unit_rs, ipi_porc, rs_dif,
                                     emissao, n_c, clie, id_ped)
                            tabela.append(dados)
                    else:
                        if dados_nfs:
                            nf = dados_nfs[0][1]

                            dados = (entr, nf, oc, qtde_float, unit_rs, ipi_porc, tot_rs, emissao, n_c, clie, id_ped)
                            tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Vendas, tabela)

                self.table_Vendas.scrollToBottom()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaProdutoVendas("")
    tela.show()
    qt.exec_()
