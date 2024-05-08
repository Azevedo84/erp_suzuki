import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab, limpa_tabela
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from forms.tela_prod_incluir import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import inspect
import os
from unidecode import unidecode
import re
from datetime import date


class TelaProdutoIncluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        self.layout_tabela(self.table_Produto)
        self.layout_proprio()

        self.table_Produto.viewport().installEventFilter(self)

        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.line_Codigo.editingFinished.connect(self.lanca_codigo_barras)
        self.processando = False

        self.definir_validador()
        self.inicio_manipula_pre_cadastro()
        self.lanca_combo_conjunto()
        self.lanca_combo_tipo()
        self.lanca_combo_projeto()
        self.data_emissao()

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor1)
            cor_widget(self.widget_Cor2)
            cor_widget(self.widget_Cor3)
            cor_widget(self.widget_Cor4)

            cor_fonte(self.label)
            cor_fonte(self.label_11)
            cor_fonte(self.label_13)
            cor_fonte(self.label_16)
            cor_fonte(self.label_14)
            cor_fonte(self.label_10)
            cor_fonte(self.label_17)
            cor_fonte(self.label_2)
            cor_fonte(self.label_26)
            cor_fonte(self.label_3)
            cor_fonte(self.label_4)
            cor_fonte(self.label_5)
            cor_fonte(self.label_50)
            cor_fonte(self.label_59)
            cor_fonte(self.label_6)
            cor_fonte(self.label_63)
            cor_fonte(self.label_64)
            cor_fonte(self.label_68)
            cor_fonte(self.label_8)
            cor_fonte(self.label_9)
            cor_fonte(self.label_Titulo)
            cor_fonte(self.label_7)
            cor_fonte(self.label_78)
            cor_fonte(self.label_74)
            cor_fonte(self.label_73)
            cor_fonte(self.label_76)
            cor_fonte(self.label_72)
            cor_fonte(self.label_75)
            cor_fonte(self.label_77)
            cor_fonte(self.label_79)
            cor_fonte(self.label_80)

            cor_btn(self.btn_Salvar)
            cor_btn(self.btn_Limpar)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 35)
            nome_tabela.setColumnWidth(1, 190)
            nome_tabela.setColumnWidth(2, 90)
            nome_tabela.setColumnWidth(3, 30)
            nome_tabela.setColumnWidth(4, 110)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def remover_acentos(self, string):
        try:
            return unidecode(string)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_formato_referencia(self, referencia):
        try:
            padrao = re.compile(r'^D \d{2}\.\d{2}\.\d{3}\.\d{2}$')
            correspondencia = padrao.match(referencia)

            return correspondencia

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def definir_validador(self):
        try:
            validator = QtGui.QDoubleValidator(0, 9999999.000, 3, self.line_NCM)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            validator.setBottom(0.001)

            self.line_NCM.setValidator(validator)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def inicio_manipula_pre_cadastro(self):
        try:
            limpa_tabela(self.table_Produto)

            tabela = []
            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, registro, obs, descricao, descr_compl, referencia, um, ncm, "
                           f"kg_mt, fornecedor, data_criacao, codigo "
                           f"FROM PRODUTOPRELIMINAR "
                           f"WHERE (codigo IS NULL) AND (entregue IS NULL OR entregue = '');")
            dados_banco = cursor.fetchall()

            if dados_banco:
                for i in dados_banco:
                    id_pre, registro, obs, descr, compl, ref, um, ncm, kg_mt, forn, emissao, cod_prod = i

                    dados = (id_pre, descr, ref, um, forn)
                    tabela.append(dados)

            if tabela:
                lanca_tabela(self.table_Produto, tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def data_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def lanca_codigo_barras(self):
        if not self.processando:
            try:
                self.processando = True

                codigo_produto = self.line_Codigo.text()

                if codigo_produto:
                    self.line_Barras.setText(codigo_produto)

                    self.line_Custo_Unit.setText("0")
                    self.line_Qtde_Mini.setText("0")

                    if not self.line_kg_mt.text():
                        self.line_kg_mt.setText("0")

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
                            mensagem_alerta(f"Já existe produtos com este número de desenho!\n\n{msg}")
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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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

                if tp == 1 or tp == 3 or tp == 4 or tp == 5 or tp == 6 or tp == 7:
                    if tp == 1 or tp == 4:
                        tip_count = self.combo_Tipo.count()
                        for i_tip in range(tip_count):
                            tip_text = self.combo_Tipo.itemText(i_tip)
                            if "87 - CONJUNTO" in tip_text:
                                self.combo_Tipo.setCurrentText(tip_text)

                    if tp == 3 or tp == 5 or tp == 6:
                        tip_count = self.combo_Tipo.count()
                        for i_tip in range(tip_count):
                            tip_text = self.combo_Tipo.itemText(i_tip)
                            if "88 - USINAGEM" in tip_text:
                                self.combo_Tipo.setCurrentText(tip_text)

                    if tp == 7:
                        tip_count = self.combo_Tipo.count()
                        for i_tip in range(tip_count):
                            tip_text = self.combo_Tipo.itemText(i_tip)
                            if "119 - INDUSTRIALIZACAO" in tip_text:
                                self.combo_Tipo.setCurrentText(tip_text)

                    conj_count = self.combo_Conjunto.count()
                    for i_conj in range(conj_count):
                        conj_text = self.combo_Conjunto.itemText(i_conj)
                        if "10 - Produtos Acabados" in conj_text:
                            self.combo_Conjunto.setCurrentText(conj_text)
                else:
                    conj_count = self.combo_Conjunto.count()
                    for i_conj in range(conj_count):
                        conj_text = self.combo_Conjunto.itemText(i_conj)
                        if "8 - Materia Prima" in conj_text:
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
                    if "8 - Materia Prima" in conj_text:
                        self.combo_Conjunto.setCurrentText(conj_text)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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

            self.label_Maquina_Des.setText("")

            self.data_emissao()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def limpa_tudo(self):
        try:
            self.limpa_dados_produto()
            self.inicio_manipula_pre_cadastro()
            self.lanca_combo_conjunto()
            self.lanca_combo_tipo()
            self.lanca_combo_projeto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_salvamento(self):
        try:
            cod_produto = self.line_Codigo.text()
            cod_barras = self.line_Barras.text()
            descr = self.line_Descricao.text()
            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            conjunto = self.combo_Conjunto.currentText()
            tipo = self.combo_Tipo.currentText()

            if not cod_produto:
                mensagem_alerta(f'O Código do produto não pode estar vazio!')
            elif not cod_barras:
                mensagem_alerta(f'O Código de barras do produto não pode estar vazio!')
            elif not descr:
                mensagem_alerta(f'A Descrição do produto não pode estar vazia!')
            elif not ncm:
                mensagem_alerta(f'A NCM do produto não pode estar vazia!')
            elif not um:
                mensagem_alerta(f'A Unidade de Medida (UM) do produto não pode estar vazia!')
            elif not conjunto:
                mensagem_alerta(f'O Conjunto do produto não pode estar vazio!')
            elif not tipo:
                mensagem_alerta(f'O Tipo de Material do produto não pode estar vazio!')
            else:
                if um == "KG":
                    kg_mt = self.line_kg_mt.text()
                    if not kg_mt:
                        mensagem_alerta(f'O "KG/MT" do produto não pode estar vazio!')
                    else:
                        self.salvar_produto()
                else:
                    self.salvar_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

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
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def salvar_produto(self):
        try:
            cod_produto = self.line_Codigo.text()
            ref = self.line_Referencia.text()
            descr = self.line_Descricao.text()
            compl = self.line_DescrCompl.text()
            embalagem = self.line_Embalagem.text()
            ncm = self.line_NCM.text()
            kg_mt = self.line_kg_mt.text()
            qtde_minima = self.line_Qtde_Mini.text()
            custo_unit = self.line_Custo_Unit.text()
            local = self.line_Local.text()
            cod_barras = self.line_Barras.text()
            obs = self.plain_Obs.toPlainText()

            conjunto = self.combo_Conjunto.currentText()
            conjuntotete = conjunto.find(" - ")
            id_conjunto = conjunto[:conjuntotete]

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
                cursor.execute(f"Insert into produto (ID, CODIGO, CODBARRAS, CONJUNTO, DESCRICAO, "
                               f"DESCRICAOCOMPLEMENTAR, EMBALAGEM, UNIDADE, MEDIDADECORTE, PESO, "
                               f"KILOSMETRO, QUANTIDADE, QUANTIDADEMIN, CUSTOUNITARIO, OBS, LOCALIZACAO, "
                               f"DATA, CUSTOESTRUTURA, TIPOMATERIAL, PROJETO, OBS2, NCM) "
                               f"values (GEN_ID(GEN_PRODUTO_ID,1), '{cod_produto}', '{cod_barras}', '{id_conjunto}', "
                               f"'{descr}', '{compl}', '{embalagem}', '{um}', '0', '0', '{kg_mt}', '0', "
                               f"'{qtde_minima}', '{custo_unit}', '{ref}', '{local}', '{data_hoje}', "
                               f"'0', '{id_tipo}', '{id_projeto}', '{obs}', '{ncm}');")
            else:
                cursor = conecta.cursor()
                cursor.execute(f"Insert into produto (ID, CODIGO, CODBARRAS, CONJUNTO, DESCRICAO, "
                               f"DESCRICAOCOMPLEMENTAR, EMBALAGEM, UNIDADE, MEDIDADECORTE, PESO, "
                               f"KILOSMETRO, QUANTIDADE, QUANTIDADEMIN, CUSTOUNITARIO, OBS, LOCALIZACAO, "
                               f"DATA, CUSTOESTRUTURA, TIPOMATERIAL, OBS2, NCM) "
                               f"values (GEN_ID(GEN_PRODUTO_ID,1), '{cod_produto}', '{cod_barras}', '{id_conjunto}', "
                               f"'{descr}', '{compl}', '{embalagem}', '{um}', '0', '0', '{kg_mt}', '0', "
                               f"'{qtde_minima}', '{custo_unit}', '{ref}', '{local}', '{data_hoje}', "
                               f"'0', '{id_tipo}', '{obs}', '{ncm}');")

                conecta.commit()

            mensagem_alerta(f"Cadastro do produto {cod_produto} realizado com Sucesso!")

            self.verifica_pre_cadastro()

            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaProdutoIncluir()
    tela.show()
    qt.exec_()
