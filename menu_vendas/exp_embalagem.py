import sys
from banco_dados.conexao import conecta
from forms.tela_exp_incluir_v3 import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela_v2, extrair_tabela
from comandos.telas import icone, cor_fundo_tela
from comandos.conversores import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
import inspect
import os
import socket
import traceback


class TelaExpedicaoEmbalagem(QMainWindow, Ui_MainWindow):
    volumes = pyqtSignal(object)
    def __init__(self, dados, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.nome_computador = socket.gethostname()

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")

        self.btn_Add_Vol_Log.clicked.connect(self.adicionar_volume)
        self.btn_Add_Vol_Maq.clicked.connect(self.adicionar_volume)
        self.btn_Add_Vol_Ter.clicked.connect(self.adicionar_volume)

        self.btn_Excluir_Vol_Log.clicked.connect(self.excluir_volume)
        self.btn_Excluir_Vol_Maq.clicked.connect(self.excluir_volume)
        self.btn_Excluir_Vol_Ter.clicked.connect(self.excluir_volume)

        self.btn_Salvar.clicked.connect(self.carregar_volumes)

        #dados = ([['21882', 'CONJUNTO MESA ROLO TR 800', 'D 43.00.080.01', 'UN', '2.0', 'PI 434']], 'SUZUKI MÁQUINAS', 'CIF - NOSSO')

        if dados:
            dados_volume, responsavel = dados

            self.responsavel = responsavel

            self.selecionar_responsavel_lanca_volumes(dados_volume)

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

    def carregar_volumes(self):
        try:
            if self.responsavel:
                if self.responsavel == "SUZUKI MÁQUINAS":
                    nome_tabela = self.table_Volume_Maq

                elif self.responsavel == "LOGÍSTICA":
                    nome_tabela = self.table_Volume_Log
                else:
                    nome_tabela = self.table_Volume_Ter

                dados_tabela = extrair_tabela(nome_tabela)

                dados = {
                    "responsavel": self.responsavel,
                    "volumes": dados_tabela
                }

                self.volumes.emit(dados)
                self.close()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def adicionar_volume(self):
        try:
            tem_tudo = False

            if self.responsavel:
                if self.responsavel == "SUZUKI MÁQUINAS":
                    nome_tabela = self.table_Volume_Maq
                    combo_tipo = self.combo_Tipo_Emb_Maq.currentText()
                    peso_embalagem = self.line_Peso_Emb_Maq.text()
                    peso_total = self.line_Peso_Total_Maq.text()

                    if peso_embalagem:
                        valor_peso_embalagem = round(valores_para_float(peso_embalagem), 2)
                    else:
                        valor_peso_embalagem = 0

                    if peso_total:
                        valor_peso_total = round(valores_para_float(peso_total), 2)
                    else:
                        valor_peso_total = 0

                    peso_liq = round((valor_peso_total - valor_peso_embalagem), 2)

                    dados_tabela = extrair_tabela(nome_tabela)
                    qtde_itens = len(dados_tabela) + 1

                    dados = (qtde_itens, combo_tipo, peso_embalagem, peso_total, peso_liq)

                    tem_tudo = True
                elif self.responsavel == "LOGÍSTICA":
                    nome_tabela = self.table_Volume_Log
                    combo_tipo = self.combo_Tipo_Emb_Log.currentText()
                    peso_embalagem = self.line_Peso_Emb_Log.text()
                    peso_total = self.line_Peso_Total_Log.text()

                    altura = self.line_Altura_Log.text()
                    largura = self.line_Largura_Log.text()
                    compr = self.line_Compr_Log.text()

                    if altura and largura and compr:
                        tem_tudo = True

                    if peso_embalagem:
                        valor_peso_embalagem = round(valores_para_float(peso_embalagem), 2)
                    else:
                        valor_peso_embalagem = 0

                    if peso_total:
                        valor_peso_total = round(valores_para_float(peso_total), 2)
                    else:
                        valor_peso_total = 0

                    if altura:
                        valor_altura = round(valores_para_float(altura), 2)
                    else:
                        valor_altura = 0

                    if largura:
                        valor_largura = round(valores_para_float(largura), 2)
                    else:
                        valor_largura = 0

                    if compr:
                        valor_compr = round(valores_para_float(compr), 2)
                    else:
                        valor_compr = 0

                    peso_liq = round((valor_peso_total - valor_peso_embalagem), 2)

                    dados_tabela = extrair_tabela(nome_tabela)
                    qtde_itens = len(dados_tabela) + 1

                    dados = (qtde_itens, valor_altura, valor_largura, valor_compr, combo_tipo, peso_embalagem, peso_total, peso_liq)
                else:
                    nome_tabela = self.table_Volume_Ter
                    combo_tipo = self.combo_Tipo_Emb_Ter.currentText()
                    peso_embalagem = self.line_Peso_Emb_Ter.text()
                    peso_total = self.line_Peso_Total_Ter.text()

                    if peso_embalagem:
                        valor_peso_embalagem = round(valores_para_float(peso_embalagem), 2)
                    else:
                        valor_peso_embalagem = 0

                    if peso_total:
                        valor_peso_total = round(valores_para_float(peso_total), 2)
                    else:
                        valor_peso_total = 0

                    peso_liq = round((valor_peso_total - valor_peso_embalagem), 2)

                    dados_tabela = extrair_tabela(nome_tabela)
                    qtde_itens = len(dados_tabela) + 1

                    dados = (qtde_itens, combo_tipo, peso_embalagem, peso_total, peso_liq)

                    tem_tudo = True

                if combo_tipo and peso_liq and peso_total:
                    if tem_tudo:
                        if valor_peso_total > 0 and peso_liq > 0 and valor_peso_embalagem >= 0:
                            if peso_liq > valor_peso_total:
                                self.mensagem_alerta("O Peso Líquido não pode ser maior que o Peso Total!")
                            else:
                                dados_tabela.append(dados)

                                lanca_tabela_v2(nome_tabela, dados_tabela)

                                self.somar_volumes()
                                self.limpar_campos_maq()
                        else:
                            self.mensagem_alerta("O Peso não pode ser igual ou menor que Zero!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_volume(self):
        try:
            if self.responsavel:
                if self.responsavel == "SUZUKI MÁQUINAS":
                    nome_tabela = self.table_Volume_Maq

                elif self.responsavel == "LOGÍSTICA":
                    nome_tabela = self.table_Volume_Log
                else:
                    nome_tabela = self.table_Volume_Ter

                dados_tab = extrair_tabela(nome_tabela)
                if not dados_tab:
                    self.mensagem_alerta(f'A tabela está vazia!')
                else:
                    linha = nome_tabela.currentRow()
                    if linha >= 0:
                        nome_tabela.removeRow(linha)

                self.somar_volumes()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpar_campos_maq(self):
        try:
            self.combo_Tipo_Emb_Maq.setCurrentText("")
            self.line_Peso_Total_Maq.clear()
            self.line_Peso_Emb_Maq.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def somar_volumes(self):
        try:
            peso_total_final = 0
            peso_liq_total = 0
            qtde_itens = 0

            if self.responsavel:
                if self.responsavel == "SUZUKI MÁQUINAS":
                    nome_tabela = self.table_Volume_Maq

                    dados_tabela = extrair_tabela(nome_tabela)
                    if dados_tabela:
                        for i in dados_tabela:
                            num_vol, tipo, embalagem, peso_total, peso_liq = i

                            peso_total_valor = valores_para_float(peso_total)
                            peso_total_final += peso_total_valor

                            peso_liq_valor = valores_para_float(peso_liq)
                            peso_liq_total += peso_liq_valor

                    qtde_itens = len(dados_tabela)

                elif self.responsavel == "LOGÍSTICA":
                    nome_tabela = self.table_Volume_Log

                    dados_tabela = extrair_tabela(nome_tabela)

                    if dados_tabela:
                        for i in dados_tabela:
                            num_vol, altura, largura, compr, tipo, embalagem, peso_total, peso_liq = i

                            peso_total_valor = valores_para_float(peso_total)
                            peso_total_final += peso_total_valor

                            peso_liq_valor = valores_para_float(peso_liq)
                            peso_liq_total += peso_liq_valor

                    qtde_itens = len(dados_tabela)

                else:
                    nome_tabela = self.table_Volume_Ter

                    dados_tabela = extrair_tabela(nome_tabela)

                    if dados_tabela:
                        for i in dados_tabela:
                            num_vol, tipo, embalagem, peso_total, peso_liq = i

                            peso_total_valor = valores_para_float(peso_total)
                            peso_total_final += peso_total_valor

                            peso_liq_valor = valores_para_float(peso_liq)
                            peso_liq_total += peso_liq_valor

                    qtde_itens = len(dados_tabela)

            self.spin_Volume.setValue(qtde_itens)

            peso_liquido = round(peso_liq_total, 2)
            peso_bruto = round(peso_total_final, 2)

            self.line_Peso_Bruto.setText(f"{peso_bruto}")
            self.line_Peso_Liquido.setText(f"{peso_liquido}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_embalagem(self, combo):
        try:
            tabela = []

            combo.clear()
            tabela.append("")

            dados = ["📦 CAIXA DE PAPELÃO",
                     "🪵 CAIXA DE MADEIRA",
                     "🪵 PALLET DE MADEIRA",
                     "🛍️ SACO",
                     "⚙️ SEM EMBALAGEM",
                     "➕ OUTROS"]

            for dadus in dados:
                tabela.append(dadus)

            combo.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def selecionar_responsavel_lanca_volumes(self, dados_volume):
        try:
            if self.responsavel:
                if self.responsavel == "SUZUKI MÁQUINAS":
                    self.stacked_Responsavel.setCurrentWidget(self.page_Maquinas)
                    self.definir_combo_embalagem(self.combo_Tipo_Emb_Maq)
                    nome_tabela = self.table_Volume_Maq
                elif self.responsavel == "LOGÍSTICA":
                    self.stacked_Responsavel.setCurrentWidget(self.page_Logistica)
                    self.definir_combo_embalagem(self.combo_Tipo_Emb_Log)
                    nome_tabela = self.table_Volume_Log
                else:
                    self.stacked_Responsavel.setCurrentWidget(self.page_Terceiros)
                    self.definir_combo_embalagem(self.combo_Tipo_Emb_Ter)
                    nome_tabela = self.table_Volume_Ter

                if dados_volume:
                    lanca_tabela_v2(nome_tabela, dados_volume)

                    self.somar_volumes()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaExpedicaoEmbalagem([])
    tela.show()
    qt.exec_()