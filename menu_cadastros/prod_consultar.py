import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import lanca_tabela, layout_cabec_tab, limpa_tabela, extrair_tabela
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget_cab
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_conversoes import valores_para_virgula, valores_para_float
from comandos.comando_excel import edita_alinhamento, edita_bordas, linhas_colunas_p_edicao
from comandos.comando_excel import criar_workbook, edita_fonte, edita_preenchimento, letra_coluna
from forms.tela_prod_consultar import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os
from pathlib import Path
from PyQt5.QtCore import pyqtSignal


class TelaProdutoConsulta(QMainWindow, Ui_MainWindow):
    produto_escolhido = pyqtSignal(str)

    def __init__(self, produto, outra_tela, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.produto = produto
        self.outra_tela = outra_tela

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Resultado)
        cor_widget_cab(self.widget_cabecalho)

        self.table_Resultado.viewport().installEventFilter(self)

        self.btn_Buscar.clicked.connect(self.procura_produtos)
        self.btn_Excel.clicked.connect(self.gerar_excel)

        self.processando = False

    def eventFilter(self, source, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_Resultado.viewport()):

                if self.outra_tela:
                    item = self.table_Resultado.currentItem()
                    extrai_total = extrair_tabela(self.table_Resultado)
                    item_selecionado = extrai_total[item.row()]

                    cod_definido = item_selecionado[0]

                    self.produto_escolhido.emit(cod_definido)
                    self.close()

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def procura_produtos(self):
        try:
            localizacao = self.line_Local.text()
            if localizacao:
                self.localizacao_com_estoque(localizacao)
            else:
                descricao1 = self.line_Descricao1.text().upper()
                descricao2 = self.line_Descricao2.text().upper()
                descricao3 = self.line_Descricao3.text().upper()

                estoque = self.check_Estoque_Busca.isChecked()
                movimentacao = self.check_Mov_Busca.isChecked()

                if estoque and movimentacao:
                    if descricao1 and descricao2 and descricao3:
                        self.estoque_movimentacao_pal1_pal2_pal3(descricao1, descricao2, descricao3)
                    elif descricao1 and descricao2:
                        self.estoque_movimentacao_pal1_pal2(descricao1, descricao2)
                    elif descricao1 and descricao3:
                        self.estoque_movimentacao_pal1_pal3(descricao1, descricao3)
                    elif descricao2 and descricao3:
                        self.estoque_movimentacao_pal2_pal3(descricao2, descricao3)
                    elif descricao1:
                        self.estoque_movimentacao_pal1(descricao1)
                    elif descricao2:
                        self.estoque_movimentacao_pal2(descricao2)
                    elif descricao3:
                        self.estoque_movimentacao_pal3(descricao3)
                    else:
                        self.estoque_movimentacao()
                elif estoque:
                    if descricao1 and descricao2 and descricao3:
                        self.estoque_pal1_pal2_pal3(descricao1, descricao2, descricao3)
                    elif descricao1 and descricao2:
                        self.estoque_pal1_pal2(descricao1, descricao2)
                    elif descricao1 and descricao3:
                        self.estoque_pal1_pal3(descricao1, descricao3)
                    elif descricao2 and descricao3:
                        self.estoque_pal2_pal3(descricao2, descricao3)
                    elif descricao1:
                        self.estoque_pal1(descricao1)
                    elif descricao2:
                        self.estoque_pal2(descricao2)
                    elif descricao3:
                        self.estoque_pal3(descricao3)
                    else:
                        self.estoque()
                elif movimentacao:
                    if descricao1 and descricao2 and descricao3:
                        self.movimentacao_pal1_pal2_pal3(descricao1, descricao2, descricao3)
                    elif descricao1 and descricao2:
                        self.movimentacao_pal1_pal2(descricao1, descricao2)
                    elif descricao1 and descricao3:
                        self.movimentacao_pal1_pal3(descricao1, descricao3)
                    elif descricao2 and descricao3:
                        self.movimentacao_pal2_pal3(descricao2, descricao3)
                    elif descricao1:
                        self.movimentacao_pal1(descricao1)
                    elif descricao2:
                        self.movimentacao_pal2(descricao2)
                    elif descricao3:
                        self.movimentacao_pal3(descricao3)
                    else:
                        self.movimentacao()
                else:
                    if descricao1 and descricao2 and descricao3:
                        self.pal1_pal2_pal3(descricao1, descricao2, descricao3)
                    elif descricao1 and descricao2:
                        self.pal1_pal2(descricao1, descricao2)
                    elif descricao1 and descricao3:
                        self.pal1_pal3(descricao1, descricao3)
                    elif descricao2 and descricao3:
                        self.pal2_pal3(descricao2, descricao3)
                    elif descricao1:
                        self.pal1(descricao1)
                    elif descricao2:
                        self.pal2(descricao2)
                    elif descricao3:
                        self.pal3(descricao3)
                    else:
                        mensagem_alerta("Defina algum parâmetro para seguir com a consulta!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def localizacao_com_estoque(self, localizacao):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE prod.localizacao LIKE '%{localizacao}%' "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque(self):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT codigo, descricao, COALESCE(descricaocomplementar, ''), COALESCE(obs, ''), "
                           f"unidade, COALESCE(quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto "
                           f"WHERE quantidade > 0 "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao(self):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"order by prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao(self):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE prod.quantidade > 0 "
                           f"order by prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal1_pal2_pal3(self, descricao1, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal1_pal2(self, descricao1, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal1_pal3(self, descricao1, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal2_pal3(self, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal1(self, descricao1):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal2(self, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_movimentacao_pal3(self, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal1_pal2_pal3(self, descricao1, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal1_pal2(self, descricao1, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal1_pal3(self, descricao1, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal2_pal3(self, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal1(self, descricao1):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal2(self, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def estoque_pal3(self, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"AND prod.quantidade > 0 "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal1_pal2_pal3(self, descricao1, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal1_pal2(self, descricao1, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal1_pal3(self, descricao1, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal2_pal3(self, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"AND (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal1(self, descricao1):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao1}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"prod.obs LIKE '%{descricao1}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal2(self, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao2}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"prod.obs LIKE '%{descricao2}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def movimentacao_pal3(self, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DISTINCT prod.codigo, prod.descricao, "
                           f"COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"INNER JOIN movimentacao as mov ON prod.id = mov.produto "
                           f"WHERE (prod.descricao LIKE '%{descricao3}%' OR "
                           f"prod.descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"prod.obs LIKE '%{descricao3}%') "
                           f"ORDER BY prod.descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal1_pal2_pal3(self, descricao1, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao1}%' OR "
                           f"descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"obs LIKE '%{descricao1}%') "
                           f"AND (descricao LIKE '%{descricao2}%' OR "
                           f"descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"obs LIKE '%{descricao2}%') "
                           f"AND (descricao LIKE '%{descricao3}%' OR "
                           f"descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"obs LIKE '%{descricao3}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal1_pal2(self, descricao1, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao1}%' OR "
                           f"descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"obs LIKE '%{descricao1}%') "
                           f"AND (descricao LIKE '%{descricao2}%' OR "
                           f"descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"obs LIKE '%{descricao2}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal1_pal3(self, descricao1, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao1}%' OR "
                           f"descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"obs LIKE '%{descricao1}%') "
                           f"AND (descricao LIKE '%{descricao3}%' OR "
                           f"descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"obs LIKE '%{descricao3}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal2_pal3(self, descricao2, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao2}%' OR "
                           f"descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"obs LIKE '%{descricao2}%') "
                           f"AND (descricao LIKE '%{descricao3}%' OR "
                           f"descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"obs LIKE '%{descricao3}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal1(self, descricao1):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao1}%' OR "
                           f"descricaocomplementar LIKE '%{descricao1}%' OR "
                           f"obs LIKE '%{descricao1}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal2(self, descricao2):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao2}%' OR "
                           f"descricaocomplementar LIKE '%{descricao2}%' OR "
                           f"obs LIKE '%{descricao2}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def pal3(self, descricao3):
        try:
            limpa_tabela(self.table_Resultado)

            tabela = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.descricaocomplementar, ''), "
                           f"COALESCE(prod.obs, ''), "
                           f"prod.unidade, COALESCE(prod.quantidade, ''), "
                           f"COALESCE(prod.localizacao, ''), COALESCE(prod.ncm, '') "
                           f"FROM produto as prod "
                           f"WHERE (descricao LIKE '%{descricao3}%' OR "
                           f"descricaocomplementar LIKE '%{descricao3}%' OR "
                           f"obs LIKE '%{descricao3}%') "
                           f"order by descricao;")
            detalhes_produto = cursor.fetchall()
            if detalhes_produto:
                for tudo in detalhes_produto:
                    cod, descr, compl, ref, um, saldo, local, ncm = tudo

                    saldo = valores_para_float(saldo)
                    saldo_formatado = "{:.{}f}".format(saldo, len(str(saldo).split('.')[-1]))
                    saldinho = valores_para_virgula(saldo_formatado)

                    dados = (cod, descr, compl, ref, um, saldinho, local, ncm)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Resultado, tabela)
            else:
                mensagem_alerta("Não foi encontrado nenhum registro com essas condições!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def gerar_excel(self):
        try:
            extrai_dados_tabela = extrair_tabela(self.table_Resultado)
            if extrai_dados_tabela:
                workbook = criar_workbook()
                sheet = workbook.active
                sheet.title = "Estoque Final"

                headers = ["Código", "Descrição", "Descrição Compl.", "Referência", "UM", "Saldo", "Local", "NCM"]
                sheet.append(headers)

                header_row = sheet[1]
                for cell in header_row:
                    edita_fonte(cell, negrito=True)
                    edita_preenchimento(cell)
                    edita_alinhamento(cell)

                for dados_ex in extrai_dados_tabela:
                    codigo, descr, compl, ref, um, saldo, local, ncm = dados_ex
                    codigu = int(codigo)

                    sheet.append([codigu, descr, compl, ref, um, saldo, local, ncm])

                for cell in linhas_colunas_p_edicao(sheet, 1, sheet.max_row, 1, sheet.max_column):
                    edita_bordas(cell)
                    edita_alinhamento(cell)

                for column in sheet.columns:
                    max_length = 0
                    column_letter = letra_coluna(column[0].column)
                    for cell in column:
                        if isinstance(cell.value, (int, float)):
                            cell_value_str = "{:.3f}".format(cell.value)
                        else:
                            cell_value_str = str(cell.value)
                        if len(cell_value_str) > max_length:
                            max_length = len(cell_value_str)

                    adjusted_width = (max_length + 2)
                    sheet.column_dimensions[column_letter].width = adjusted_width

                for cell in linhas_colunas_p_edicao(sheet, 2, sheet.max_row, 7, 9):
                    cell.number_format = '0.000'

                desktop = Path.home() / "Desktop"
                desk_str = str(desktop)
                nome_req = f'\Lista de Produtos.xlsx'
                caminho = (desk_str + nome_req)

                workbook.save(caminho)

                self.label_Excel.setText(f'Excel criado com sucesso!!')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaProdutoConsulta("", False)
    tela.show()
    qt.exec_()
