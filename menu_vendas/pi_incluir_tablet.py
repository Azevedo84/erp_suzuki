import sys
from banco_dados.conexao import conecta
from forms.tela_pi_incluir_tablet import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab
from comandos.telas import icone
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
from datetime import date, datetime
import socket
import traceback

import fitz  # PyMuPDF
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt


class TelaPiIncluirTablet(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        from PyQt5.QtWidgets import QScroller

        QScroller.grabGesture(
            self.scrollArea.viewport(),
            QScroller.LeftMouseButtonGesture
        )
        self.showMaximized()

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        layout_cabec_tab(self.table_Pedido)

        self.definir_line_bloqueados()
        self.definir_validador()
        self.definir_emissao()
        self.definir_num_ped()

        self.line_Codigo_Manu.editingFinished.connect(self.verifica_line_codigo_manual)
        self.line_Qtde_Manu.editingFinished.connect(self.verifica_line_qtde_manual)

        self.btn_ExcluirTudo.clicked.connect(self.excluir_tudo_pedido)
        self.btn_ExcluirItem.clicked.connect(self.excluir_item_estrutura)
        self.btn_Limpar.clicked.connect(self.limpa_tudo)

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

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

    def definir_line_bloqueados(self):
        try:
            self.line_Num_Ped.setReadOnly(True)
            self.line_Descricao_Manu.setReadOnly(True)
            self.line_Referencia_Manu.setReadOnly(True)
            self.line_UM_Manu.setReadOnly(True)
            self.line_NCM_Manu.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_validador(self):
        try:
            validator = QtGui.QIntValidator(0, 123456, self.line_Codigo_Manu)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Codigo_Manu.setValidator(validator)

            validator = QtGui.QDoubleValidator(0, 9999999.000, 3, self.line_Qtde_Manu)
            locale = QtCore.QLocale("pt_BR")
            validator.setLocale(locale)
            self.line_Qtde_Manu.setValidator(validator)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_num_ped(self):
        try:
            cursor = conecta.cursor()
            cursor.execute("select GEN_ID(GEN_PEDIDOINTERNO_ID,0) from rdb$database;")
            ultimo_id_req0 = cursor.fetchall()
            ultimo_id_req1 = ultimo_id_req0[0]
            ultimo_id_req2 = int(ultimo_id_req1[0]) + 1
            ultimo_id_req = str(ultimo_id_req2)
            self.line_Num_Ped.setText(ultimo_id_req)
            self.line_Num_Ped.setReadOnly(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tabela_pedido(self):
        try:
            self.table_Pedido.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_dados_manual(self):
        try:
            self.line_Codigo_Manu.clear()
            self.line_Descricao_Manu.clear()
            self.line_Referencia_Manu.clear()
            self.line_UM_Manu.clear()
            self.line_NCM_Manu.clear()
            self.line_Qtde_Manu.clear()
            self.definir_emissao()

            self.table_Estoque.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_dados_pedido(self):
        try:
            self.line_Solicitante.clear()
            self.line_Obs.clear()
            self.combo_Cliente.setCurrentText("")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpa_tudo(self):
        self.limpa_tabela_pedido()
        self.limpa_dados_manual()
        self.limpa_dados_pedido()

    def verifica_line_codigo_manual(self):
        if not self.processando:
            try:
                self.processando = True

                codigo_produto = self.line_Codigo_Manu.text()

                if not codigo_produto:
                    self.mensagem_alerta('O campo "Código" não pode estar vazio!')
                    self.line_Codigo_Manu.clear()
                elif int(codigo_produto) == 0:
                    self.mensagem_alerta('O campo "Código" não pode ser "0"!')
                    self.line_Codigo_Manu.clear()
                else:
                    self.verifica_sql_produto_manual()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_dados_produto_manual(self):
        try:
            codigo_produto = self.line_Codigo_Manu.text()
            cur = conecta.cursor()
            cur.execute(f"SELECT id, descricao, COALESCE(descricaocomplementar, '') as compl, "
                        f"COALESCE(obs, '') as obs, unidade, COALESCE(ncm, '') as local, "
                        f"quantidade, embalagem FROM produto where codigo = {codigo_produto};")
            detalhes_produto = cur.fetchall()
            id_prod, descr, compl, ref, um, ncm, saldo, embalagem = detalhes_produto[0]

            self.line_Descricao_Manu.setText(descr)
            self.line_Referencia_Manu.setText(ref)
            self.line_NCM_Manu.setText(ncm)
            self.line_UM_Manu.setText(um)

            self.line_Saldo_Total.setText(str(saldo))

            self.manipula_dados_tabela_estoque(id_prod)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_dados_tabela_estoque(self, id_prod):
        try:
            cur = conecta.cursor()
            cur.execute(f"SELECT loc.nome, sald.saldo FROM SALDO_ESTOQUE as sald "
                        f"INNER JOIN LOCALESTOQUE loc ON sald.local_estoque = loc.id "
                        f"where sald.produto_id = {id_prod} order by loc.nome;")
            detalhes_saldos = cur.fetchall()
            if detalhes_saldos:
                lanca_tabela(self.table_Estoque, detalhes_saldos)

            self.abrir_pdf_interno()

            self.line_Qtde_Manu.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def abrir_pdf_interno(self):
        try:
            self.label_2.clear()

            cod = self.line_Codigo_Manu.text()
            ref = self.line_Referencia_Manu.text()

            import re

            s = re.sub(r"[^\d.]", "", ref)  # remove tudo que não é número ou ponto
            s = re.sub(r"\.+$", "", s)

            caminho_pdf = rf"\\Publico\C\OP\Projetos\{s}.pdf"
            caminho_png = rf"\\Publico\C\OP\Projetos\{cod}.png"

            if os.path.exists(caminho_pdf):
                doc = fitz.open(caminho_pdf)
                page = doc.load_page(0)
                pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

                image = QImage(
                    pix.samples,
                    pix.width,
                    pix.height,
                    pix.stride,
                    QImage.Format_RGB888
                )

                pixmap = QPixmap.fromImage(image)
                self.mostrar_pixmap(pixmap)

            elif os.path.exists(caminho_png):
                pixmap = QPixmap(caminho_png)
                self.mostrar_pixmap(pixmap)

            else:
                from arquivos.chamar_arquivos import definir_caminho_arquivo

                caminho = os.path.join('..', 'arquivos', 'imagens tela', "sem desenho.png")
                caminho_arquivo = definir_caminho_arquivo(caminho)

                doc = fitz.open(caminho_arquivo)
                page = doc.load_page(0)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

                image = QImage(
                    pix.samples,
                    pix.width,
                    pix.height,
                    pix.stride,
                    QImage.Format_RGB888
                )

                pixmap = QPixmap.fromImage(image)
                self.mostrar_pixmap(pixmap)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def mostrar_pixmap(self, pixmap):
        pixmap = pixmap.scaled(
            self.label_2.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.label_2.setPixmap(pixmap)

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
                exc_traceback = sys.exc_info()[2]
                self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

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

            extrai_estrutura = extrair_tabela(self.table_Pedido)

            ja_existe = False
            for itens in extrai_estrutura:
                cod_con = itens[0]
                if cod_con == cod:
                    ja_existe = True
                    break

            if not ja_existe:
                datamov = self.date_Emissao.text()

                cursor = conecta.cursor()
                cursor.execute(f"SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, "
                               f"prod.unidade "
                               f"FROM produto as prod "
                               f"INNER JOIN conjuntos conj ON prod.conjunto = conj.id "
                               f"where codigo = {cod};")
                detalhes_produto = cursor.fetchall()
                cod, descr, ref, um = detalhes_produto[0]

                dados1 = [cod, descr, ref, um, qtdezinha_float, datamov]
                extrai_estrutura.append(dados1)

                if extrai_estrutura:
                    lanca_tabela(self.table_Pedido, extrai_estrutura)

            else:
                self.mensagem_alerta("Este produto já foi adicionado a estrutura!")

            self.limpa_dados_manual()
            self.line_Codigo_Manu.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_tudo_pedido(self):
        try:
            extrai_estrutura = extrair_tabela(self.table_Pedido)
            if not extrai_estrutura:
                self.mensagem_alerta(f'A tabela "Lista Pedido" está vazia!')
            else:
                self.table_Pedido.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_item_estrutura(self):
        try:
            extrai_recomendados = extrair_tabela(self.table_Pedido)
            if not extrai_recomendados:
                self.mensagem_alerta(f'A tabela "Lista Pedido" está vazia!')
            else:
                linha_selecao = self.table_Pedido.currentRow()
                if linha_selecao >= 0:
                    self.table_Pedido.removeRow(linha_selecao)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            extrai_pedido = extrair_tabela(self.table_Pedido)
            num_ped = self.line_Num_Ped.text()
            cliente = self.combo_Cliente.currentText()
            solicitante = self.line_Solicitante.text()
            obs = self.line_Obs.text()

            if not extrai_pedido:
                self.mensagem_alerta(f'A tabela "Lista Pedido" está vazia!')
            elif not num_ped:
                self.mensagem_alerta(f'O campo "Nº PED" não pode estar vazio!')
            elif num_ped == "0":
                self.mensagem_alerta(f'O "Nº PED" não pode ser "0"!')
            elif not cliente:
                self.mensagem_alerta(f'O campo "Cliente" não pode estar vazio!')
            elif not solicitante:
                self.mensagem_alerta(f'O campo "Solicitante" não pode estar vazio!')
            elif not obs:
                self.mensagem_alerta(f'O campo "Observação" não pode estar vazio!\n\n'
                                     f'Defina o destino (Onde vai ser usado) da "Lista Pedidos".')
            else:
                self.salvar_pedido()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_pedido(self):
        try:
            print("salvar")
            cliente = self.combo_Cliente.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]

            solicitante = self.line_Solicitante.text().upper()
            obs = self.line_Obs.text().upper()

            nome_computador = socket.gethostname()

            datamov = self.date_Emissao.text()
            date_mov = datetime.strptime(datamov, '%d/%m/%Y').date()
            data_mov_certa = str(date_mov)

            cursor = conecta.cursor()
            cursor.execute("select GEN_ID(GEN_PEDIDOINTERNO_ID,0) from rdb$database;")
            ultimo_ped0 = cursor.fetchall()
            ultimo_ped1 = ultimo_ped0[0]
            ultimo_ped = int(ultimo_ped1[0]) + 1

            if obs:
                cursor = conecta.cursor()
                cursor.execute(f"Insert into pedidointerno (ID, EMISSAO, ID_CLIENTE, SOLICITANTE, OBS, NOME_PC, "
                               f"STATUS) "
                               f"values (GEN_ID(GEN_PEDIDOINTERNO_ID,1), "
                               f"'{data_mov_certa}', '{id_cliente}', '{solicitante}', '{obs}', "
                               f"'{nome_computador}', 'A');")
            else:
                cursor = conecta.cursor()
                cursor.execute(f"Insert into pedidointerno (ID, EMISSAO, ID_CLIENTE, SOLICITANTE, NOME_PC, STATUS) "
                               f"values (GEN_ID(GEN_PEDIDOINTERNO_ID,1), "
                               f"'{data_mov_certa}', '{id_cliente}', '{solicitante}', '{nome_computador}', 'A');")

            extrai_pedido = extrair_tabela(self.table_Pedido)

            for itens in extrai_pedido:
                codigo, descricao, referencia, um, qtde, entrega = itens

                if "," in qtde:
                    qtdezinha_com_ponto = qtde.replace(',', '.')
                    qtdezinha_float = float(qtdezinha_com_ponto)
                else:
                    qtdezinha_float = float(qtde)

                date_entr = datetime.strptime(entrega, '%d/%m/%Y').date()
                data_entr_certa = str(date_entr)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, codigo, embalagem FROM produto where codigo = '{codigo}';")
                dados_produto = cursor.fetchall()
                id_produto, codigo, embalagem = dados_produto[0]

                cursor = conecta.cursor()
                cursor.execute(f"Insert into produtopedidointerno (ID_PRODUTO, ID_PEDIDOINTERNO, QTDE, "
                               f"DATA_PREVISAO, STATUS) "
                               f"values ({id_produto}, {ultimo_ped}, {qtdezinha_float}, '{data_entr_certa}', "
                               f"'A');")

            conecta.commit()
            print("salvado")

            self.limpa_tudo()
            self.definir_num_ped()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPiIncluirTablet()
    tela.show()
    qt.exec_()
