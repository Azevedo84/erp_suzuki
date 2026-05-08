import sys
from banco_dados.conexao import conecta, conecta_engenharia
from forms.tela_eng_projeto_incluir import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.telas import tamanho_aplicacao, icone
from comandos.lines import validador_decimal, definir_data_atual
from comandos.tabelas import layout_cabec_tab, extrair_tabela, lanca_tabela
from comandos.inventor import padrao_desenho
from comandos.conversores import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from arquivos.chamar_arquivos import definir_caminho_arquivo
import inspect
import os
import traceback
from datetime import date, datetime, timedelta
import socket


class TelaEngenhariaProjeto(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu.png")
        tamanho_aplicacao(self)

        layout_cabec_tab(self.table_Projetos)

        validador_decimal(self.line_Qtde)

        self.table_Projetos.viewport().installEventFilter(self)

        caminho = os.path.join('..', 'arquivos', 'icones', 'lupa.png')
        caminho_arquivo = definir_caminho_arquivo(caminho)
        icon = QIcon(caminho_arquivo)
        self.btn_Lupa.setIcon(icon)
        self.escolher_produto = []
        self.btn_Lupa.clicked.connect(self.abrir_tela_escolher_produto)

        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.btn_Excluir.clicked.connect(self.excluir_projeto)

        self.definir_num_projeto()

        definir_data_atual(self.date_Emissao)

        data_entrega = date.today() + timedelta(60)
        self.date_Entrega.setDate(data_entrega)

        self.line_Num_Desenho.editingFinished.connect(self.verifica_line_num_desenho)

        self.processando = False

        self.lanca_projetos_pendentes()

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

    def definir_num_projeto(self):
        try:
            cursor = conecta_engenharia.cursor()
            cursor.execute("select GEN_ID(GEN_PROJETO_ID,0) from rdb$database;")
            ultimo_id_req0 = cursor.fetchall()
            ultimo_id_req1 = ultimo_id_req0[0]
            ultimo_id_req2 = int(ultimo_id_req1[0]) + 1
            ultimo_id_req = str(ultimo_id_req2)
            self.line_Num_Projeto.setText(ultimo_id_req)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def abrir_tela_escolher_produto(self):
        from menu_engenharia.eng_localizar_projeto import TelaLocalizaProjeto

        texto_desenho = self.line_Num_Desenho.text()

        self.escolher_produto = TelaLocalizaProjeto(True, texto_desenho)
        self.escolher_produto.produto_escolhido.connect(self.atualizar_produto_entry)
        self.escolher_produto.show()

    def atualizar_produto_entry(self, id_arquivo):
        self.limpa_campos_selecionados()

        self.line_Cod_Arq.setText(id_arquivo)

        cursor = conecta_engenharia.cursor()
        cursor.execute("""
                                            SELECT NOME_BASE, TIPO_ARQUIVO
                                            FROM ARQUIVOS
                                            WHERE ID = ?
                                        """, (id_arquivo,))
        dados_arquivo = cursor.fetchall()
        if dados_arquivo:
            nome_base, tipo_arq = dados_arquivo[0]

            self.line_Num_Desenho.setText(nome_base)
            self.line_Tipo.setText(tipo_arq)

            descricao = self.consulta_propriedade_ipt_iam(id_arquivo, "DESCRIPTION")
            self.line_Descricao.setText(descricao)

            cod_erp = self.consulta_propriedade_ipt_iam(id_arquivo, "AUTHORITY")
            self.line_Cod_ERP.setText(cod_erp)

        self.line_Qtde.setFocus()

    def verifica_line_num_desenho(self):
        if not self.processando:
            try:
                self.processando = True

                texto_desenho = self.line_Num_Desenho.text()

                if texto_desenho:
                    self.limpa_campos_selecionados()

                    cursor = conecta_engenharia.cursor()
                    cursor.execute("""
                                    SELECT ID, NOME_BASE, TIPO_ARQUIVO
                                    FROM ARQUIVOS
                                    WHERE NOME_BASE = ? AND TIPO_ARQUIVO IN ('IPT', 'IAM')
                                """, (texto_desenho,))
                    dados_arquivo = cursor.fetchall()
                    if dados_arquivo:
                        id_arquivo, nome_base, tipo_arq = dados_arquivo[0]

                        self.line_Cod_Arq.setText(f"{id_arquivo}")
                        self.line_Num_Desenho.setText(nome_base)
                        self.line_Tipo.setText(tipo_arq)

                        descricao = self.consulta_propriedade_ipt_iam(id_arquivo, "DESCRIPTION")
                        self.line_Descricao.setText(descricao)

                        cod_erp = self.consulta_propriedade_ipt_iam(id_arquivo, "AUTHORITY")
                        self.line_Cod_ERP.setText(cod_erp)

                    self.line_Qtde.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

            finally:
                self.processando = False

    def limpa_campos_selecionados(self):
        try:
            self.line_Cod_Arq.clear()
            self.line_Descricao.clear()
            self.line_Cod_ERP.clear()
            self.line_Tipo.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def consulta_propriedade_ipt_iam(self, id_arquivo, propr):
        try:
            propriedade_escolhida = ""

            cursor_eng = conecta_engenharia.cursor()
            sql = f"""
                SELECT ipt.id_arquivo, ipt.{propr}
                FROM PROPRIEDADES_IPT ipt
                WHERE ipt.id_arquivo = ?
            """
            cursor_eng.execute(sql, (id_arquivo,))
            dados_ipt = cursor_eng.fetchall()
            if dados_ipt:
                for i in dados_ipt:
                    propriedade_escolhida = i[1].strip()

            sql = f"""
                SELECT iam.id_arquivo, iam.{propr}
                FROM PROPRIEDADES_IAM iam
                WHERE iam.id_arquivo = ?
            """
            cursor_eng.execute(sql, (id_arquivo,))
            dados_iam = cursor_eng.fetchall()

            if dados_iam:
                for ii in dados_iam:
                    propriedade_escolhida = ii[1].strip()

            return propriedade_escolhida

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, sources, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and event.buttons() == QtCore.Qt.LeftButton
                    and sources is self.table_Projetos.viewport()):
                item = self.table_Projetos.currentItem()

                if item:
                    dados_fornecedor = extrair_tabela(self.table_Projetos)

                    item_selecionado = dados_fornecedor[item.row()]
                    id_proj, emissao, num_des, caminho, qtde, cliente, solic, entrega, obs = item_selecionado

                    cursor = conecta_engenharia.cursor()
                    cursor.execute(f"SELECT id, emissao, ID_ARQUIVO, NUM_DESENHO, QTDE, ID_CLIENTE, SOLICITANTE, "
                                   f"PREVISAO_ENTREGA, OBS "
                                   f"FROM PROJETO "
                                   f"where id = {id_proj};")
                    dados_interno = cursor.fetchall()

                    if dados_interno:
                        id_projeto, emissaos, id_arquivo, num_des, qtde, id_cliente, solicitante, entregas, obs = dados_interno[0]

                        self.line_Num_Projeto.setText(f"{id_projeto}")

                        if qtde:
                            self.line_Qtde.setText(f"{qtde}")

                        if obs:
                            print("entrei", obs)
                            self.plain_Obs.setPlainText(f"{obs}")

                        if solicitante:
                            self.line_Solicitante.setText(f"{solicitante}")

                        self.date_Emissao.setDate(emissaos)
                        self.date_Entrega.setDate(entregas)


                        if id_cliente:
                            item_count = self.combo_Cliente.count()
                            for i in range(item_count):
                                item_text = self.combo_Cliente.itemText(i)
                                if item_text:
                                    clientetete = item_text.find(" - ")
                                    id_cli = int(item_text[:clientetete])

                                    if id_cliente == int(id_cli):
                                        self.combo_Cliente.setCurrentText(item_text)

                        if id_arquivo:
                            self.line_Cod_Arq.setText(f"{id_arquivo}")

                            cursor = conecta_engenharia.cursor()
                            cursor.execute("""
                                            SELECT NOME_BASE, TIPO_ARQUIVO
                                            FROM ARQUIVOS
                                            WHERE ID = ?
                                        """, (id_arquivo,))
                            dados_arquivo = cursor.fetchall()
                            if dados_arquivo:
                                nome_base, tipo_arq = dados_arquivo[0]

                                self.line_Num_Desenho.setText(nome_base)
                                self.line_Tipo.setText(tipo_arq)

                                descricao = self.consulta_propriedade_ipt_iam(id_arquivo, "DESCRIPTION")
                                self.line_Descricao.setText(descricao)

                                cod_erp = self.consulta_propriedade_ipt_iam(id_arquivo, "AUTHORITY")
                                self.line_Cod_ERP.setText(cod_erp)
                        else:
                            self.line_Num_Desenho.setText(num_des)

            return super(QMainWindow, self).eventFilter(sources, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_projetos_pendentes(self):
        try:
            nova_lista = []

            cursor = conecta_engenharia.cursor()
            cursor.execute(f"SELECT proj.id, "
                           f"EXTRACT(DAY FROM proj.EMISSAO) || '/' || "
                           f"EXTRACT(MONTH FROM proj.EMISSAO) || '/' || "
                           f"EXTRACT(YEAR FROM proj.EMISSAO) AS EMISSAO_BR, "
                           f"proj.NUM_DESENHO, COALESCE(arq.caminho, ''), COALESCE(proj.qtde, ''), COALESCE(proj.id_cliente, ''), "
                           f"COALESCE(proj.SOLICITANTE, ''), "
                           f"EXTRACT(DAY FROM proj.PREVISAO_ENTREGA) || '/' || "
                           f"EXTRACT(MONTH FROM proj.PREVISAO_ENTREGA) || '/' || "
                           f"EXTRACT(YEAR FROM proj.PREVISAO_ENTREGA) AS ENTREGA_BR, COALESCE(proj.OBS, '') "
                           f"FROM PROJETO as proj "
                           f"LEFT JOIN ARQUIVOS as arq ON proj.ID_ARQUIVO = arq.id "
                           f"where proj.status = 'A';")
            dados_interno = cursor.fetchall()
            if dados_interno:
                for i in dados_interno:
                    id_proj, emissao, num_des, caminho, qtde, id_cliente, solic, entrega, obs = i

                    if id_cliente:
                        cursor = conecta.cursor()
                        cursor.execute(f"select id, razao "
                                       f"from clientes "
                                       f"where id = {id_cliente};")
                        dados_cliente = cursor.fetchall()

                        if dados_cliente:
                            cliente = f"{dados_cliente[0][0]} - {dados_cliente[0][1]}"
                        else:
                            cliente = ""
                    else:
                        cliente = ""

                    dados = (id_proj, emissao, num_des, caminho, qtde, cliente, solic, entrega, obs)
                    nova_lista.append(dados)

            if nova_lista:
                lanca_tabela(self.table_Projetos, nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tudo(self):
        try:
            self.table_Projetos.setRowCount(0)

            self.line_Solicitante.clear()
            self.combo_Cliente.setCurrentText("")

            self.line_Num_Desenho.clear()
            self.line_Cod_Arq.clear()
            self.line_Qtde.clear()
            self.line_Descricao.clear()
            self.line_Cod_ERP.clear()
            self.line_Tipo.clear()
            self.plain_Obs.clear()

            data_entrega = date.today() + timedelta(60)
            self.date_Entrega.setDate(data_entrega)

            self.lanca_projetos_pendentes()

            self.definir_num_projeto()

            definir_data_atual(self.date_Emissao)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_projeto(self):
        try:
            id_projeto = self.line_Num_Projeto.text()

            tem_projeto = self.consulta_projeto_existe(id_projeto)

            if tem_projeto:
                cursor = conecta_engenharia.cursor()
                cursor.execute(f"DELETE FROM PROJETO WHERE ID = {id_projeto}")

                conecta_engenharia.commit()

                self.mensagem_alerta(f'O projeto de registro Nº {id_projeto} foi excluído com sucesso!')

                self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def consulta_projeto_existe(self, id_projeto):
        try:
            cursor = conecta_engenharia.cursor()
            cursor.execute(f"SELECT ID_ARQUIVO, NUM_DESENHO, QTDE, ID_CLIENTE, SOLICITANTE, "
                           f"PREVISAO_ENTREGA, OBS "
                           f"FROM PROJETO "
                           f"where id = {id_projeto};")
            dados_interno = cursor.fetchall()

            return dados_interno

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            id_projeto = self.line_Num_Projeto.text()

            num_desenho = self.line_Num_Desenho.text()
            id_arquivo = self.line_Cod_Arq.text()
            cliente = self.combo_Cliente.currentText()

            qtde = self.line_Qtde.text()

            match = padrao_desenho.search(num_desenho)

            if not id_arquivo and not num_desenho:
                self.mensagem_alerta(f'Precisa definir o número de desenho para prosseguir!')
            elif not match:
                self.mensagem_alerta(f'Número de desenho fora do padrão!')
            elif not cliente:
                msg = f'Tem certeza que deseja salvar o projeto sem definir o Cliente?'

                proj_existe = self.consulta_projeto_existe(id_projeto)
                if self.pergunta_confirmacao(msg):
                    if proj_existe:
                        self.salvar_projeto_existente(id_projeto)
                    else:
                        self.salvar_projeto_novo()
            elif not qtde:
                msg = f'Tem certeza que deseja salvar o projeto sem definir Quantidade de Produção?'
                proj_existe = self.consulta_projeto_existe(id_projeto)
                if self.pergunta_confirmacao(msg):
                    if proj_existe:
                        self.salvar_projeto_existente(id_projeto)
                    else:
                        self.salvar_projeto_novo()
            else:
                proj_existe = self.consulta_projeto_existe(id_projeto)
                if proj_existe:
                    self.salvar_projeto_existente(id_projeto)
                else:
                    self.salvar_projeto_novo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_projeto_existente(self, id_projeto):
        try:
            cliente = self.combo_Cliente.currentText()
            if cliente:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]
            else:
                id_cliente = None

            solicitante = self.line_Solicitante.text()
            if solicitante:
                solic = solicitante.upper()
            else:
                solic = None

            num_desenho = self.line_Num_Desenho.text()

            id_arquivo = self.line_Cod_Arq.text()
            if id_arquivo:
                id_arq = id_arquivo
            else:
                id_arq = None

            observacao = self.plain_Obs.toPlainText()
            if observacao:
                obs = observacao.upper()
            else:
                obs = None

            qtde = self.line_Qtde.text()
            if qtde:
                qtde_f = valores_para_float(qtde)
            else:
                qtde_f = None

            nome_computador = socket.gethostname()

            emissao = self.date_Emissao.text()
            emis = datetime.strptime(emissao, '%d/%m/%Y').date()

            entrega = self.date_Entrega.text()
            entreg = datetime.strptime(entrega, '%d/%m/%Y').date()

            cursor = conecta_engenharia.cursor()
            cursor.execute("""
                UPDATE PROJETO SET 
                    EMISSAO = ?, 
                    ID_ARQUIVO = ?,
                    NUM_DESENHO = ?,
                    QTDE = ?,
                    ID_CLIENTE = ?,
                    SOLICITANTE = ?,
                    PREVISAO_ENTREGA = ?,
                    OBS = ?,
                    STATUS = ?,
                    NOME_PC = ?
                WHERE ID = ?
            """, (
                emis,
                id_arq,
                num_desenho,
                qtde_f,
                id_cliente,
                solic,
                entreg,
                obs,  # ← None aqui vira NULL
                'A',
                nome_computador,
                id_projeto  # ← importante
            ))

            conecta_engenharia.commit()

            self.mensagem_alerta(f'O projeto Nº {id_projeto} - {num_desenho} foi atualizado com sucesso!')

            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_projeto_novo(self):
        try:
            cliente = self.combo_Cliente.currentText()
            if cliente:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]
            else:
                id_cliente = None

            solicitante = self.line_Solicitante.text()
            if solicitante:
                solic = solicitante.upper()
            else:
                solic = None

            num_desenho = self.line_Num_Desenho.text()
            id_arquivo = self.line_Cod_Arq.text()
            if id_arquivo:
                id_arq = id_arquivo
            else:
                id_arq = None

            observacao = self.plain_Obs.toPlainText()
            if observacao:
                obs = observacao.upper()
            else:
                obs = None

            qtde = self.line_Qtde.text()
            if qtde:
                qtde_f = valores_para_float(qtde)
            else:
                qtde_f = None

            nome_computador = socket.gethostname()

            emissao = self.date_Emissao.text()
            emis = datetime.strptime(emissao, '%d/%m/%Y').date()

            entrega = self.date_Entrega.text()
            entreg = datetime.strptime(entrega, '%d/%m/%Y').date()

            cursor = conecta_engenharia.cursor()
            cursor.execute("""
                INSERT INTO PROJETO 
                (EMISSAO, ID_ARQUIVO, NUM_DESENHO, QTDE, ID_CLIENTE, SOLICITANTE,
                 PREVISAO_ENTREGA, OBS, STATUS, NOME_PC)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                emis,
                id_arq,
                num_desenho,
                qtde_f,
                id_cliente,
                solic,
                entreg,
                obs,
                'A',
                nome_computador
            ))

            conecta_engenharia.commit()

            self.mensagem_alerta(f'O projeto {num_desenho} foi criado com sucesso!')

            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaEngenhariaProjeto()
    tela.show()
    qt.exec_()
