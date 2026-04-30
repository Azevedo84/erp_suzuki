import sys
from banco_dados.conexao import conecta_engenharia
from forms.tela_engenharia_divergencias import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.telas import tamanho_aplicacao, icone
from comandos.cores import cor_cinza_claro
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QStyledItemDelegate, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import inspect
import os
import traceback


class TelaConsultaDivergencias(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu.png")
        tamanho_aplicacao(self)

        self.definir_combo_fornecedor()

        self.btn_Consulta.clicked.connect(self.lanca_diveregencias)

        self.table_Divergencia.cellDoubleClicked.connect(self.resolver_item)

        self.btn_Salvar.clicked.connect(self.salvar_dados)

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

    def resolver_item(self, row):
        try:
            item_ref = self.table_Divergencia.item(row, 0)

            resolvido = item_ref.data(Qt.UserRole)

            novo_estado = not resolvido
            item_ref.setData(Qt.UserRole, novo_estado)

            for col in range(self.table_Divergencia.columnCount()):
                item = self.table_Divergencia.item(row, col)
                if item:
                    if novo_estado:
                        item.setBackground(QColor(cor_cinza_claro))
                    else:
                        item.setBackground(QColor(255, 255, 255))

        except Exception as e:
            print(e)

    def definir_combo_fornecedor(self):
        try:
            self.combo_Divergencia.clear()

            tabela = []

            branco = "TODOS"
            tabela.append(branco)

            cursor = conecta_engenharia.cursor()
            sql = """
            SELECT ID, DESCRICAO
            FROM TIPO_DIVERGENCIA
            """
            cursor.execute(sql)
            dados_diverg = cursor.fetchall()

            if dados_diverg:
                for dadus in dados_diverg:
                    ides, descricao = dadus
                    msg = f"{ides} - {descricao}"
                    tabela.append(msg)

                self.combo_Divergencia.addItems(tabela)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_diveregencias(self):
        try:
            self.table_Divergencia.setRowCount(0)

            divergencias = self.combo_Divergencia.currentText()

            if divergencias:
                sql = """
                    SELECT div.RESOLVIDO, div.id, div.ID_ARQUIVO, ARQ.NOME_BASE, arq.TIPO_ARQUIVO, tip_div.DESCRICAO, 
                    div.OBS, arq.CAMINHO
                    FROM DIVERGENCIAS as div
                    INNER JOIN ARQUIVOS as arq ON div.ID_ARQUIVO = arq.id 
                    INNER JOIN TIPO_DIVERGENCIA as tip_div ON div.ID_TIPO_DIVERGENCIA = tip_div.id 
                    """

                parametros = []

                if divergencias != "TODOS":
                    pos = divergencias.find(" - ")
                    if pos == -1:
                        raise ValueError("Formato inválido no combo de divergência")

                    id_divergencia = divergencias[:pos]

                    sql += " WHERE div.ID_TIPO_DIVERGENCIA = ? "
                    parametros.append(id_divergencia)

                cur = conecta_engenharia.cursor()
                cur.execute(sql, parametros)
                dados_divergencias = cur.fetchall()

                if dados_divergencias:
                    self.lanca_tabela_v2(self.table_Divergencia, dados_divergencias, bloqueia_texto=False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_tabela_v2(self, nome_tabela, dados_tab, altura_linha=23,
                        zebra=True, largura_auto=True, bloqueia_texto=True):

        try:
            if not dados_tab:
                return

            linhas_est = len(dados_tab)
            colunas_est = len(dados_tab[0])

            # 👉 remove coluna RESOLVIDO da visualização
            nome_tabela.setRowCount(linhas_est)
            nome_tabela.setColumnCount(colunas_est - 1)

            # delegate centralizado
            alinha_cetralizado = AlignDelegate(nome_tabela)
            for j in range(colunas_est - 1):
                nome_tabela.setItemDelegateForColumn(j, alinha_cetralizado)

            for i, linha in enumerate(dados_tab):
                nome_tabela.setRowHeight(i, altura_linha)

                resolvido_linha = linha[0]  # 👈 coluna RESOLVIDO

                for j, dado in enumerate(linha):

                    # 👉 ignora coluna RESOLVIDO
                    if j == 0:
                        continue

                    item = QTableWidgetItem(str(dado))

                    # 🔒 bloqueia tudo por padrão
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                    # ✅ libera edição na coluna OBS (ajusta se quiser)
                    # OBS: como removemos coluna 0, aqui é j-1
                    if (j - 1) == 6:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)

                    # ✅ aplica estado resolvido
                    if resolvido_linha == "S":
                        item.setBackground(QColor(cor_cinza_claro))
                        item.setData(Qt.UserRole, True)
                    else:
                        item.setData(Qt.UserRole, False)

                    # 👉 posiciona na coluna correta
                    nome_tabela.setItem(i, j - 1, item)

            nome_tabela.setSelectionBehavior(QAbstractItemView.SelectRows)

            if largura_auto:
                nome_tabela.resizeColumnsToContents()

            if bloqueia_texto:
                nome_tabela.setEditTriggers(QTableWidget.NoEditTriggers)

            if zebra:
                nome_tabela.setAlternatingRowColors(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_dados(self):
        try:
            cursor = conecta_engenharia.cursor()

            total = 0

            for row in range(self.table_Divergencia.rowCount()):

                item_id = self.table_Divergencia.item(row, 0)

                if not item_id:
                    continue

                id_div = item_id.text()
                resolvido = item_id.data(Qt.UserRole)

                if resolvido:
                    total += 1

                    cursor.execute("UPDATE DIVERGENCIAS SET RESOLVIDO = ? WHERE ID = ?", ("S", id_div,))

                    conecta_engenharia.commit()
                else:
                    cursor.execute("UPDATE DIVERGENCIAS SET RESOLVIDO = ? WHERE ID = ?", (None, id_div,))

                    conecta_engenharia.commit()

            self.mensagem_alerta(f"{total} divergência(s) marcada(s) como resolvida(s).")

        except Exception as e:
            print(e)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaConsultaDivergencias()
    tela.show()
    qt.exec_()
