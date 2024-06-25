import sys
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, pergunta_confirmacao, \
    tratar_notificar_erros
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, limpa_tabela, layout_cabec_tab, excluir_item_tab
from comandos.comando_lines import validador_decimal, definir_data_atual
from comandos.comando_string import remover_acentos
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_banco import definir_proximo_generator
from forms.tela_pre_incluir import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import inspect
import os


class TelaPreIncluir(QMainWindow, Ui_MainWindow):
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

        self.line_Fornecedor.editingFinished.connect(self.manual_verifica_pelo_line)

        self.btn_Adicionar.clicked.connect(self.manual_verifica_line_codigo)
        self.btn_Salvar.clicked.connect(self.salvar_verifica_salvamento)
        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_ExcluirTudo.clicked.connect(partial(limpa_tabela, self.table_Produto))
        self.btn_ExcluirItem.clicked.connect(partial(excluir_item_tab, self.table_Produto, "Lista de Produtos"))

        validador_decimal(self.line_NCM, 9999999.000)

        definir_proximo_generator(self.line_Registro, "PRODUTOPRELIMINAR")
        definir_data_atual(self.date_Emissao)

        self.line_Obs.setFocus()

        self.processando = False

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
            cor_fonte(self.label_2)
            cor_fonte(self.label_26)
            cor_fonte(self.label_3)
            cor_fonte(self.label_4)
            cor_fonte(self.label_40)
            cor_fonte(self.label_5)
            cor_fonte(self.label_50)
            cor_fonte(self.label_59)
            cor_fonte(self.label_6)
            cor_fonte(self.label_63)
            cor_fonte(self.label_64)
            cor_fonte(self.label_68)
            cor_fonte(self.label_69)
            cor_fonte(self.label_71)
            cor_fonte(self.label_8)
            cor_fonte(self.label_9)
            cor_fonte(self.label_Titulo)

            cor_btn(self.btn_Salvar)
            cor_btn(self.btn_Adicionar)
            cor_btn(self.btn_ExcluirTudo)
            cor_btn(self.btn_ExcluirItem)
            cor_btn(self.btn_Limpar)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def layout_tabela(self, nome_tabela):
        try:
            layout_cabec_tab(nome_tabela)

            nome_tabela.setColumnWidth(0, 210)
            nome_tabela.setColumnWidth(1, 210)
            nome_tabela.setColumnWidth(2, 100)
            nome_tabela.setColumnWidth(3, 30)
            nome_tabela.setColumnWidth(4, 80)
            nome_tabela.setColumnWidth(5, 55)
            nome_tabela.setColumnWidth(6, 150)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_pelo_line(self):
        if not self.processando:
            try:
                self.processando = True

                self.manual_verifica_line_codigo()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

            finally:
                self.processando = False

    def manual_verifica_line_codigo(self):
        try:
            obs = self.line_Obs.text()
            descr = self.line_Descricao.text()
            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            if not obs:
                mensagem_alerta('O campo "Obs" não pode estar vazio!')
                self.line_Obs.clear()
            elif not descr:
                mensagem_alerta('O campo "Descrição" não pode estar vazio!')
                self.line_Descricao.clear()
            elif not ncm:
                mensagem_alerta('O campo "NCM" não pode estar vazio!')
                self.line_NCM.clear()
            elif not um:
                mensagem_alerta('O campo "UM" não pode estar vazio!')
                self.combo_UM.setCurrentText("")
            else:
                self.manual_verifica_descricao_preposicoes()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_descricao_preposicoes(self):
        try:
            descr = self.line_Descricao.text().upper()

            if "BANDEIJA" in descr:
                mensagem_alerta('A PALAVRA BANDEJA NÃO TEM "I"!')

            elif "TRAZEIRA" in descr:
                mensagem_alerta('A PALAVRA TRASEIRA É COM "S"!')

            elif "ESTERIA" in descr:
                mensagem_alerta('VERIFIQUE A PALAVRA "ESTERIA"!')

            elif "TRAZEIRO" in descr:
                mensagem_alerta('A PALAVRA TRASEIRO É COM "S"!')

            elif " DE " in descr \
                    or " DO " in descr \
                    or " DA " in descr \
                    or " PARA " in descr \
                    or " DE " in descr \
                    or " COM " in descr:
                msg = 'Não podemos utilizar preposições (da, do, em, com, etc..) em nossos cadastros.\n' \
                      'Tem certeza que deseja continuar?'
                if pergunta_confirmacao(msg):
                    self.manual_verifica_descricao_no_banco()
            else:
                self.manual_verifica_descricao_no_banco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_descricao_no_banco(self):
        try:
            descr = self.line_Descricao.text().upper()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT codigo, descricao FROM produto where descricao = '{descr}';")
            produto_descr = cursor.fetchall()

            cursor = conecta.cursor()
            cursor.execute(f"SELECT registro, descricao FROM PRODUTOPRELIMINAR where descricao = '{descr}';")
            produto_pre_descr = cursor.fetchall()

            if produto_descr:
                codis = produto_descr[0][0]
                mensagem_alerta(f'Já existe produtos cadastrados com esta descrição"\n\n'
                                f' - Código do Produto: {codis}')
            elif produto_pre_descr:
                codis_pre = produto_pre_descr[0][0]
                mensagem_alerta(f'Já existe produtos no pré cadastrado com esta descrição"\n\n'
                                f' - Código do Registro: {codis_pre}')
            else:
                self.manual_verifica_referencia_no_banco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_referencia_no_banco(self):
        try:
            ref = self.line_Referencia.text()

            if ref:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT codigo, descricao FROM produto where obs = '{ref}';")
                produto_ref = cursor.fetchall()

                cursor = conecta.cursor()
                cursor.execute(f"SELECT registro, descricao FROM PRODUTOPRELIMINAR where referencia = '{ref}';")
                produto_pre_ref = cursor.fetchall()

                if produto_ref:
                    codis = produto_ref[0][0]
                    mensagem_alerta(f'Já existe produtos cadastrados com esta referência"\n\n'
                                    f' - Código do Produto: {codis}')
                elif produto_pre_ref:
                    codis_pre = produto_pre_ref[0][0]
                    mensagem_alerta(f'Já existe produtos no pré cadastrado com esta referência"\n\n'
                                    f' - Código do Registro: {codis_pre}')
                else:
                    self.manual_verifica_2espacos_branco()
            else:
                self.manual_verifica_2espacos_branco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_2espacos_branco(self):
        try:
            descr = self.line_Descricao.text()
            ref = self.line_Referencia.text()
            compl = self.line_DescrCompl.text()

            if descr.count('  ') == 1:
                mensagem_alerta("Dois espaços encontrados em 'Descrição'")

            elif ref.count('  ') == 1:
                mensagem_alerta("Dois espaços encontrados em 'Referência'")

            elif compl.count('  ') == 1:
                mensagem_alerta("Dois espaços encontrados em 'D. Compl.'")
            else:
                self.manual_verifica_unidade_kg()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_verifica_unidade_kg(self):
        try:
            um = self.combo_UM.currentText()

            if um == "KG":
                kg_mt = self.line_kg_mt.text()
                if not kg_mt:
                    mensagem_alerta('O campo "KG/MT" não pode estar vazio quando a unidade de medida for "KG"!')
                else:
                    self.manual_manipula_produto()
            else:
                self.manual_manipula_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manual_manipula_produto(self):
        try:
            descr = self.line_Descricao.text().upper()
            descr_certo = remover_acentos(descr)

            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            ref = self.line_Referencia.text()

            descr_compl = self.line_DescrCompl.text()
            if descr_compl:
                descr_c_certo = remover_acentos(descr_compl.upper())
            else:
                descr_c_certo = ""

            kg_mt = self.line_kg_mt.text()
            fornecedor = self.line_Fornecedor.text()

            extrai_estrutura = extrair_tabela(self.table_Produto)

            ja_existe = False
            for itens in extrai_estrutura:
                descr_con = itens[0]
                ref_con = itens[2]
                if descr_con == descr_c_certo or ref_con == ref:
                    ja_existe = True
                    break

            if not ja_existe:
                dados1 = [descr_certo, descr_c_certo, ref, um, ncm, kg_mt, fornecedor]
                extrai_estrutura.append(dados1)

                if extrai_estrutura:
                    lanca_tabela(self.table_Produto, extrai_estrutura, largura_auto=False)

            else:
                mensagem_alerta("Este produto já foi adicionado a tabela!")

            self.line_Descricao.setFocus()

            self.limpa_dados_manual()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def limpa_dados_manual(self):
        try:
            self.line_Descricao.clear()
            self.line_NCM.clear()
            self.combo_UM.setCurrentText("")

            self.line_Referencia.clear()
            self.line_DescrCompl.clear()
            self.line_kg_mt.clear()
            self.line_Fornecedor.clear()
            definir_data_atual(self.date_Emissao)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def limpa_tudo(self):
        self.limpa_dados_manual()
        self.line_Obs.clear()
        limpa_tabela(self.table_Produto)
        definir_data_atual(self.date_Emissao)
        self.line_Obs.setFocus()

    def salvar_verifica_salvamento(self):
        try:
            extrai_pedido = extrair_tabela(self.table_Produto)
            obs = self.line_Obs.text()

            if not extrai_pedido:
                mensagem_alerta(f'A tabela "Lista de Produtos" está vazia!')
            elif not obs:
                mensagem_alerta('O campo "Obs" não pode estar vazio!')
            else:
                self.salvar_produtos()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def salvar_produtos(self):
        try:
            registro = int(self.line_Registro.text())
            obs = self.line_Obs.text().upper()

            extrai_produtos = extrair_tabela(self.table_Produto)

            for itens in extrai_produtos:
                descr, decr_compl, ref, um, ncm, kg_mt, fornecedor = itens

                if kg_mt:
                    if "," in kg_mt:
                        qtdezinha_com_ponto = kg_mt.replace(',', '.')
                        qtdezinha_float = float(qtdezinha_com_ponto)
                    else:
                        qtdezinha_float = float(kg_mt)
                else:
                    qtdezinha_float = 0.00

                cursor = conecta.cursor()
                cursor.execute(f"Insert into PRODUTOPRELIMINAR (ID, REGISTRO, OBS, DESCRICAO, DESCR_COMPL, "
                               f"REFERENCIA, UM, NCM, KG_MT, FORNECEDOR) "
                               f"values (GEN_ID(GEN_PRODUTOPRELIMINAR_ID,1), {registro}, '{obs}', '{descr}', "
                               f"'{decr_compl}', '{ref}', '{um}', '{ncm}', {qtdezinha_float}, '{fornecedor}');")

            conecta.commit()

            mensagem_alerta(f'O Registro de Produtos Nº {registro} foi criada com Sucesso!')
            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPreIncluir()
    tela.show()
    qt.exec_()