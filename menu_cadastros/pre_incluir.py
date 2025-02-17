import sys
from banco_dados.conexao import conecta
from forms.tela_pre_incluir import *
from banco_dados.controle_erros import grava_erro_banco
from banco_dados.bc_consultas import definir_proximo_generator
from comandos.tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab
from comandos.lines import validador_decimal, definir_data_atual
from comandos.telas import tamanho_aplicacao, icone
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import traceback
from unidecode import unidecode


class TelaPreIncluir(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_cadastro.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Produto)

        self.line_Fornecedor.editingFinished.connect(self.manual_verifica_pelo_line)

        self.btn_Adicionar.clicked.connect(self.manual_verifica_line_codigo)
        self.btn_Salvar.clicked.connect(self.salvar_verifica_salvamento)
        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_ExcluirTudo.clicked.connect(self.limpa_tabela)
        self.btn_ExcluirItem.clicked.connect(self.excluir_item_tab)

        validador_decimal(self.line_NCM, 9999999.000)

        definir_proximo_generator(self.line_Registro, "PRODUTOPRELIMINAR")
        definir_data_atual(self.date_Emissao)

        self.line_Obs.setFocus()

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

    def limpa_tabela(self):
        try:
            nome_tabela = self.table_Produto

            nome_tabela.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_item_tab(self):
        try:
            nome_tabela = self.table_Produto

            extrai_recomendados = extrair_tabela(nome_tabela)
            if not extrai_recomendados:
                self.mensagem_alerta(f'A tabela "Lista de Produtos" está vazia!')
            else:
                linha_selecao = nome_tabela.currentRow()
                if linha_selecao >= 0:
                    nome_tabela.removeRow(linha_selecao)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manual_verifica_pelo_line(self):
        if not self.processando:
            try:
                self.processando = True

                self.manual_verifica_line_codigo()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def manual_verifica_line_codigo(self):
        try:
            obs = self.line_Obs.text()
            descr = self.line_Descricao.text()
            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            if not obs:
                self.mensagem_alerta('O campo "Obs" não pode estar vazio!')
                self.line_Obs.clear()
            elif not descr:
                self.mensagem_alerta('O campo "Descrição" não pode estar vazio!')
                self.line_Descricao.clear()
            elif not ncm:
                self.mensagem_alerta('O campo "NCM" não pode estar vazio!')
                self.line_NCM.clear()
            elif not um:
                self.mensagem_alerta('O campo "UM" não pode estar vazio!')
                self.combo_UM.setCurrentText("")
            else:
                self.manual_verifica_descricao_preposicoes()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manual_verifica_descricao_preposicoes(self):
        try:
            descr = self.line_Descricao.text().upper()

            if "BANDEIJA" in descr:
                self.mensagem_alerta('A PALAVRA BANDEJA NÃO TEM "I"!')

            elif "TRAZEIRA" in descr:
                self.mensagem_alerta('A PALAVRA TRASEIRA É COM "S"!')

            elif "ESTERIA" in descr:
                self.mensagem_alerta('VERIFIQUE A PALAVRA "ESTERIA"!')

            elif "TRAZEIRO" in descr:
                self.mensagem_alerta('A PALAVRA TRASEIRO É COM "S"!')

            elif " DE " in descr \
                    or " DO " in descr \
                    or " DA " in descr \
                    or " PARA " in descr \
                    or " DE " in descr \
                    or " COM " in descr:
                msg = 'Não podemos utilizar preposições (da, do, em, com, etc..) em nossos cadastros.\n' \
                      'Tem certeza que deseja continuar?'
                if self.pergunta_confirmacao(msg):
                    self.manual_verifica_descricao_no_banco()
            else:
                self.manual_verifica_descricao_no_banco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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
                self.mensagem_alerta(f'Já existe produtos cadastrados com esta descrição"\n\n'
                                     f' - Código do Produto: {codis}')
            elif produto_pre_descr:
                codis_pre = produto_pre_descr[0][0]
                self.mensagem_alerta(f'Já existe produtos no pré cadastrado com esta descrição"\n\n'
                                     f' - Código do Registro: {codis_pre}')
            else:
                self.manual_verifica_referencia_no_banco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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
                    self.mensagem_alerta(f'Já existe produtos cadastrados com esta referência"\n\n'
                                         f' - Código do Produto: {codis}')
                elif produto_pre_ref:
                    codis_pre = produto_pre_ref[0][0]
                    self.mensagem_alerta(f'Já existe produtos no pré cadastrado com esta referência"\n\n'
                                         f' - Código do Registro: {codis_pre}')
                else:
                    self.manual_verifica_2espacos_branco()
            else:
                self.manual_verifica_2espacos_branco()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manual_verifica_2espacos_branco(self):
        try:
            descr = self.line_Descricao.text()
            ref = self.line_Referencia.text()
            compl = self.line_DescrCompl.text()

            if descr.count('  ') == 1:
                self.mensagem_alerta("Dois espaços encontrados em 'Descrição'")

            elif ref.count('  ') == 1:
                self.mensagem_alerta("Dois espaços encontrados em 'Referência'")

            elif compl.count('  ') == 1:
                self.mensagem_alerta("Dois espaços encontrados em 'D. Compl.'")
            else:
                self.manual_verifica_unidade_kg()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manual_verifica_unidade_kg(self):
        try:
            um = self.combo_UM.currentText()

            if um == "KG":
                kg_mt = self.line_kg_mt.text()
                if not kg_mt:
                    self.mensagem_alerta('O campo "KG/MT" não pode estar vazio quando a unidade de medida for "KG"!')
                else:
                    self.manual_manipula_produto()
            else:
                self.manual_manipula_produto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manual_manipula_produto(self):
        try:
            descr = self.line_Descricao.text().upper()
            descr_certo = unidecode(descr)

            ncm = self.line_NCM.text()
            um = self.combo_UM.currentText()

            ref = self.line_Referencia.text()

            descr_compl = self.line_DescrCompl.text()
            if descr_compl:
                descr_c_certo = unidecode(descr_compl.upper())
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
                self.mensagem_alerta("Este produto já foi adicionado a tabela!")

            self.line_Descricao.setFocus()

            self.limpa_dados_manual()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tudo(self):
        self.limpa_dados_manual()
        self.line_Obs.clear()
        self.limpa_tabela()
        definir_data_atual(self.date_Emissao)
        self.line_Obs.setFocus()

    def salvar_verifica_salvamento(self):
        try:
            extrai_pedido = extrair_tabela(self.table_Produto)
            obs = self.line_Obs.text()

            if not extrai_pedido:
                self.mensagem_alerta(f'A tabela "Lista de Produtos" está vazia!')
            elif not obs:
                self.mensagem_alerta('O campo "Obs" não pode estar vazio!')
            else:
                self.salvar_produtos()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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
                sql = """
                INSERT INTO PRODUTOPRELIMINAR (ID, REGISTRO, OBS, DESCRICAO, DESCR_COMPL, 
                REFERENCIA, UM, NCM, KG_MT, FORNECEDOR) 
                VALUES (GEN_ID(GEN_PRODUTOPRELIMINAR_ID,1), ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """

                cursor.execute(sql, (registro, obs, descr, decr_compl, ref, um, ncm, qtdezinha_float, fornecedor))

            conecta.commit()

            self.mensagem_alerta(f'O Registro de Produtos Nº {registro} foi criada com Sucesso!')
            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPreIncluir()
    tela.show()
    qt.exec_()
