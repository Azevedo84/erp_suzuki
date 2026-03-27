import sys
from banco_dados.conexao import conecta
from comandos.conversores import valores_para_float
from forms.tela_prod_vincular_fornecedor import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.cores import cor_amarelo, cor_vermelho, transparente
from comandos.tabelas import lanca_tabela_v2, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback

import socket
import getpass
import re

from PyQt5.QtCore import QTimer


class TelaVincularProdutoFornecedor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.processando = False

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        self.nome_computador = socket.gethostname()
        self.username = getpass.getuser()

        icone(self, "menu.png")
        tamanho_aplicacao(self)

        self.timer_busca = QTimer()
        self.timer_busca.setSingleShot(True)  # dispara uma vez só
        self.timer_busca.timeout.connect(self.buscar_produto)

        self.line_Filtro_Siger1.textChanged.connect(self.iniciar_timer_busca)

        self.escolher_produto = []
        self.btn_Lupa_Prod.clicked.connect(self.abrir_tela_escolher_produto)

        self.combo_Fornecedor.activated.connect(self.lanca_produtos_fornecedor)

        self.table_Prod_Forn.viewport().installEventFilter(self)
        self.table_Prod_Nosso.viewport().installEventFilter(self)

        self.btn_Vincular.clicked.connect(self.confere_vinculo_para_vincular)

        self.btn_Desvincular.clicked.connect(self.confere_vinculo_para_desvincular)

        self.btn_limpar.clicked.connect(self.limpa_tudo)

        self.radio_SemVinculo.setChecked(True)
        self.radio_SemVinculo.clicked.connect(self.definir_radios)
        self.radio_Todos.clicked.connect(self.definir_radios)

        self.definir_combo_fornecedor()

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

    def limpa_tudo(self):
        try:
            self.limpa_tabelas()
            self.limpa_filtros()
            self.limpa_campos_selecionados()

            self.radio_SemVinculo.setChecked(True)

            self.definir_combo_fornecedor()

            self.lanca_produtos_fornecedor()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_radios(self):
        try:
            self.definir_combo_fornecedor()

            self.lanca_produtos_fornecedor()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_campos_selecionados(self):
        try:
            self.line_cod_s.clear()
            self.line_descr_s.clear()
            self.line_um_s.clear()
            self.line_ncm_s.clear()
            self.line_fator_s.clear()

            self.line_cod_f.clear()
            self.line_descr_f.clear()
            self.line_um_f.clear()
            self.line_ncm_f.clear()
            self.line_fator_f.clear()

            self.remove_pintura_lines()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tabelas(self):
        try:
            self.table_Prod_Nosso.setRowCount(0)

            self.table_Prod_Forn.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_filtros(self):
        try:
            self.line_Filtro_F1.clear()
            self.line_Filtro_Siger1.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def reinicia_com_fornecedor_definido(self):
        try:
            self.limpa_tabelas()
            self.limpa_campos_selecionados()

            self.limpa_filtros()

            self.radio_SemVinculo.setChecked(True)

            self.definir_combo_fornecedor()

            self.lanca_produtos_fornecedor()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, sources, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and event.buttons() == QtCore.Qt.LeftButton
                    and sources is self.table_Prod_Forn.viewport()):
                item = self.table_Prod_Forn.currentItem()

                if item:
                    self.limpa_campos_selecionados()

                    dados_fornecedor = extrair_tabela(self.table_Prod_Forn)

                    item_selecionado_f = dados_fornecedor[item.row()]
                    cod_f, descr_f, um_f, ncm_f, codigo_siger, fator_s = item_selecionado_f

                    if codigo_siger == "-":
                        self.line_descr_s.setText("PRODUTO NÃO VINCULADO")
                        self.line_fator_f.setText("-")
                    else:
                        cur = conecta.cursor()
                        cur.execute("""
                                        SELECT codigo, descricao, COALESCE(obs, ''), unidade, COALESCE(ncm, '')
                                        FROM produto
                                        WHERE codigo = ?
                                        """, (codigo_siger,))
                        select_prod = cur.fetchall()
                        if select_prod:
                            cod_s, descr_s, ref_s, um_s, ncm_s = select_prod[0]

                            if ncm_s:
                                ncm_limpa = re.sub(r'\D', '', ncm_s)  # remove tudo que não for número
                            else:
                                ncm_limpa = ""

                            junta = f"{descr_s} - {ref_s}"

                            self.line_cod_s.setText(cod_s)
                            self.line_descr_s.setText(junta)
                            self.line_um_s.setText(um_s)
                            self.line_ncm_s.setText(ncm_limpa)

                            if fator_s == "-":
                                self.line_fator_s.setText("")
                            else:
                                self.line_fator_s.setText(fator_s)

                    self.line_cod_f.setText(cod_f)
                    self.line_descr_f.setText(descr_f)
                    self.line_um_f.setText(um_f)
                    self.line_ncm_f.setText(ncm_f)
                    self.line_fator_f.setText("1")

                    self.pintar_lines()

            elif (event.type() == QtCore.QEvent.MouseButtonDblClick and event.buttons() == QtCore.Qt.LeftButton
                  and sources is self.table_Prod_Nosso.viewport()):
                item_s = self.table_Prod_Nosso.currentItem()

                if item_s:
                    cod_selecionado = self.line_cod_f.text()
                    if cod_selecionado:
                        self.remove_pintura_lines()

                        dados_siger = extrair_tabela(self.table_Prod_Nosso)

                        item_selecionado_s = dados_siger[item_s.row()]
                        cod_s, descr_s, ref_s, um_s, ncm_s = item_selecionado_s

                        junta = f"{descr_s} - {ref_s}"

                        self.line_cod_s.setText(cod_s)
                        self.line_descr_s.setText(junta)
                        self.line_um_s.setText(um_s)
                        self.line_ncm_s.setText(ncm_s)

                        self.pintar_lines()

            return super(QMainWindow, self).eventFilter(sources, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def normalizar_um(self, um):
        try:
            if not um:
                return ""

            um = um.strip().upper()

            equivalentes_unidade = ["UN", "PC", "PÇ", "PCA", "PCS", "BB", "PCT"]

            if um in equivalentes_unidade:
                return "UN"

            return um

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def pintar_lines(self):
        try:
            cod_s = self.line_cod_s.text()

            if cod_s:
                um_f = self.line_um_f.text()
                ncm_f = self.line_ncm_f.text()

                um_s = self.line_um_s.text()
                ncm_s = self.line_ncm_s.text()

                um_f_norm = self.normalizar_um(um_f)
                um_s_norm = self.normalizar_um(um_s)

                if um_f_norm != um_s_norm:
                    self.line_um_f.setStyleSheet(f"QLineEdit {{ background-color: {cor_amarelo}; }}")
                    self.line_um_s.setStyleSheet(f"QLineEdit {{ background-color: {cor_amarelo}; }}")

                if ncm_f != ncm_s:
                    if ncm_f[:4] == ncm_s[:4]:
                        # 4 primeiros iguais → amarelo
                        self.line_ncm_f.setStyleSheet(f"background-color: {cor_amarelo};")
                        self.line_ncm_s.setStyleSheet(f"background-color: {cor_amarelo};")
                    else:
                        # 4 primeiros diferentes → vermelho
                        self.line_ncm_f.setStyleSheet(f"background-color: {cor_vermelho};")
                        self.line_ncm_s.setStyleSheet(f"background-color: {cor_vermelho};")

            else:
                self.line_cod_s.setStyleSheet(f"QLineEdit {{ background-color: {cor_vermelho}; }}")
                self.line_descr_s.setStyleSheet(f"QLineEdit {{ background-color: {cor_vermelho}; }}")
                self.line_um_s.setStyleSheet(f"QLineEdit {{ background-color: {cor_vermelho}; }}")
                self.line_ncm_s.setStyleSheet(f"QLineEdit {{ background-color: {cor_vermelho}; }}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def remove_pintura_lines(self):
        try:
            self.line_cod_s.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_descr_s.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_um_s.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_ncm_s.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")

            self.line_cod_f.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_descr_f.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_um_f.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")
            self.line_ncm_f.setStyleSheet(f"QLineEdit {{ background-color: {transparente}; }}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def abrir_tela_escolher_produto(self):
        try:
            from menu_cadastros.prod_pesquisar import TelaProdutoPesquisar

            self.escolher_produto = TelaProdutoPesquisar(True)
            self.escolher_produto.produto_escolhido.connect(self.atualizar_produto_entry)
            self.escolher_produto.show()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def atualizar_produto_entry(self, produto):
        try:
            self.line_Filtro_Siger1.setText(produto)

            self.buscar_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def iniciar_timer_busca(self):
        try:
            self.timer_busca.start(400)  # 400 ms (ajuste se quiser)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def buscar_produto(self):
        try:
            self.table_Prod_Nosso.setRowCount(0)

            texto = self.line_Filtro_Siger1.text().strip()

            if texto:
                if texto.isdigit():
                    produto = self.lanca_produtos_siger_por_cod(texto)
                    if not produto:
                        self.lanca_produtos_siger_por_descricao(texto)
                else:
                    self.lanca_produtos_siger_por_descricao(texto)
            else:
                fornecedor = self.combo_Fornecedor.currentText()

                if fornecedor:
                    fornecedor_tete = fornecedor.find(" - ")
                    id_fornecedor = fornecedor[:fornecedor_tete]

                    self.lanca_dados_ordens_abertas_forn(id_fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_fornecedor(self):
        try:
            self.combo_Fornecedor.clear()

            tabela = []

            branco = ""
            tabela.append(branco)

            cursor = conecta.cursor()

            sem_vinculo = self.radio_SemVinculo.isChecked()

            if sem_vinculo:
                sql = """
                SELECT DISTINCT pre.id_fornecedor, forn.razao
                FROM PRE_PRODUTO_FORNECEDOR as pre 
                INNER JOIN fornecedores as forn ON pre.id_fornecedor = forn.id 
                WHERE pre.ID_PRODUTO_SIGER IS NULL
                   OR pre.FATOR_CONVERSAO IS NULL
                """
            else:
                sql = """
                SELECT DISTINCT pre.id_fornecedor, forn.razao
                FROM PRE_PRODUTO_FORNECEDOR as pre 
                INNER JOIN fornecedores as forn ON pre.id_fornecedor = forn.id 
                """

            cursor.execute(sql)
            ids_fornecedores = cursor.fetchall()

            if ids_fornecedores:
                for dadus in ids_fornecedores:
                    ides, razao = dadus
                    msg = f"{ides} - {razao}"
                    tabela.append(msg)

                self.combo_Fornecedor.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_ordens_abertas_forn(self, id_fornecedor):
        try:
            nova_lista = []

            cursor = conecta.cursor()
            cursor.execute(
                f"SELECT oc.numero, prodoc.codigo, "
                f"prod.descricao, COALESCE(prod.obs, ''), "
                f"prod.unidade, prod.ncm "
                f"FROM ordemcompra as oc "
                f"INNER JOIN produtoordemcompra as prodoc ON oc.id = prodoc.mestre "
                f"INNER JOIN produto as prod ON prodoc.produto = prod.id "
                f"where oc.fornecedor = {id_fornecedor} "
                f"and oc.entradasaida = 'E' "
                f"AND oc.STATUS = 'A' "
                f"ORDER BY prod.descricao;")
            dados_oc = cursor.fetchall()

            if dados_oc:
                for i in dados_oc:
                    num_oc, cod, descr, ref, um, ncm = i

                    descr_oc = f"{descr} - OC {num_oc}"

                    if ncm:
                        ncm_limpa = re.sub(r'\D', '', ncm)  # remove tudo que não for número
                    else:
                        ncm_limpa = ""

                    nova_lista.append((cod, descr_oc, ref, um, ncm_limpa))

                    lanca_tabela_v2(self.table_Prod_Nosso, nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_produtos_fornecedor(self):
        try:
            self.limpa_tabelas()
            self.limpa_campos_selecionados()
            self.line_Filtro_Siger1.clear()

            fornecedor = self.combo_Fornecedor.currentText()

            if fornecedor:
                fornecedor_tete = fornecedor.find(" - ")
                id_fornecedor = fornecedor[:fornecedor_tete]

                sem_vinculo = self.radio_SemVinculo.isChecked()
                filtro = self.line_Filtro_F1.text().strip()

                sql = """
                SELECT 
                    pre.CODIGO_FORNECEDOR, 
                    pre.DESCRICAO, 
                    pre.UM, 
                    pre.NCM, 
                    COALESCE(prod.codigo, '-'), COALESCE(pre.FATOR_CONVERSAO, '-')
                FROM PRE_PRODUTO_FORNECEDOR as pre
                LEFT JOIN produto as prod 
                    ON pre.ID_PRODUTO_SIGER = prod.id 
                WHERE pre.ID_FORNECEDOR = ?
                """

                parametros = [id_fornecedor]

                # 🔹 Filtro sem vínculo
                if sem_vinculo:
                    sql += """
                    AND (
                        pre.ID_PRODUTO_SIGER IS NULL
                        OR pre.FATOR_CONVERSAO IS NULL
                    )
                    """

                # 🔹 Filtro por texto
                if filtro:
                    sql += " AND pre.DESCRICAO LIKE ?"
                    parametros.append(f"%{filtro}%")

                sql += " order by pre.DESCRICAO"

                cur = conecta.cursor()
                cur.execute(sql, parametros)
                detalhes_produto = cur.fetchall()

                if detalhes_produto:
                    lanca_tabela_v2(self.table_Prod_Forn, detalhes_produto)

                self.line_Filtro_Siger1.setFocus()

                self.lanca_dados_ordens_abertas_forn(id_fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_produtos_siger_por_cod(self, codigo):
        try:
            detalhes_limpos = []

            cursor = conecta.cursor()
            cursor.execute(f"SELECT codigo, descricao, COALESCE(obs, ''), unidade, COALESCE(ncm, '') "
                           f"FROM produto where codigo = {codigo};")
            detalhes_produto = cursor.fetchall()

            if detalhes_produto:
                for produto in detalhes_produto:
                    codigo, descricao, obs, unidade, ncm = produto

                    if ncm:
                        ncm_limpa = re.sub(r'\D', '', ncm)  # remove tudo que não for número
                    else:
                        ncm_limpa = ""

                    detalhes_limpos.append((codigo, descricao, obs, unidade, ncm_limpa))

                lanca_tabela_v2(self.table_Prod_Nosso, detalhes_limpos)

            return detalhes_limpos

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_produtos_siger_por_descricao(self, descricao):
        try:
            detalhes_limpos = []

            cursor = conecta.cursor()
            cursor.execute(
                "SELECT codigo, descricao, COALESCE(obs, ''), unidade, COALESCE(ncm, '') "
                "FROM produto WHERE UPPER(descricao) LIKE UPPER(?) order by descricao",
                (f"%{descricao}%",)
            )
            detalhes_produto = cursor.fetchall()

            if detalhes_produto:
                for produto in detalhes_produto:
                    codigo, descricao, obs, unidade, ncm = produto

                    if ncm:
                        ncm_limpa = re.sub(r'\D', '', ncm)  # remove tudo que não for número
                    else:
                        ncm_limpa = ""

                    detalhes_limpos.append((codigo, descricao, obs, unidade, ncm_limpa))

                lanca_tabela_v2(self.table_Prod_Nosso, detalhes_limpos)

            return detalhes_limpos

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def confere_vinculo_para_desvincular(self):
        try:
            cod_s = self.line_cod_s.text()
            cod_f = self.line_cod_f.text()
            fornecedor = self.combo_Fornecedor.currentText()

            if cod_s and cod_f and fornecedor:
                self.remover_vinculo(fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def remover_vinculo(self, fornecedor):
        try:
            fornecedor_tete = fornecedor.find(" - ")
            id_fornecedor = fornecedor[:fornecedor_tete]

            cod_f = self.line_cod_f.text()

            cursor = conecta.cursor()
            cursor.execute("""
            UPDATE PRE_PRODUTO_FORNECEDOR 
            SET ID_PRODUTO_SIGER = NULL, FATOR_CONVERSAO = NULL
            where ID_FORNECEDOR = ? 
            and CODIGO_FORNECEDOR = ?
            """, (id_fornecedor, cod_f))
            conecta.commit()

            self.mensagem_alerta("Produto desvinculado com sucesso!")

            self.reinicia_com_fornecedor_definido()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def confere_vinculo_para_vincular(self):
        try:
            cod_s = self.line_cod_s.text()
            cod_f = self.line_cod_f.text()
            fornecedor = self.combo_Fornecedor.currentText()

            fator_c = self.line_fator_s.text()

            if cod_s and cod_f and fornecedor:
                if not fator_c:
                    self.mensagem_alerta("O fator de Conversão dos produtos precisa ser vinculado!")
                else:
                    ncm_f = self.line_ncm_f.text()

                    ncm_s = self.line_ncm_s.text()

                    if ncm_f != ncm_s:
                        if ncm_f[:4] == ncm_s[:4]:
                            self.salvar_vinculo(fornecedor)
                        else:
                            self.mensagem_alerta("A NCM dos produtos são diferentes e não podem ser vinculados!")
                    else:
                        self.salvar_vinculo(fornecedor)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_vinculo(self, fornecedor):
        try:
            fornecedor_tete = fornecedor.find(" - ")
            id_fornecedor = fornecedor[:fornecedor_tete]

            cod_f = self.line_cod_f.text()

            cod_s = self.line_cod_s.text()

            fator_c = valores_para_float(self.line_fator_s.text())

            cur = conecta.cursor()
            cur.execute("""
            SELECT id, codigo FROM produto WHERE codigo = ?
            """, (cod_s,))
            select_prod = cur.fetchall()
            if select_prod:
                id_prod, cod_prod = select_prod[0]

                cursor = conecta.cursor()
                cursor.execute("""
                UPDATE PRE_PRODUTO_FORNECEDOR SET ID_PRODUTO_SIGER = ?, FATOR_CONVERSAO = ?
                where ID_FORNECEDOR = ? and CODIGO_FORNECEDOR = ?
                """, (id_prod, fator_c, id_fornecedor, cod_f))
                conecta.commit()

                self.mensagem_alerta("Produto vinculado com sucesso!")

                self.reinicia_com_fornecedor_definido()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaVincularProdutoFornecedor()
    tela.show()
    qt.exec_()
