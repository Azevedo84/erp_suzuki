import sys
from banco_dados.conexao import conecta
from forms.tela_prod_incluir import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab
from comandos.telas import tamanho_aplicacao, icone
from comandos.lines import validador_decimal
from comandos.conversores import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import re
from datetime import date
import traceback


class TelaProdutoIncluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Produto)

        self.table_Produto.viewport().installEventFilter(self)

        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.line_Codigo.editingFinished.connect(self.lanca_codigo_barras)

        validador_decimal(self.line_NCM, numero=9999999.000)

        self.inicio_manipula_pre_cadastro()
        self.lanca_combo_conjunto()
        self.lanca_combo_servico_interno()
        self.lanca_combo_tipo()
        self.lanca_combo_projeto()
        self.data_emissao()

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
            
    def limpa_tabela(self):
        try:
            nome_tabela = self.table_Produto

            nome_tabela.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_formato_referencia(self, referencia):
        try:
            padrao = re.compile(r'^D \d{2}\.\d{2}\.\d{3}\.\d{2}$')
            correspondencia = padrao.match(referencia)
    
            return correspondencia
        
        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def remover_espaco_branco_ini_fim(self, string):
        try:
            if string.endswith(' '):
                string_final = string.rstrip()
            else:
                string_final = string
    
            if string_final.startswith(' '):
                string_final1 = string_final.lstrip()
            else:
                string_final1 = string_final.lstrip()
    
            return string_final1
        
        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def inicio_manipula_pre_cadastro(self):
        try:
            self.limpa_tabela()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, descricao, referencia, um, fornecedor "
                           f"FROM PRODUTOPRELIMINAR "
                           f"WHERE (codigo IS NULL) AND (entregue IS NULL OR entregue = '');")
            dados_banco = cursor.fetchall()

            if dados_banco:
                lanca_tabela(self.table_Produto, dados_banco)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def data_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_conjunto(self):
        try:
            self.combo_Conjunto.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, conjunto FROM conjuntos order by conjunto;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Conjunto.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_servico_interno(self):
        try:
            self.combo_Servico_Interno.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, descricao FROM SERVICO_INTERNO order by descricao;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Servico_Interno.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_tipo(self):
        try:
            self.combo_Tipo.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, tipomaterial FROM TIPOMATERIAL order by tipomaterial;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Tipo.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_combo_projeto(self):
        try:
            self.combo_Projeto.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, projeto FROM PROJETO order by projeto;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Projeto.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_codigo_barras(self):
        if not self.processando:
            try:
                self.processando = True

                codigo_produto = self.line_Codigo.text()

                if codigo_produto:
                    prefixo = "SZP"
                    total_digitos = 10
                    zeros_de_preenchimento = total_digitos - len(prefixo) - len(str(codigo_produto))
                    codigo_barras = prefixo + "0" * zeros_de_preenchimento + str(codigo_produto)
                    self.line_Barras.setText(codigo_barras)

                    self.line_Custo_Unit.setText("0")
                    self.line_Qtde_Mini.setText("0")

                    if not self.line_kg_mt.text():
                        self.line_kg_mt.setText("0")

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def eventFilter(self, source, event):
        try:
            qtable_widget = self.table_Produto

            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is qtable_widget.viewport()):

                self.label_Fornecedor.setText("")

                self.limpa_dados_produto()

                item = qtable_widget.currentItem()

                extrai_recomendados = extrair_tabela(qtable_widget)
                item_selecionado = extrai_recomendados[item.row()]

                id_pre, desc, ref, um, forn = item_selecionado

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, registro, obs, descricao, descr_compl, referencia, um, ncm, "
                               f"kg_mt, fornecedor, data_criacao, codigo "
                               f"FROM PRODUTOPRELIMINAR "
                               f"where id = {id_pre};")
                dados_banco = cursor.fetchall()

                if dados_banco:
                    for i in dados_banco:
                        id_pres, registro, obs, descrs, compl, refs, ums, ncm, kg_mt, forns, emissao, cod_prod = i

                        descr_sem = self.remover_espaco_branco_ini_fim(descrs)
                        compl_sem = self.remover_espaco_branco_ini_fim(compl)
                        ref_sem = self.remover_espaco_branco_ini_fim(refs)

                        ja_existe = self.verifica_ref_desenho_existe(ref_sem)
                        if ja_existe:
                            msg = ""
                            for ii in ja_existe:
                                cod_des, descr_des, ref_des = ii
                                msg += f"{cod_des} - {descr_des} - {ref_des}\n"
                            self.mensagem_alerta(f"Já existe produtos com este número de desenho!\n\n{msg}")
                        else:
                            if forns:
                                self.label_Fornecedor.setText(forns)
                                self.manipula_fornecedor_tipo(forns)

                            if ums == "KG":
                                self.line_Embalagem.setText("SIM")

                            self.manipula_ref_desenho(ref_sem)
                            self.manipula_descricao_tipo(descr_sem)

                            self.line_ID_Pre.setText(str(id_pres))
                            self.line_Descricao.setText(descr_sem)
                            self.line_DescrCompl.setText(compl_sem)
                            self.line_Referencia.setText(ref_sem)
                            self.line_NCM.setText(ncm)
                            self.line_kg_mt.setText(str(kg_mt))
                            self.line_Custo_Unit.setText("0")
                            self.line_Qtde_Mini.setText("0")

                            um_count = self.combo_UM.count()
                            for i_um in range(um_count):
                                um_text = self.combo_UM.itemText(i_um)
                                if ums in um_text:
                                    self.combo_UM.setCurrentText(um_text)

                            self.line_Codigo.setFocus()

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_ref_desenho(self, refs):
        try:
            if self.verifica_formato_referencia(refs):
                ref_sem_d = refs[2:]
                cod_maq = int(ref_sem_d[0:2])

                cursor = conecta.cursor()
                cursor.execute(f"SELECT num_maq, descricao FROM maquina "
                               f"where num_maq = {cod_maq};")
                dados_maquina = cursor.fetchall()
                if dados_maquina:
                    id_maq, descr_maq = dados_maquina[0]
                    self.label_Maquina_Des.setText(descr_maq)

                tp = int(ref_sem_d[-2:])
                conj_peca = (ref_sem_d[3:5])

                if tp == 1 or tp == 3 or tp == 4 or tp == 5 or tp == 6 or tp == 7:
                    if conj_peca == "00":
                        tip_count = self.combo_Tipo.count()
                        for i_tip in range(tip_count):
                            tip_text = self.combo_Tipo.itemText(i_tip)
                            if "87 - CONJUNTO" in tip_text:
                                self.combo_Tipo.setCurrentText(tip_text)

                        if tp == 1:
                            tip_count = self.combo_Servico_Interno.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Servico_Interno.itemText(i_tip)
                                if "3 - MONTAGEM" in tip_text:
                                    self.combo_Servico_Interno.setCurrentText(tip_text)

                        if tp == 4:
                            tip_count = self.combo_Servico_Interno.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Servico_Interno.itemText(i_tip)
                                if "1 - SOLDA" in tip_text:
                                    self.combo_Servico_Interno.setCurrentText(tip_text)

                    elif conj_peca == "01":
                        if tp == 3 or tp == 5 or tp == 6:
                            tip_count = self.combo_Tipo.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Tipo.itemText(i_tip)
                                if "88 - USINAGEM" in tip_text:
                                    self.combo_Tipo.setCurrentText(tip_text)

                        if tp == 3:
                            tip_count = self.combo_Servico_Interno.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Servico_Interno.itemText(i_tip)
                                if "2 - CORTE" in tip_text:
                                    self.combo_Servico_Interno.setCurrentText(tip_text)

                        if tp == 5:
                            tip_count = self.combo_Servico_Interno.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Servico_Interno.itemText(i_tip)
                                if "4 - USINAGEM" in tip_text:
                                    self.combo_Servico_Interno.setCurrentText(tip_text)

                        if tp == 6:
                            tip_count = self.combo_Servico_Interno.count()
                            for i_tip in range(tip_count):
                                tip_text = self.combo_Servico_Interno.itemText(i_tip)
                                if "5 - FRESA" in tip_text:
                                    self.combo_Servico_Interno.setCurrentText(tip_text)

                    if tp == 7:
                        tip_count = self.combo_Tipo.count()
                        for i_tip in range(tip_count):
                            tip_text = self.combo_Tipo.itemText(i_tip)
                            if "119 - INDUSTRIALIZACAO" in tip_text:
                                self.combo_Tipo.setCurrentText(tip_text)

                    conj_count = self.combo_Conjunto.count()
                    for i_conj in range(conj_count):
                        conj_text = self.combo_Conjunto.itemText(i_conj)
                        if "10 - PRODUTOS ACABADOS" in conj_text:
                            self.combo_Conjunto.setCurrentText(conj_text)
                else:
                    conj_count = self.combo_Conjunto.count()
                    for i_conj in range(conj_count):
                        conj_text = self.combo_Conjunto.itemText(i_conj)
                        if "8 - MATERIA PRIMA" in conj_text:
                            self.combo_Conjunto.setCurrentText(conj_text)

                if tp == 23:
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "116 - CORTE A LASER F" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

                elif tp == 21:
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "85 - CORTE A J'AGUA" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

                elif tp == 22:
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "84 - CORTE A LASER" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

                elif tp == 24:
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "125 - CORTE A OXICORTE" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

            else:
                conj_count = self.combo_Conjunto.count()
                for i_conj in range(conj_count):
                    conj_text = self.combo_Conjunto.itemText(i_conj)
                    if "8 - MATERIA PRIMA" in conj_text:
                        self.combo_Conjunto.setCurrentText(conj_text)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_ref_desenho_existe(self, refs):
        try:
            ja_existe = []

            if self.verifica_formato_referencia(refs):
                cursor = conecta.cursor()
                cursor.execute(f"SELECT codigo, descricao, obs FROM produto where obs = '{refs}';")
                lista_completa = cursor.fetchall()
                if lista_completa:
                    ja_existe = lista_completa

            return ja_existe

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_descricao_tipo(self, descricao):
        try:
            posicao = descricao.find(" ")
            prim_palavra = descricao[:posicao]

            if prim_palavra == "INVERSOR":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "98 - INVERSORES" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "PARAFUSO":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "76 - FATI/FG" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "ROLAMENTO":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "78 - JJD" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "CONTACTORA":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "82 - REAL CENTER" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "CONTATOR":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "82 - REAL CENTER" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "BOTAO":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "82 - REAL CENTER" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "RELE":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "82 - REAL CENTER" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

            elif prim_palavra == "RESISTENCIA":
                tip_count = self.combo_Tipo.count()
                for i_tip in range(tip_count):
                    tip_text = self.combo_Tipo.itemText(i_tip)
                    if "109 - RESIMAC" in tip_text:
                        self.combo_Tipo.setCurrentText(tip_text)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_fornecedor_tipo(self, fornecedor):
        try:
            qtde_palavras = len(fornecedor.split())

            if qtde_palavras == 1:
                if fornecedor == "PWM":
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "126 - PWM" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

                if fornecedor == "SIMILAR":
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "90 - SIMILAR" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

                if fornecedor == "SENSORVILLE":
                    tip_count = self.combo_Tipo.count()
                    for i_tip in range(tip_count):
                        tip_text = self.combo_Tipo.itemText(i_tip)
                        if "140 - SENSORVILLE" in tip_text:
                            self.combo_Tipo.setCurrentText(tip_text)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_dados_produto(self):
        try:
            self.line_ID_Pre.clear()
            self.line_Codigo.clear()
            self.line_Referencia.clear()
            self.line_Descricao.clear()
            self.line_DescrCompl.clear()
            self.line_Embalagem.clear()
            self.line_NCM.clear()
            self.line_kg_mt.clear()
            self.line_Qtde_Mini.clear()
            self.line_Custo_Unit.clear()
            self.line_Local.clear()
            self.line_Barras.clear()
            self.plain_Obs.clear()

            self.combo_UM.setCurrentText("")
            self.combo_Conjunto.setCurrentText("")
            self.combo_Tipo.setCurrentText("")
            self.combo_Projeto.setCurrentText("")
            self.combo_Servico_Interno.setCurrentText("")

            self.label_Maquina_Des.setText("")

            self.data_emissao()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tudo(self):
        try:
            self.limpa_dados_produto()
            self.inicio_manipula_pre_cadastro()
            self.lanca_combo_conjunto()
            self.lanca_combo_servico_interno()
            self.lanca_combo_tipo()
            self.lanca_combo_projeto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            cod_produto = self.line_Codigo.text()
            cod_barras = self.line_Barras.text()
            descr = self.line_Descricao.text()
            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            conjunto = self.combo_Conjunto.currentText()
            servico_interno = self.combo_Servico_Interno.currentText()
            tipo = self.combo_Tipo.currentText()

            if not cod_produto:
                self.mensagem_alerta(f'O Código do produto não pode estar vazio!')
            elif not cod_barras:
                self.mensagem_alerta(f'O Código de barras do produto não pode estar vazio!')
            elif not descr:
                self.mensagem_alerta(f'A Descrição do produto não pode estar vazia!')
            elif not ncm:
                self.mensagem_alerta(f'A NCM do produto não pode estar vazia!')
            elif not um:
                self.mensagem_alerta(f'A Unidade de Medida (UM) do produto não pode estar vazia!')
            elif not conjunto:
                self.mensagem_alerta(f'O Conjunto do produto não pode estar vazio!')
            elif not tipo:
                self.mensagem_alerta(f'O Tipo de Material do produto não pode estar vazio!')
            else:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT codigo, descricao, obs FROM produto where codigo = '{cod_produto}';")
                lista_completa = cursor.fetchall()
                if lista_completa:
                    self.mensagem_alerta(f'Este código de produto já foi cadastrado!')
                else:
                    conjuntotete = conjunto.find(" - ")
                    id_conjunto = conjunto[:conjuntotete]

                    if um == "KG":
                        kg_mt = self.line_kg_mt.text()
                        if not kg_mt:
                            self.mensagem_alerta(f'Se o material for Aço, verifique o campo "KG/MT"')
                        self.salvar_produto()
                    elif id_conjunto == "10":
                        if not servico_interno:
                            self.mensagem_alerta(f'O Serviço Interno do produto acabado não pode estar vazio!')
                        else:
                            self.salvar_produto()
                    else:
                        self.salvar_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_pre_cadastro(self):
        try:
            id_pre = self.line_ID_Pre.text()
            cod_produto = self.line_Codigo.text()

            if id_pre:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, registro, obs, descricao, descr_compl, referencia, um, ncm, "
                               f"kg_mt, fornecedor, data_criacao, codigo "
                               f"FROM PRODUTOPRELIMINAR "
                               f"where id = {id_pre};")
                dados_banco = cursor.fetchall()

                if dados_banco:
                    for i in dados_banco:
                        id_pres, registro, obs, descrs, compl, refs, ums, ncm, kg_mt, forns, emissao, cod_prod = i

                        cursor = conecta.cursor()
                        cursor.execute(f"UPDATE PRODUTOPRELIMINAR SET CODIGO = {cod_produto} WHERE id = {id_pres};")

                        conecta.commit()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_produto(self):
        try:
            cod_produto = self.line_Codigo.text()
            ref = self.line_Referencia.text()
            descr = self.line_Descricao.text()
            compl = self.line_DescrCompl.text()
            embalagem = self.line_Embalagem.text()
            ncm = self.line_NCM.text()
            kg_mt = self.line_kg_mt.text()
            kg_mt_float = valores_para_float(kg_mt)
            qtde_minima = self.line_Qtde_Mini.text()
            custo_unit = self.line_Custo_Unit.text()
            local = self.line_Local.text()
            cod_barras = self.line_Barras.text()

            obs = self.plain_Obs.toPlainText()

            conjunto = self.combo_Conjunto.currentText()
            conjuntotete = conjunto.find(" - ")
            id_conjunto = conjunto[:conjuntotete]

            if id_conjunto == "10":
                servico_interno = self.combo_Servico_Interno.currentText()
                servico_internotete = servico_interno.find(" - ")
                id_servico_interno = servico_interno[:servico_internotete]
            else:
                id_servico_interno = "NULL"

            tipo = self.combo_Tipo.currentText()
            tipotete = tipo.find(" - ")
            id_tipo = tipo[:tipotete]

            um = self.combo_UM.currentText()

            data_hoje = date.today()

            projeto = self.combo_Projeto.currentText()
            if projeto:
                projetotete = projeto.find(" - ")
                id_projeto = projeto[:projetotete]

                cursor = conecta.cursor()
                cursor.execute(f"Insert into produto (ID, CODIGO, CODBARRAS, CONJUNTO, ID_SERVICO_INTERNO, "
                               f"DESCRICAO, "
                               f"DESCRICAOCOMPLEMENTAR, EMBALAGEM, UNIDADE, MEDIDADECORTE, PESO, "
                               f"KILOSMETRO, QUANTIDADE, QUANTIDADEMIN, CUSTOUNITARIO, OBS, LOCALIZACAO, "
                               f"DATA, CUSTOESTRUTURA, TIPOMATERIAL, PROJETO, OBS2, NCM) "
                               f"values (GEN_ID(GEN_PRODUTO_ID,1), '{cod_produto}', '{cod_barras}', "
                               f"'{id_conjunto}', {id_servico_interno}, '{descr}', '{compl}', '{embalagem}', "
                               f"'{um}', '0', '0', "
                               f"'{kg_mt_float}', '0', '{qtde_minima}', '{custo_unit}', '{ref}', '{local}', "
                               f"'{data_hoje}', "
                               f"'0', '{id_tipo}', '{id_projeto}', '{obs}', '{ncm}');")
            else:
                cursor = conecta.cursor()
                cursor.execute(f"Insert into produto (ID, CODIGO, CODBARRAS, CONJUNTO, ID_SERVICO_INTERNO, "
                               f"DESCRICAO, "
                               f"DESCRICAOCOMPLEMENTAR, EMBALAGEM, UNIDADE, MEDIDADECORTE, PESO, "
                               f"KILOSMETRO, QUANTIDADE, QUANTIDADEMIN, CUSTOUNITARIO, OBS, LOCALIZACAO, "
                               f"DATA, CUSTOESTRUTURA, TIPOMATERIAL, OBS2, NCM) "
                               f"values (GEN_ID(GEN_PRODUTO_ID,1), '{cod_produto}', '{cod_barras}', "
                               f"'{id_conjunto}', {id_servico_interno}, '{descr}', '{compl}', '{embalagem}', "
                               f"'{um}', '0', '0', "
                               f"'{kg_mt_float}', '0', '{qtde_minima}', '{custo_unit}', '{ref}', '{local}', "
                               f"'{data_hoje}', "
                               f"'0', '{id_tipo}', '{obs}', '{ncm}');")

                conecta.commit()

            self.mensagem_alerta(f"Cadastro do produto {cod_produto} realizado com Sucesso!")

            self.verifica_pre_cadastro()

            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaProdutoIncluir()
    tela.show()
    qt.exec_()
