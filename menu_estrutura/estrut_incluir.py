import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import grava_erro_banco
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, limpa_tabela, layout_cabec_tab
from comandos.comando_lines import validador_decimal, validador_inteiro
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget_cab
from comandos.comando_conversoes import valores_para_float, valores_para_virgula
from banco_dados.bc_consultas import Produto
from forms.tela_estrut_incluir import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
from functools import partial
import traceback


class TelaEstruturaIncluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_estrutura.png")
        tamanho_aplicacao(self)
        self.layout_tabela(self.table_Estrutura)
        cor_widget_cab(self.widget_cabecalho)

        self.tab_prod = Produto()

        self.definir_line_bloqueados()

        self.line_Codigo_Estrut.setFocus()

        self.line_Codigo_Estrut.editingFinished.connect(self.verifica_line_codigo_acabado)
        self.line_Codigo_Manu.editingFinished.connect(self.verifica_line_codigo_manual)
        self.line_Qtde_Manu.editingFinished.connect(self.verifica_line_qtde_manual)
        self.line_Medida_Manu.editingFinished.connect(self.verifica_line_medida_manual)
        self.line_Tempo_Mao.editingFinished.connect(self.mascara_tempo_mao_de_obra)

        self.btn_ExcluirTudo.clicked.connect(partial(limpa_tabela, self.table_Estrutura))
        self.btn_ExcluirItem.clicked.connect(self.verifica_ops_consumidas)
        self.btn_Limpar.clicked.connect(self.limpar)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.processando = False

        self.check_Converte_Manu.stateChanged.connect(self.verifica_check_converter_kilos)

        validador_inteiro(self.line_Codigo_Estrut, 1234567)
        validador_inteiro(self.line_Codigo_Manu, 1234567)

        validador_decimal(self.line_Qtde_Manu, 9999999.000)
        validador_decimal(self.line_Medida_Manu, 9999999.000)

        self.widget_MaoObra.setHidden(True)
        self.widget_Terceiros.setHidden(True)
        self.widget_medida_peca.setHidden(True)

    def trata_excecao(self, nome_funcao, mensagem, arquivo):
        try:
            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}"\n{mensagem}')
            self.mensagem_alerta(f'Houve um problema no arquivo:\n\n{arquivo}\n\n'
                                 f'Comunique o desenvolvedor sobre o problema descrito abaixo:\n\n'
                                 f'{nome_funcao}: {mensagem}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

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
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

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
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def layout_tabela(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 40)
            nome_tabela.setColumnWidth(1, 210)
            nome_tabela.setColumnWidth(2, 100)
            nome_tabela.setColumnWidth(3, 30)
            nome_tabela.setColumnWidth(4, 60)
            nome_tabela.setColumnWidth(5, 65)
            nome_tabela.setColumnWidth(6, 110)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_check_converter_kilos(self):
        try:
            if self.check_Converte_Manu.isChecked():
                self.widget_medida_peca.setHidden(False)
            else:
                self.widget_medida_peca.setHidden(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def definir_line_bloqueados(self):
        try:
            self.line_Descricao_Estrut.setReadOnly(True)
            self.line_Referencia_Estrut.setReadOnly(True)
            self.line_Tipo_Estrut.setReadOnly(True)
            self.line_NCM_Estrut.setReadOnly(True)
            self.line_UM_Estrut.setReadOnly(True)

            self.line_Descricao_Manu.setReadOnly(True)
            self.line_DescrCompl_Manu.setReadOnly(True)
            self.line_Referencia_Manu.setReadOnly(True)
            self.line_UM_Manu.setReadOnly(True)
            self.line_NCM_Manu.setReadOnly(True)
            self.line_Kg_Manu.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_line_codigo_acabado(self):
        if not self.processando:
            try:
                self.processando = True

                self.limpa_tudo()

                codigo_produto = self.line_Codigo_Estrut.text()

                if not codigo_produto:
                    self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                    self.limpa_dados_produto_estrutura()
                    limpa_tabela(self.table_Estrutura)
                elif int(codigo_produto) == 0:
                    self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                    self.limpa_dados_produto_estrutura()
                    limpa_tabela(self.table_Estrutura)
                else:
                    self.verifica_sql_acabado()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
                grava_erro_banco(nome_funcao, e, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_sql_acabado(self):
        try:
            codigo_produto = self.line_Codigo_Estrut.text()
            cursor = conecta.cursor()
            cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, conjunto, quantidade "
                           f"FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cursor.fetchall()
            if not detalhes_produto:
                self.mensagem_alerta('Este código de produto não existe!')
                self.limpa_dados_produto_estrutura()
                limpa_tabela(self.table_Estrutura)
                self.line_Codigo_Estrut.clear()
            else:
                conjunto = detalhes_produto[0][3]
                if conjunto == 10:
                    self.lanca_dados_acabado()
                else:
                    self.mensagem_alerta('Este produto não tem o conjunto classificado como "Produtos Acabados"!')
                    self.limpa_dados_produto_estrutura()
                    limpa_tabela(self.table_Estrutura)
                    self.line_Codigo_Estrut.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_dados_acabado(self):
        try:
            codigo_produto = self.line_Codigo_Estrut.text()
            cur = conecta.cursor()
            cur.execute(f"SELECT prod.descricao, COALESCE(tip.tipomaterial, '') as tipus, "
                        f"COALESCE(prod.obs, '') as ref, prod.unidade, "
                        f"COALESCE(prod.ncm, '') as ncm, COALESCE(prod.obs2, '') as obs "
                        f"FROM produto as prod "
                        f"LEFT JOIN tipomaterial tip ON prod.tipomaterial = tip.id "
                        f"where codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()
            descr, tipo, ref, um, ncm, obs = detalhes_produto[0]

            self.line_Descricao_Estrut.setText(descr)
            self.line_Referencia_Estrut.setText(ref)
            self.line_Tipo_Estrut.setText(tipo)
            self.line_NCM_Estrut.setText(ncm)
            self.line_UM_Estrut.setText(um)

            tipo_material = self.line_Tipo_Estrut.text()

            if not tipo_material:
                self.mensagem_alerta('O campo "Tipo de Material" não pode estar vazio!\n\n'
                                     'Entre no cadastro de produtos e defina o Tipo de Material:\n'
                                     'Exemplos: CONJUNTO, USINAGEM, INDUSTRIALIZACAO')
                self.limpa_dados_produto_estrutura()
                limpa_tabela(self.table_Estrutura)
                self.line_Codigo_Estrut.clear()
            else:
                self.line_Obs.setText(obs)

                if tipo == "INDUSTRIALIZACAO":
                    self.widget_Terceiros.setHidden(False)
                    self.widget_MaoObra.setHidden(True)
                else:
                    self.widget_MaoObra.setHidden(False)
                    self.widget_Terceiros.setHidden(True)

                self.line_Codigo_Manu.setFocus()

                self.lanca_descricao_tempo_mao_de_obra(codigo_produto)
                self.lanca_descricao_custo_servico(codigo_produto)

                self.lanca_estrutura()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpa_dados_produto_estrutura(self):
        try:
            self.line_Descricao_Estrut.clear()
            self.line_Tipo_Estrut.clear()
            self.line_Referencia_Estrut.clear()
            self.line_NCM_Estrut.clear()
            self.line_UM_Estrut.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpa_dados_mao_de_obra_servico(self):
        try:
            self.line_Descricao_Mao.clear()
            self.line_Tempo_Mao.clear()

            self.line_Descricao_Servico.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpa_dados_manu(self):
        try:
            self.line_Codigo_Manu.clear()
            self.line_Descricao_Manu.clear()
            self.line_DescrCompl_Manu.clear()
            self.line_Referencia_Manu.clear()
            self.line_UM_Manu.clear()
            self.line_NCM_Manu.clear()
            self.line_Qtde_Manu.clear()
            self.line_Medida_Manu.clear()
            self.check_Converte_Manu.setChecked(False)
            self.line_Codigo_Manu.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpa_tudo(self):
        limpa_tabela(self.table_Estrutura)
        self.limpa_dados_produto_estrutura()
        self.limpa_dados_mao_de_obra_servico()
        self.line_Obs.clear()

    def lanca_estrutura(self):
        try:
            nova_tabela = []
            codigo_produto = self.line_Codigo_Estrut.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, codigo FROM produto where codigo = {codigo_produto};")
            select_prod = cursor.fetchall()
            idez, cod = select_prod[0]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT mat.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, "
                           f"conj.conjunto, prod.unidade, (mat.quantidade * 1) as qtde, "
                           f"COALESCE(prod.ncm, '') as ncm "
                           f"from materiaprima as mat "
                           f"INNER JOIN produto prod ON mat.codigo = prod.codigo "
                           f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                           f"where mat.mestre = {idez} order by conj.conjunto DESC, prod.descricao ASC;")
            tabela_estrutura = cursor.fetchall()

            if tabela_estrutura:
                for i in tabela_estrutura:
                    cod, descr, ref, conjunto, um, qtde, ncm = i

                    qtde_float = float(qtde)

                    dados = (cod, descr, ref, um, qtde_float, ncm, conjunto)
                    nova_tabela.append(dados)

            if nova_tabela:
                lanca_tabela(self.table_Estrutura, nova_tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_descricao_tempo_mao_de_obra(self, codigo):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT etapas, tempo FROM produto WHERE codigo = {codigo};")
            dados_produto = cursor.fetchall()
            if dados_produto:
                for i in dados_produto:
                    etapas, tempo = i

                    if etapas:
                        self.line_Descricao_Mao.setText(etapas)
                    if tempo:
                        self.line_Tempo_Mao.setText(str(tempo))

                self.mascara_tempo_mao_de_obra()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def mascara_tempo_mao_de_obra(self):
        try:
            tempo_mao = self.line_Tempo_Mao.text()

            if tempo_mao:
                tempo_mao_sem_espacos = tempo_mao.strip()
                if "." in tempo_mao_sem_espacos:
                    string_com_virgula = tempo_mao_sem_espacos.replace('.', ',')
                elif tempo_mao_sem_espacos.startswith(','):
                    string_com_virgula = '0' + tempo_mao_sem_espacos
                else:
                    string_com_virgula = tempo_mao_sem_espacos

                self.line_Tempo_Mao.setText(string_com_virgula)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_descricao_custo_servico(self, codigo):
        try:
            cursor = conecta.cursor()
            cursor.execute(f"SELECT terceirizadoobs, terceirizado FROM produto WHERE codigo = {codigo};")
            dados_produto = cursor.fetchall()
            if dados_produto:
                for i in dados_produto:
                    descr_servico, custo = i

                    if descr_servico:
                        self.line_Descricao_Servico.setText(descr_servico)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_line_codigo_manual(self):
        if not self.processando:
            try:
                self.processando = True

                codigo_produto = self.line_Codigo_Manu.text()
                codigo_pai = self.line_Codigo_Estrut.text()

                if not codigo_produto:
                    self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                    self.line_Codigo_Manu.clear()
                elif int(codigo_produto) == 0:
                    self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                    self.line_Codigo_Manu.clear()
                elif codigo_pai == codigo_produto:
                    self.mensagem_alerta('O campo "Código" não pode ser igual ao código da estrutura!')
                    self.line_Codigo_Manu.clear()
                else:
                    self.verifica_sql_produto_manual()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
                grava_erro_banco(nome_funcao, e, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_sql_produto_manual(self):
        try:
            codigo_produto = self.line_Codigo_Manu.text()
            cursor = conecta.cursor()
            cursor.execute(f"SELECT descricao, COALESCE(obs, ' ') as obs, unidade, localizacao, quantidade "
                           f"FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cursor.fetchall()
            if not detalhes_produto:
                self.mensagem_alerta('Este código de produto não existe!')
                self.line_Codigo_Manu.clear()
            else:
                self.lanca_dados_produto_manual()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def lanca_dados_produto_manual(self):
        try:
            codigo_produto = self.line_Codigo_Manu.text()
            cur = conecta.cursor()
            cur.execute(f"SELECT descricao, COALESCE(descricaocomplementar, '') as compl, "
                        f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                        f"quantidade, embalagem, kilosmetro "
                        f"FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()
            descr, compl, ref, um, ncm, qtde, embalagem, kg_mt = detalhes_produto[0]

            self.line_Descricao_Manu.setText(descr)
            self.line_DescrCompl_Manu.setText(compl)
            self.line_Referencia_Manu.setText(ref)
            self.line_NCM_Manu.setText(ncm)
            self.line_UM_Manu.setText(um)

            if kg_mt == 0:
                kg_mt_string = ''
            else:
                kg_mt_string = str(kg_mt)
            self.line_Kg_Manu.setText(kg_mt_string)

            if um == "KG":
                self.check_Converte_Manu.setChecked(True)
                self.line_Medida_Manu.setFocus()
            else:
                self.check_Converte_Manu.setChecked(False)
                self.line_Qtde_Manu.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_line_medida_manual(self):
        if not self.processando:
            try:
                self.processando = True

                medida = self.line_Medida_Manu.text()

                if medida:
                    medida_float = valores_para_float(medida)

                    kg_mt = self.line_Kg_Manu.text()
                    if kg_mt:
                        kg_mt_float = valores_para_float(kg_mt)

                        qtde_peso = medida_float * (kg_mt_float/1000)
                        qtde_peso_2casas = ("%.2f" % qtde_peso)

                        qtde_final = valores_para_virgula(qtde_peso_2casas)

                        self.line_Qtde_Manu.setText(qtde_final)
                        self.line_Qtde_Manu.setFocus()
                    else:
                        self.mensagem_alerta('O cadastro do produto precisa ter a informação "KG/MT"!')
                        self.limpa_dados_manu()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
                grava_erro_banco(nome_funcao, e, self.nome_arquivo)

            finally:
                self.processando = False

    def verifica_line_qtde_manual(self):
        if not self.processando:
            try:
                self.processando = True

                qtdezinha = self.line_Qtde_Manu.text()

                if len(qtdezinha) == 0:
                    self.mensagem_alerta('O campo "Qtde:" não pode estar vazio')
                    self.line_Qtde_Manu.clear()
                    self.line_Qtde_Manu.setFocus()
                elif qtdezinha == "0":
                    self.mensagem_alerta('O campo "Qtde:" não pode ser "0"')
                    self.line_Qtde_Manu.clear()
                    self.line_Qtde_Manu.setFocus()
                else:
                    self.item_produto_manual()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
                grava_erro_banco(nome_funcao, e, self.nome_arquivo)

            finally:
                self.processando = False

    def item_produto_manual(self):
        try:
            cod = self.line_Codigo_Manu.text()

            qtde_manu = self.line_Qtde_Manu.text()
            if "," in qtde_manu:
                qtde_manu_com_ponto = qtde_manu.replace(',', '.')
                qtdezinha_float = float(qtde_manu_com_ponto)
            else:
                qtdezinha_float = float(qtde_manu)

            extrai_estrutura = extrair_tabela(self.table_Estrutura)

            ja_existe = False
            for itens in extrai_estrutura:
                cod_con = itens[0]
                if cod_con == cod:
                    ja_existe = True
                    break

            if not ja_existe:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, "
                               f"COALESCE(prod.ncm, '') as ncm, conj.conjunto, "
                               f"prod.unidade "
                               f"FROM produto as prod "
                               f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                               f"where codigo = {cod};")
                detalhes_produto = cursor.fetchall()
                cod, descr, ref, ncm, conjunto, um = detalhes_produto[0]

                dados1 = [cod, descr, ref, um, qtdezinha_float, ncm, conjunto]
                extrai_estrutura.append(dados1)

                if extrai_estrutura:
                    lanca_tabela(self.table_Estrutura, extrai_estrutura)

            else:
                self.mensagem_alerta("Este produto já foi adicionado a estrutura!")

            self.limpa_dados_manu()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpar(self):
        self.limpa_tudo()
        self.line_Codigo_Estrut.clear()
        self.line_Codigo_Estrut.setFocus()

    def verifica_salvamento(self):
        try:
            codigo_produto = self.line_Codigo_Estrut.text()

            if not codigo_produto:
                self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                self.limpa_dados_produto_estrutura()
                limpa_tabela(self.table_Estrutura)
            elif int(codigo_produto) == 0:
                self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                self.limpa_dados_produto_estrutura()
                limpa_tabela(self.table_Estrutura)
            else:
                extrai_tabela = extrair_tabela(self.table_Estrutura)
                if not extrai_tabela:
                    if self.pergunta_confirmacao(f'A tabela "Estrutura" está vazia! Deseja mesmo continuar?'):
                        self.define_dados_salvamento(extrai_tabela)
                else:
                    tipo_material = self.line_Tipo_Estrut.text()

                    if tipo_material == "INDUSTRIALIZACAO":
                        descr_servico = self.line_Descricao_Servico.text()

                        if not descr_servico:
                            self.mensagem_alerta('O campo "Descrição do Serviço" não pode estar vazio!')
                        else:
                            self.define_dados_salvamento(extrai_tabela)
                    else:
                        descr_mao = self.line_Descricao_Mao.text()
                        tempo = self.line_Tempo_Mao.text()

                        if not descr_mao or not tempo:
                            self.mensagem_alerta('Os campos "Descrição e Tempo de Serviço" não podem estar vazio!')
                        else:
                            self.define_dados_salvamento(extrai_tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_ops_consumidas(self):
        try:
            nome_tabela = self.table_Estrutura
            cod_pai = self.line_Codigo_Estrut.text()
            print(cod_pai)

            dados_prod = self.tab_prod.consulta_por_codigo(cod_pai)
            id_pai = dados_prod[0][0]

            extrai_recomendados = extrair_tabela(nome_tabela)
            if not extrai_recomendados:
                self.mensagem_alerta(f'A tabela "Estrutura" está vazia!')
            else:
                linha_selecao = nome_tabela.currentRow()
                if linha_selecao >= 0:
                    dados_linha = []
                    for coluna in range(nome_tabela.columnCount()):
                        item = nome_tabela.item(linha_selecao, coluna)
                        dados_linha.append(item.text() if item else "")
                    cod_filho = dados_linha[0]

                    if id_pai:
                        cursor = conecta.cursor()
                        cursor.execute(f"select ordser.datainicial, ordser.dataprevisao, ordser.numero, prod.id, "
                                       f"prod.descricao, "
                                       f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                                       f"ordser.quantidade "
                                       f"from ordemservico as ordser "
                                       f"INNER JOIN produto prod ON ordser.produto = prod.id "
                                       f"where ordser.status = 'A' AND prod.id = {id_pai} "
                                       f"order by ordser.numero;")
                        op_abertas = cursor.fetchall()

                        if op_abertas:
                            for i in op_abertas:
                                num_op = i[2]
                                id_produto = i[3]

                                cursor = conecta.cursor()
                                cursor.execute(f"SELECT mat.id, prod.codigo, prod.descricao, "
                                               f"COALESCE(prod.obs, '') as obs, prod.unidade, "
                                               f"((SELECT quantidade FROM ordemservico where numero = {num_op}) * "
                                               f"(mat.quantidade)) AS Qtde, "
                                               f"COALESCE(prod.localizacao, ''), prod.quantidade "
                                               f"FROM materiaprima as mat "
                                               f"INNER JOIN produto as prod ON mat.produto = prod.id "
                                               f"where mat.mestre = {id_produto} and prod.codigo = {cod_filho} "
                                               f"ORDER BY prod.descricao;")
                                select_estrut = cursor.fetchall()
                                if select_estrut:
                                    for dados_estrut in select_estrut:
                                        id_mat_e, cod_e, descr_e, ref_e, um_e, qtde_e, local_e, saldo_e = dados_estrut

                                        cursor = conecta.cursor()
                                        cursor.execute(f"SELECT max(mat.id), max(prod.codigo), max(prod.descricao), "
                                                       f"sum(p_op.qtde_materia)as total "
                                                       f"FROM materiaprima as mat "
                                                       f"INNER JOIN produto as prod ON mat.produto = prod.id "
                                                       f"INNER JOIN produtoos as p_op ON mat.id = p_op.id_materia "
                                                       f"where mat.mestre = {id_produto} "
                                                       f"and p_op.numero = {num_op} and mat.id = {id_mat_e} "
                                                       f"group by p_op.id_materia;")
                                        select_os_resumo = cursor.fetchall()

                                        if not select_os_resumo:
                                            nome_tabela.removeRow(linha_selecao)
                                        else:
                                            self.mensagem_alerta(f"O produto {cod_filho} está sendo consumido em OP "
                                                                 f"e não pode ser excluído!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def define_dados_salvamento(self, extrai_tabela):
        try:
            codigo_produto = self.line_Codigo_Estrut.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT id, codigo FROM produto where codigo = {codigo_produto};")
            select_prod = cursor.fetchall()
            idez, cod = select_prod[0]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT mat.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, "
                           f"conj.conjunto, prod.unidade, (mat.quantidade * 1) as qtde, "
                           f"COALESCE(prod.ncm, '') as ncm "
                           f"from materiaprima as mat "
                           f"INNER JOIN produto prod ON mat.codigo = prod.codigo "
                           f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                           f"where mat.mestre = {idez} order by conj.conjunto DESC, prod.descricao ASC;")
            tabela_estrutura = cursor.fetchall()

            reg_atualizados = []
            reg_a_excluir = []
            reg_a_inserir = []

            for itens_estrut in tabela_estrutura:
                cod_estrut = itens_estrut[0]
                qtde_estrut = float(itens_estrut[5])

                registro_correspondente = next((item for item in extrai_tabela if item[0] == cod_estrut),
                                               None)

                if registro_correspondente:
                    qtde_nova = float(registro_correspondente[4])

                    if qtde_estrut != qtde_nova:
                        reg_atualizados.append((cod_estrut, qtde_nova))
                else:
                    reg_a_excluir.append(cod_estrut)

            for itens_tab in extrai_tabela:
                cod_tabela = itens_tab[0]
                if cod_tabela not in [item[0] for item in tabela_estrutura]:
                    reg_a_inserir.append((cod_tabela, float(itens_tab[4])))

            cursor = conecta.cursor()
            cursor.execute(f"SELECT numero, datainicial, status, produto, quantidade "
                           f"FROM ordemservico where codigo = {codigo_produto} and status = 'B';")
            extrair_dados = cursor.fetchall()
            if not extrair_dados:
                self.salvar_dados_com_produtos(idez, reg_a_inserir, reg_atualizados, reg_a_excluir)
            else:
                descr = self.line_Descricao_Estrut.text()

                if reg_a_inserir or reg_atualizados or reg_a_excluir:
                    self.mensagem_alerta(f'O produto {descr}\ntem ordens de produção (OP) encerradas e a '
                                         f'estrutura não pode ser editada!')
                self.salvar_dados_sem_produtos(idez)

                self.limpa_tudo()
                self.line_Codigo_Estrut.clear()
                self.line_Obs.clear()
                self.line_Codigo_Estrut.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_dados_com_produtos(self, mestre, insert, update, delete):
        try:
            descr = self.line_Descricao_Estrut.text()

            if insert:
                for item_insert in insert:
                    cod_ins = item_insert[0]
                    qtde_ins = item_insert[1]

                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT id, codigo FROM produto where codigo = {cod_ins};")
                    select_prod = cursor.fetchall()
                    idez_ins, cod = select_prod[0]

                    cursor = conecta.cursor()
                    cursor.execute(f"Insert into materiaprima "
                                   f"(ID, MESTRE, QUANTIDADE, PRODUTO, CODIGO) "
                                   f"values (GEN_ID(GEN_MATERIAPRIMA_ID,1), "
                                   f"{mestre}, {qtde_ins}, {idez_ins}, {cod_ins});")
                    conecta.commit()

            if update:
                for item_update in update:
                    cod_up = item_update[0]
                    qtde_up = item_update[1]

                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE materiaprima SET quantidade = '{qtde_up}' "
                                   f"where mestre = {mestre} and codigo = {cod_up};")
                    conecta.commit()

            if delete:
                for cod_delete in delete:
                    cursor = conecta.cursor()
                    cursor.execute(f"DELETE FROM materiaprima where mestre = {mestre} and codigo = {cod_delete};")
                    conecta.commit()

            tipo_material = self.line_Tipo_Estrut.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT terceirizadoobs, etapas, tempo, obs2 FROM produto where id = {mestre};")
            selects = cursor.fetchall()
            terc_servico, etapa_mao, tempo_mao, obs_banco = selects[0]

            tips_mat = 0
            if tipo_material == "INDUSTRIALIZACAO":
                descr_servico = self.line_Descricao_Servico.text().upper()

                if terc_servico != descr_servico:
                    tips_mat += 1

                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE produto SET terceirizadoobs = '{descr_servico}' "
                                   f"where id = {mestre};")
                    conecta.commit()

            else:
                descr_mao = self.line_Descricao_Mao.text().upper()
                tempo = self.line_Tempo_Mao.text()
                tempo_float = valores_para_float(tempo)

                if etapa_mao != descr_mao or float(tempo_mao) != tempo_float:
                    tips_mat += 1

                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE produto SET etapas = '{descr_mao}', tempo = '{tempo_float}' "
                                   f"where id = {mestre};")
                    conecta.commit()

            obis = 0
            obs = self.line_Obs.text().upper()
            if obs_banco != obs:
                obis += 1
                cursor = conecta.cursor()
                cursor.execute(f"UPDATE produto SET obs2 = '{obs}' "
                               f"where id = {mestre};")
                conecta.commit()

            if insert or update or delete or tips_mat or obis:
                self.mensagem_alerta(f"Estrutura do produto {descr} salvo com Sucesso!!")

                self.limpa_tudo()
                self.line_Codigo_Estrut.clear()
                self.line_Obs.clear()
                self.line_Codigo_Estrut.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_dados_sem_produtos(self, mestre):
        try:
            descr = self.line_Descricao_Estrut.text()

            tipo_material = self.line_Tipo_Estrut.text()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT terceirizadoobs, etapas, tempo, obs2 FROM produto where id = {mestre};")
            selects = cursor.fetchall()
            terc_servico, etapa_mao, tempo_mao, obs_banco = selects[0]

            tips_mat = 0
            if tipo_material == "INDUSTRIALIZACAO":
                descr_servico = self.line_Descricao_Servico.text().upper()

                if terc_servico != descr_servico:
                    tips_mat += 1

                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE produto SET terceirizadoobs = '{descr_servico}' "
                                   f"where id = {mestre};")
                    conecta.commit()

            else:
                descr_mao = self.line_Descricao_Mao.text().upper()
                tempo = self.line_Tempo_Mao.text()
                tempo_float = valores_para_float(tempo)

                if etapa_mao != descr_mao or float(tempo_mao) != tempo_float:
                    tips_mat += 1

                    cursor = conecta.cursor()
                    cursor.execute(f"UPDATE produto SET etapas = '{descr_mao}', tempo = '{tempo_float}' "
                                   f"where id = {mestre};")
                    conecta.commit()

            obis = 0
            obs = self.line_Obs.text().upper()
            if obs_banco != obs:
                obis += 1
                cursor = conecta.cursor()
                cursor.execute(f"UPDATE produto SET obs2 = '{obs}' "
                               f"where id = {mestre};")
                conecta.commit()

            if tips_mat or obis:
                self.mensagem_alerta(f"Cadastro do produto {descr} foi atualizado com Sucesso!!")

                self.limpa_tudo()
                self.line_Codigo_Estrut.clear()
                self.line_Obs.clear()
                self.line_Codigo_Estrut.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo)
            grava_erro_banco(nome_funcao, e, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaEstruturaIncluir()
    tela.show()
    qt.exec_()
