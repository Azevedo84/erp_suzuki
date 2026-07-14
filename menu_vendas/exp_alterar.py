import sys
from banco_dados.conexao import conecta
from forms.tela_exp_alterar import *
from banco_dados.controle_erros import grava_erro_banco
from comandos.tabelas import lanca_tabela_v2, extrair_tabela
from comandos.telas import tamanho_aplicacao, icone
from comandos.conversores import valores_para_float
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import inspect
import os
import socket
import traceback
from datetime import date, datetime
import getpass


class TelaExpedicaoAlterar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.nome_computador = socket.gethostname()
        self.username = getpass.getuser()

        frame = inspect.currentframe()
        if frame is None:
            raise RuntimeError("Não foi possível obter o frame atual.")
        nome_arquivo_com_caminho = inspect.getframeinfo(frame).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_vendas.png")
        tamanho_aplicacao(self)

        self.definir_combo_cliente_vendas()

        self.table_Vendas_Pendentes.viewport().installEventFilter(self)

        self.combo_Cliente_Vendas.activated.connect(self.lanca_vendas_pendentes)

        self.definir_emissao()
        self.definir_num_exp()

        self.btn_Limpar.clicked.connect(self.limpar_tudo)
        self.btn_Excluir_Item.clicked.connect(self.excluir_item)
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
            frame = inspect.currentframe()
            nome_funcao_trat = frame.f_code.co_name if frame else "desconhecida"
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
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
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
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_num_exp(self):
        try:
            cursor = conecta.cursor()
            cursor.execute("select GEN_ID(GEN_EXPEDICAO_ID,0) from rdb$database;")
            ultimo_id_req0 = cursor.fetchall()
            ultimo_id_req1 = ultimo_id_req0[0]
            ultimo_id_req2 = int(ultimo_id_req1[0]) + 1
            ultimo_id_req = str(ultimo_id_req2)
            self.line_Num_Exp.setText(ultimo_id_req)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def definir_combo_cliente_vendas(self):
        try:
            self.combo_Cliente_Vendas.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute("""
                SELECT DISTINCT
                    c.id,
                    c.razao
                FROM CLIENTES c
                INNER JOIN PEDIDOINTERNO pi
                    ON pi.ID_CLIENTE = c.ID
                INNER JOIN PRODUTOPEDIDOINTERNO ppi
                    ON ppi.ID_PEDIDOINTERNO = pi.ID
                INNER JOIN PRODUTO p
                    ON p.ID = ppi.ID_PRODUTO
                INNER JOIN (
                    SELECT
                        se.PRODUTO_ID,
                        SUM(se.SALDO) AS SALDO_EXP
                    FROM SALDO_ESTOQUE se
                    INNER JOIN LOCALESTOQUE le
                        ON le.ID = se.LOCAL_ESTOQUE
                    WHERE le.USARESTOQUE = 'S'
                    GROUP BY se.PRODUTO_ID
                ) saldo
                    ON saldo.PRODUTO_ID = p.ID
                WHERE c.VENDA = 'S'
                  AND ppi.STATUS = 'A'
                  AND p.QUANTIDADE >= ppi.QTDE
                  AND saldo.SALDO_EXP >= ppi.QTDE
                ORDER BY c.RAZAO
            """)

            for ides, descr in cursor.fetchall():
                nova_lista.append(f"{ides} - {descr}")

            self.combo_Cliente_Vendas.addItems(nova_lista)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def lanca_vendas_pendentes(self):
        try:
            self.table_Vendas_Pendentes.setRowCount(0)
            self.table_Expedicao.setRowCount(0)

            self.line_LocalExp_Venda.clear()

            tabela_nova = []

            cliente = self.combo_Cliente_Vendas.currentText()

            if cliente:
                clientetete = cliente.find(" - ")
                id_cliente = cliente[:clientetete]
                nome_cliente = cliente[clientetete + 3:]

                # Saldo disponível apenas nos locais que podem ser expedidos
                cursor = conecta.cursor()
                cursor.execute("""
                    SELECT
                        se.produto_id,
                        SUM(se.saldo)
                    FROM SALDO_ESTOQUE se
                    INNER JOIN LOCALESTOQUE le
                        ON le.id = se.local_estoque
                    WHERE le.usarestoque = 'S'
                    GROUP BY se.produto_id
                """)

                saldo_expedivel = {}
                for id_produto, saldo in cursor.fetchall():
                    saldo_expedivel[id_produto] = valores_para_float(saldo)

                # PEDIDOS INTERNOS
                cursor = conecta.cursor()
                cursor.execute(f"""
                    SELECT
                        ped.id,
                        prod.id,
                        prod.codigo,
                        prod.descricao,
                        COALESCE(prod.obs, '') as obs,
                        prod.unidade,
                        prodint.qtde,
                        prodint.data_previsao,
                        prod.quantidade,
                        prod.localizacao,
                        cli.razao
                    FROM PRODUTOPEDIDOINTERNO prodint
                    INNER JOIN produto prod
                        ON prodint.id_produto = prod.id
                    INNER JOIN pedidointerno ped
                        ON prodint.id_pedidointerno = ped.id
                    INNER JOIN clientes cli
                        ON ped.id_cliente = cli.id
                    WHERE prodint.status = 'A'
                      AND ped.id_cliente = {id_cliente}
                """)

                dados_interno = cursor.fetchall()

                if dados_interno:
                    for i in dados_interno:
                        (num_ped, id_produto, cod, descr, ref, um,
                         qtde, entrega, saldo_total, local, cliente) = i

                        qtde_float = valores_para_float(qtde)
                        saldo_total = valores_para_float(saldo_total)
                        saldo_exp = saldo_expedivel.get(id_produto, 0)

                        if saldo_total >= qtde_float and saldo_exp >= qtde_float:
                            dados = (
                                f"PI {num_ped}",
                                cod,
                                descr,
                                ref,
                                um,
                                qtde_float,
                                local,
                                saldo_total
                            )
                            tabela_nova.append(dados)

                self.line_LocalExp_Venda.setText(f"PRAT. {nome_cliente}")

            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[1])
                lanca_tabela_v2(self.table_Vendas_Pendentes, lista_de_listas_ordenada)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def limpar_tudo(self):
        try:
            self.table_Vendas_Pendentes.setRowCount(0)
            self.table_Expedicao.setRowCount(0)

            self.definir_combo_cliente_vendas()

            self.definir_emissao()
            self.definir_num_exp()

            self.line_LocalExp_Venda.clear()

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def excluir_item(self):
        try:
            nome_tabela = self.table_Expedicao

            extrai_recomendados = extrair_tabela(nome_tabela)
            if extrai_recomendados:
                linha_selecao = nome_tabela.currentRow()
                if linha_selecao >= 0:
                    nome_tabela.removeRow(linha_selecao)

            extrai = extrair_tabela(nome_tabela)
            cliente = self.combo_Cliente_Vendas.currentText()
            if not extrai and not cliente:
                self.line_LocalExp_Venda.clear()

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def eventFilter(self, source, event):
        try:
            tabela_vendas_pendentes = self.table_Vendas_Pendentes
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is tabela_vendas_pendentes.viewport()):
                item = tabela_vendas_pendentes.currentItem()

                cliente = self.combo_Cliente_Vendas.currentText()

                if item and cliente:
                    extrai_recomendados = extrair_tabela(tabela_vendas_pendentes)
                    item_selecionado = extrai_recomendados[item.row()]

                    local_exp = self.line_LocalExp_Venda.text()
                    if local_exp:
                        self.manipula_venda_exp(item_selecionado)
                    else:
                        self.mensagem_alerta("Definir local de expedição!")

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def manipula_venda_exp(self, item_selecionado):
        try:
            origem, cod, desc, ref, um, qtde, local, saldo = item_selecionado

            extrai_produtos = extrair_tabela(self.table_Expedicao)

            local_exp = self.line_LocalExp_Venda.text()

            if local_exp:
                local = local_exp
            else:
                local = ""

            dados = [local, cod, desc, ref, um, qtde, origem]

            ja_existe = False

            for iii in extrai_produtos:
                local_e, cod_e, desc_e, ref_e, um_e, qtde_e, origem = iii

                if cod == cod_e:
                    ja_existe = True
                    break

            if not ja_existe:
                extrai_produtos.append(dados)

            lanca_tabela_v2(self.table_Expedicao, extrai_produtos)

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def verifica_salvamento(self):
        try:
            print("salvaMENTO")
            num_exp = self.line_Num_Exp.text()

            operacao = self.combo_Operacao.currentText()

            cliente = self.combo_Cliente_Vendas.currentText()

            dados_exp = extrair_tabela(self.table_Expedicao)

            if not dados_exp:
                self.mensagem_alerta(f'A tabela "EXPEDIÇÃO" não pode estar vazia!')
            elif not num_exp:
                self.mensagem_alerta(f'O campo "Nº EXP" não pode estar vazio!')
            elif not operacao:
                self.mensagem_alerta(f'O campo "TIPO OPERAÇÃO" não pode estar vazio!')
            elif not cliente:
                self.mensagem_alerta(f'O campo "CLIENTE" não pode estar vazio!')
            else:
                self.salvar_expedicao_venda()

        except Exception as e:
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)

    def salvar_expedicao_venda(self):
        try:
            print("salvar")

            cliente = self.combo_Cliente_Vendas.currentText()
            clientetete = cliente.find(" - ")
            id_cliente = cliente[:clientetete]
            nome_cliente = cliente[clientetete + 3:]

            datamov = self.date_Emissao.text()
            date_mov = datetime.strptime(datamov, "%d/%m/%Y").date()

            cur = conecta.cursor()
            cur.execute(f"SELECT funcionario_id, descricao, nome_usuario FROM ENVIA_PC "
                        f"where descricao = '{self.nome_computador}' "
                        f"and nome_usuario = '{self.username}';")
            dados_usuario = cur.fetchall()

            if dados_usuario:
                id_func = dados_usuario[0][0]
            else:
                id_func = 11

            cursor = conecta.cursor()
            cursor.execute(
                """
                INSERT INTO EXPEDICAO (DATA, ID_CLIENTE)
                VALUES (?, ?)
                RETURNING ID
                """,
                (date_mov, id_cliente)
            )

            id_expedicao = cursor.fetchone()[0]

            dados_exp = extrair_tabela(self.table_Expedicao)
            for itens in dados_exp:
                local, cod, desc, ref, um, qtde, origem = itens

                qtde_float = valores_para_float(qtde)

                cursor = conecta.cursor()
                cursor.execute(f"SELECT id, codigo, embalagem FROM produto where codigo = '{cod}';")
                dados_produto = cursor.fetchall()
                id_produto, codigo, embalagem = dados_produto[0]

                origemtete = origem.find(" ")
                tipo_origem = origem[:origemtete]
                num_origem = origem[origemtete + 1:]

                cursor.execute(
                    """
                    INSERT INTO MOVIMENTACAO
                    (PRODUTO, OBS, TIPO, QUANTIDADE, DATA, CODIGO, FUNCIONARIO, LOCALESTOQUE)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    RETURNING ID
                    """,
                    (id_produto,
                     f"EXP {id_expedicao} - {nome_cliente}/{local}",
                     "220",
                     qtde_float,
                     date_mov,
                     cod,
                     id_func,
                     20)
                )
                id_mov = cursor.fetchone()[0]

                cursor.execute(
                    """
                    INSERT INTO EXPEDICAO_PRODUTO
                    (ID_EXPEDICAO, ID_PRODUTO, QTDE, LOCAL_EXPEDICAO, TIPO_ORIGEM, NUM_ORIGEM, ID_MOV)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (id_expedicao, id_produto, qtde_float, local, tipo_origem, num_origem, id_mov)
                )

                cursor = conecta.cursor()
                cursor.execute(f"UPDATE produtopedidointerno SET STATUS = 'B' "
                               f"WHERE id_produto = {id_produto} "
                               f"and id_pedidointerno = {num_origem};")

            conecta.commit()

            self.mensagem_alerta("Ordem de Expedição salva com sucesso!")

            self.limpar_tudo()

        except Exception as e:
            conecta.rollback()
            frame = inspect.currentframe()
            nome_funcao = frame.f_code.co_name if frame else "desconhecida"
            exc_traceback = sys.exc_info()[2]
            self.trata_excecao(nome_funcao, str(e), self.nome_arquivo, exc_traceback)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaExpedicaoAlterar()
    tela.show()
    qt.exec_()