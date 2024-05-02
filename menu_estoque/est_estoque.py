import sys
from forms.tela_est_estoque import *
from banco_dados.conexao import conecta
from comandos.comando_notificacao import mensagem_alerta, tratar_notificar_erros
from comandos.comando_tabelas import extrair_tabela, lanca_tabela, layout_cabec_tab
from comandos.comando_telas import tamanho_aplicacao, icone, cor_widget, cor_widget_cab, cor_fonte, cor_btn
from comandos.comando_telas import cor_fundo_tela
from comandos.comando_excel import edita_alinhamento, edita_bordas, linhas_colunas_p_edicao
from comandos.comando_excel import criar_workbook, edita_fonte, edita_preenchimento, letra_coluna
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import date, timedelta
from pathlib import Path
import inspect
import os


class TelaEstEstoque(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        cor_fundo_tela(self)
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        icone(self, "menu_estoque.png")
        tamanho_aplicacao(self)
        layout_cabec_tab(self.table_Estoque)
        self.layout_proprio()

        self.btn_Gerar_Acinplas.clicked.connect(self.manipula_dados_acinplas)

        self.btn_Gerar_Classifica.clicked.connect(self.atualizartabela)

        self.btn_Salvar.clicked.connect(self.verifica_excel)

        self.definir_data()
        self.btn_Gerar_Classifica.setFocus()

    def layout_proprio(self):
        try:
            cor_widget_cab(self.widget_cabecalho)

            cor_widget(self.widget_Cor1)
            cor_widget(self.widget_Cor2)
            cor_widget(self.widget_Cor3)
            cor_widget(self.widget_Cor4)

            cor_fonte(self.label_13)
            cor_fonte(self.label)
            cor_fonte(self.label_3)
            cor_fonte(self.label_4)
            cor_fonte(self.label_2)
            cor_fonte(self.label_Titulo)
            cor_fonte(self.label_24)
            cor_fonte(self.label_25)

            cor_fonte(self.check_Almox)
            cor_fonte(self.check_Obsoleto)

            cor_btn(self.btn_Salvar)
            cor_btn(self.btn_Limpar)
            cor_btn(self.btn_Gerar_Classifica)
            cor_btn(self.btn_Gerar_Acinplas)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def definir_data(self):
        try:
            data_hoje = date.today()
            primeiro_dia_do_mes_atual = date(data_hoje.year, data_hoje.month, 1)
            ultimo_dia_do_mes_anterior = primeiro_dia_do_mes_atual - timedelta(days=1)

            self.date_relatorio.setDate(ultimo_dia_do_mes_anterior)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def atualizartabela(self):
        try:
            self.table_Estoque.setRowCount(0)

            almox = self.check_Almox.isChecked()
            obsoleto = self.check_Obsoleto.isChecked()

            nomes_colunas = ['CÓD.', 'DESCRIÇÃO', 'REFERÊNCIA', 'UM']

            if not almox and not obsoleto:
                mensagem_alerta(f'Deve ter no mínimo um local de estoque selecionado!')
            else:
                if almox and obsoleto:
                    nomes_colunas.append('ALMOX')
                    nomes_colunas.append('OBSOLETO')
                    self.manipula_dados_acinplas()

                elif almox and not obsoleto:
                    nomes_colunas.append('ALMOX')
                    self.manipula_dados_so_almox()

                elif not almox and obsoleto:
                    nomes_colunas.append('OBSOLETO')
                    self.manipula_dados_so_obsoleto()

                nomes_colunas.extend(['TOTAL'])

                self.table_Estoque.setColumnCount(len(nomes_colunas))
                self.table_Estoque.setHorizontalHeaderLabels(nomes_colunas)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_dados_acinplas(self):
        try:
            nomes_colunas = ['CÓD.', 'DESCRIÇÃO', 'REFERÊNCIA', 'UM', 'ALMOX', 'OBSOLETO', 'TOTAL']

            self.table_Estoque.setColumnCount(len(nomes_colunas))
            self.table_Estoque.setHorizontalHeaderLabels(nomes_colunas)

            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('yyyy-MM-dd')

            cursor = conecta.cursor()
            cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                           "SUM(CASE WHEN sal.local_estoque = 1 THEN sal.saldo ELSE 0 END) as saldo_local_1, "
                           "SUM(CASE WHEN sal.local_estoque = 2 THEN sal.saldo ELSE 0 END) as saldo_local_2, "
                           "SUM(CASE WHEN sal.local_estoque = 1 "
                           "OR sal.local_estoque = 2 THEN sal.saldo ELSE 0 END) as saldo_total "
                           "FROM saldo_estoque as sal "
                           "INNER JOIN produto prod ON sal.produto_id = prod.id "
                           "WHERE saldo <> 0 and (local_estoque = 1 or local_estoque = 2) "
                           "GROUP BY prod.codigo, prod.descricao, prod.obs, prod.unidade;")
            dados_produto = cursor.fetchall()

            itens_negativos = []

            for i in dados_produto:
                cod_sal, des_sal, ref_sal, um_sal, l1_sal, l2_sal, t_sal = i
                if l1_sal < 0 or l2_sal < 0:
                    itens_negativos.append(i)

            if itens_negativos:
                msg = "O relatório não pode ser concluído pois temos materiais com saldo negativo:\n\n"
                for nega in itens_negativos:
                    cod_neg, des_neg, ref_neg, um_neg, l1_neg, l2_neg, t_neg = nega
                    msg += f"- Código: {cod_neg} - {des_neg} \n" \
                           f"- Saldo Almox: {l1_neg}\n" \
                           f"- Saldo Obsoleto: {l2_neg}\n\n\n"

                mensagem_alerta(msg)
            else:
                cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                               f"COALESCE(CASE WHEN m.tipo < 200 THEN m.quantidade END, 0) AS Qtde_Entrada, "
                               f"COALESCE(CASE WHEN m.tipo > 200 THEN m.quantidade END, 0) AS Qtde_Saida, "
                               f"m.localestoque "
                               f"FROM movimentacao m "
                               "INNER JOIN produto prod ON m.produto = prod.id "
                               f"WHERE m.data > '{date_string}' and (m.localestoque = 1 or m.localestoque = 2);")
                select_mov = cursor.fetchall()
                if select_mov:
                    for movimentacao in select_mov:
                        cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao

                        if cod_mov not in [item[0] for item in dados_produto]:
                            dados_produto.append((cod_mov, des_mov, ref_mov, um_mov, 0, 0, 0))

                saldos_atualizados = []
                for i in dados_produto:
                    cod_saldo, des_saldo, ref_saldo, um_saldo, l1_saldo, l2_saldo, t_saldo = i

                    if select_mov:
                        for movimentacao in select_mov:
                            cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao
                            if cod_saldo == cod_mov and local_mov == 1:
                                if entrada_mov:
                                    l1_saldo -= entrada_mov
                                if saida_mov:
                                    l1_saldo += saida_mov
                            elif cod_saldo == cod_mov and local_mov == 2:
                                if entrada_mov:
                                    l2_saldo -= entrada_mov
                                if saida_mov:
                                    l2_saldo += saida_mov

                    saldo_total = l1_saldo + l2_saldo
                    saldos_atualizados.append((cod_saldo, des_saldo, ref_saldo, um_saldo, l1_saldo, l2_saldo,
                                               saldo_total))

                saldos_atualizados = [produto for produto in saldos_atualizados if produto[6] != 0]
                saldos_atualizados_ordenados = sorted(saldos_atualizados, key=lambda x: x[1])

                lanca_tabela(self.table_Estoque, saldos_atualizados_ordenados)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_dados_so_almox(self):
        try:
            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('yyyy-MM-dd')

            cursor = conecta.cursor()
            cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                           "SUM(CASE WHEN sal.local_estoque = 1 THEN sal.saldo ELSE 0 END) as saldo_local_1, "
                           "SUM(CASE WHEN sal.local_estoque = 1 THEN sal.saldo ELSE 0 END) as saldo_total "
                           "FROM saldo_estoque as sal "
                           "INNER JOIN produto prod ON sal.produto_id = prod.id "
                           "WHERE saldo <> 0 and local_estoque = 1 "
                           "GROUP BY prod.codigo, prod.descricao, prod.obs, prod.unidade;")
            dados_produto = cursor.fetchall()
            if dados_produto:
                itens_negativos = []

                for i in dados_produto:
                    cod_sal, des_sal, ref_sal, um_sal, l1_sal, t_sal = i
                    if l1_sal < 0:
                        itens_negativos.append(i)

                if itens_negativos:
                    msg = "O relatório não pode ser concluído pois temos materiais com saldo negativo:\n\n"
                    for nega in itens_negativos:
                        cod_neg, des_neg, ref_neg, um_neg, l1_neg, t_neg = nega
                        msg += f"- Código: {cod_neg} - {des_neg} \n" \
                               f"- Saldo Almox: {l1_neg}\n\n\n"

                    mensagem_alerta(msg)
                else:
                    cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                                   f"COALESCE(CASE WHEN m.tipo < 200 THEN m.quantidade END, 0) AS Qtde_Entrada, "
                                   f"COALESCE(CASE WHEN m.tipo > 200 THEN m.quantidade END, 0) AS Qtde_Saida, "
                                   f"m.localestoque "
                                   f"FROM movimentacao m "
                                   "INNER JOIN produto prod ON m.produto = prod.id "
                                   f"WHERE m.data > '{date_string}' and m.localestoque = 1;")
                    select_mov = cursor.fetchall()
                    if select_mov:
                        for movimentacao in select_mov:
                            cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao

                            if cod_mov not in [item[0] for item in dados_produto]:
                                dados_produto.append((cod_mov, des_mov, ref_mov, um_mov, 0, 0))

                    saldos_atualizados = []
                    for i in dados_produto:
                        cod_saldo, des_saldo, ref_saldo, um_saldo, l1_saldo, t_saldo = i

                        if select_mov:
                            for movimentacao in select_mov:
                                cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao
                                if cod_saldo == cod_mov and local_mov == 1:
                                    if entrada_mov:
                                        l1_saldo -= entrada_mov
                                    if saida_mov:
                                        l1_saldo += saida_mov

                        saldo_total = l1_saldo
                        saldos_atualizados.append((cod_saldo, des_saldo, ref_saldo, um_saldo, l1_saldo, saldo_total))

                    saldos_atualizados = [produto for produto in saldos_atualizados if produto[5] != 0]
                    saldos_atualizados_ordenados = sorted(saldos_atualizados, key=lambda x: x[1])

                    lanca_tabela(self.table_Estoque, saldos_atualizados_ordenados)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def manipula_dados_so_obsoleto(self):
        try:
            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('yyyy-MM-dd')

            cursor = conecta.cursor()
            cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                           "SUM(CASE WHEN sal.local_estoque = 2 THEN sal.saldo ELSE 0 END) as saldo_local_2, "
                           "SUM(CASE WHEN sal.local_estoque = 2 THEN sal.saldo ELSE 0 END) as saldo_total "
                           "FROM saldo_estoque as sal "
                           "INNER JOIN produto prod ON sal.produto_id = prod.id "
                           "WHERE saldo <> 0 and local_estoque = 2 "
                           "GROUP BY prod.codigo, prod.descricao, prod.obs, prod.unidade;")
            dados_produto = cursor.fetchall()
            if dados_produto:
                itens_negativos = []

                for i in dados_produto:
                    cod_sal, des_sal, ref_sal, um_sal, l2_sal, t_sal = i
                    if l2_sal < 0:
                        itens_negativos.append(i)

                if itens_negativos:
                    msg = "O relatório não pode ser concluído pois temos materiais com saldo negativo:\n\n"
                    for nega in itens_negativos:
                        cod_neg, des_neg, ref_neg, um_neg, l2_neg, t_neg = nega
                        msg += f"- Código: {cod_neg} - {des_neg} \n" \
                               f"- Saldo Almox: {l2_neg}\n\n\n"

                    mensagem_alerta(msg)
                else:
                    cursor.execute("SELECT prod.codigo, prod.descricao, COALESCE(prod.obs, '') as obs, prod.unidade, "
                                   f"COALESCE(CASE WHEN m.tipo < 200 THEN m.quantidade END, 0) AS Qtde_Entrada, "
                                   f"COALESCE(CASE WHEN m.tipo > 200 THEN m.quantidade END, 0) AS Qtde_Saida, "
                                   f"m.localestoque "
                                   f"FROM movimentacao m "
                                   "INNER JOIN produto prod ON m.produto = prod.id "
                                   f"WHERE m.data > '{date_string}' and m.localestoque = 2;")
                    select_mov = cursor.fetchall()
                    if select_mov:
                        for movimentacao in select_mov:
                            cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao

                            if cod_mov not in [item[0] for item in dados_produto]:
                                dados_produto.append((cod_mov, des_mov, ref_mov, um_mov, 0, 0))

                    saldos_atualizados = []
                    for i in dados_produto:
                        cod_saldo, des_saldo, ref_saldo, um_saldo, l2_saldo, t_saldo = i

                        if select_mov:
                            for movimentacao in select_mov:
                                cod_mov, des_mov, ref_mov, um_mov, entrada_mov, saida_mov, local_mov = movimentacao
                                if cod_saldo == cod_mov and local_mov == 2:
                                    if entrada_mov:
                                        l2_saldo -= entrada_mov
                                    if saida_mov:
                                        l2_saldo += saida_mov

                        saldo_total = l2_saldo
                        saldos_atualizados.append((cod_saldo, des_saldo, ref_saldo, um_saldo, l2_saldo, saldo_total))

                    saldos_atualizados = [produto for produto in saldos_atualizados if produto[5] != 0]
                    saldos_atualizados_ordenados = sorted(saldos_atualizados, key=lambda x: x[1])

                    lanca_tabela(self.table_Estoque, saldos_atualizados_ordenados)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def verifica_excel(self):
        try:
            extrai_dados_tabela = extrair_tabela(self.table_Estoque)
            if not extrai_dados_tabela:
                mensagem_alerta(f'A Tabela "Lista de Estoque" está vazia!')
            else:
                num_colunas = self.table_Estoque.columnCount()

                if num_colunas == 7:
                    self.gerar_excel_total()
                elif num_colunas == 6:
                    nomes_colunas = []
                    for coluna in range(num_colunas):
                        nome_coluna = self.table_Estoque.horizontalHeaderItem(coluna).text()
                        nomes_colunas.append(nome_coluna)
                    coluna_interessa = nomes_colunas[4]

                    if coluna_interessa == "ALMOX":
                        self.gerar_excel_almox()
                    elif coluna_interessa == "OBSOLETO":
                        self.gerar_excel_obsoleto()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def gerar_excel_total(self):
        try:
            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('dd-MM-yyyy')

            extrai_dados_tabela = extrair_tabela(self.table_Estoque)
            if not extrai_dados_tabela:
                mensagem_alerta(f'A Tabela "Lista de Estoque" está vazia!')
            else:
                workbook = criar_workbook()
                sheet = workbook.active
                sheet.title = "Estoque Final"

                headers = ["Código", "Descrição", "Referência", "UM", "Almox", "Obsoleto", "Total"]
                sheet.append(headers)

                header_row = sheet[1]
                for cell in header_row:
                    edita_fonte(cell, tamanho=11, negrito=True)
                    edita_preenchimento(cell)
                    edita_alinhamento(cell)

                for dados_ex in extrai_dados_tabela:
                    codigo, descr, ref, um, saldo_local_1, saldo_local_2, saldo_total = dados_ex
                    codigu = int(codigo)

                    if saldo_local_1 == "":
                        saldo1_e = 0.00
                    else:
                        saldo1_e = float(saldo_local_1)

                    if saldo_local_2 == "":
                        saldo2_e = 0.00
                    else:
                        saldo2_e = float(saldo_local_2)

                    if saldo_total == "":
                        total = 0.00
                    else:
                        total = float(saldo_total)

                    sheet.append([codigu, descr, ref, um, saldo1_e, saldo2_e, total])

                for cell in linhas_colunas_p_edicao(sheet, 1, sheet.max_row, 1, sheet.max_column):
                    edita_bordas(cell)
                    edita_alinhamento(cell)

                for column in sheet.columns:
                    max_length = 0
                    column_letter = letra_coluna(column[0].column)
                    for cell in column:
                        if isinstance(cell.value, (int, float)):
                            cell_value_str = "{:.3f}".format(cell.value)
                        else:
                            cell_value_str = str(cell.value)
                        if len(cell_value_str) > max_length:
                            max_length = len(cell_value_str)

                    adjusted_width = (max_length + 2)
                    sheet.column_dimensions[column_letter].width = adjusted_width

                for cell in linhas_colunas_p_edicao(sheet, 2, sheet.max_row, 7, 9):
                    cell.number_format = '0.000'

                desktop = Path.home() / "Desktop"
                desk_str = str(desktop)
                nome_req = f'\Estoque Final {date_string}.xlsx'
                caminho = (desk_str + nome_req)

                workbook.save(caminho)

                mensagem_alerta(f'Relatório do Estoque Final do dia {date_string} '
                                f'criado com sucesso!!')

                self.table_Estoque.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def gerar_excel_almox(self):
        try:
            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('dd-MM-yyyy')

            extrai_dados_tabela = extrair_tabela(self.table_Estoque)

            workbook = criar_workbook()
            sheet = workbook.active
            sheet.title = "Estoque Final"

            headers = ["Código", "Descrição", "Referência", "UM", "Almox", "Total"]
            sheet.append(headers)

            header_row = sheet[1]
            for cell in header_row:
                edita_fonte(cell, negrito=True)
                edita_preenchimento(cell)
                edita_alinhamento(cell)

            for dados_ex in extrai_dados_tabela:
                codigo, descr, ref, um, saldo_local_1, saldo_total = dados_ex
                codigu = int(codigo)

                if saldo_local_1 == "":
                    saldo1_e = 0.00
                else:
                    saldo1_e = float(saldo_local_1)

                if saldo_total == "":
                    total = 0.00
                else:
                    total = float(saldo_total)

                sheet.append([codigu, descr, ref, um, saldo1_e, total])

            for cell in linhas_colunas_p_edicao(sheet, 1, sheet.max_row, 1, sheet.max_column):
                edita_bordas(cell)
                edita_alinhamento(cell)

            for column in sheet.columns:
                max_length = 0
                column_letter = letra_coluna(column[0].column)
                for cell in column:
                    if isinstance(cell.value, (int, float)):
                        cell_value_str = "{:.3f}".format(cell.value)
                    else:
                        cell_value_str = str(cell.value)
                    if len(cell_value_str) > max_length:
                        max_length = len(cell_value_str)

                adjusted_width = (max_length + 2)
                sheet.column_dimensions[column_letter].width = adjusted_width

            for cell in linhas_colunas_p_edicao(sheet, 2, sheet.max_row, 7, 9):
                cell.number_format = '0.000'

            desktop = Path.home() / "Desktop"
            desk_str = str(desktop)
            nome_req = f'\Estoque Final {date_string}.xlsx'
            caminho = (desk_str + nome_req)

            workbook.save(caminho)

            mensagem_alerta(f'Relatório do Estoque Final do dia {date_string} '
                            f'criado com sucesso!!')

            self.table_Estoque.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)

    def gerar_excel_obsoleto(self):
        try:
            data_rel = self.date_relatorio.date()
            date_string = data_rel.toString('dd-MM-yyyy')
            print(date_string)

            extrai_dados_tabela = extrair_tabela(self.table_Estoque)
            if not extrai_dados_tabela:
                mensagem_alerta(f'A Tabela "Lista de Estoque" está vazia!')
            else:
                workbook = criar_workbook()
                sheet = workbook.active
                sheet.title = "Estoque Final"

                headers = ["Código", "Descrição", "Referência", "UM", "Obsoleto", "Total"]
                sheet.append(headers)

                header_row = sheet[1]
                for cell in header_row:
                    edita_fonte(cell, negrito=True)
                    edita_preenchimento(cell)
                    edita_alinhamento(cell)

                for dados_ex in extrai_dados_tabela:
                    codigo, descr, ref, um, saldo_local_2, saldo_total = dados_ex
                    codigu = int(codigo)

                    if saldo_local_2 == "":
                        saldo2_e = 0.00
                    else:
                        saldo2_e = float(saldo_local_2)

                    if saldo_total == "":
                        total = 0.00
                    else:
                        total = float(saldo_total)

                    sheet.append([codigu, descr, ref, um, saldo2_e, total])

                for cell in linhas_colunas_p_edicao(sheet, 1, sheet.max_row, 1, sheet.max_column):
                    edita_bordas(cell)
                    edita_alinhamento(cell)

                for column in sheet.columns:
                    max_length = 0
                    column_letter = letra_coluna(column[0].column)
                    for cell in column:
                        if isinstance(cell.value, (int, float)):
                            cell_value_str = "{:.3f}".format(cell.value)
                        else:
                            cell_value_str = str(cell.value)
                        if len(cell_value_str) > max_length:
                            max_length = len(cell_value_str)

                    adjusted_width = (max_length + 2)
                    sheet.column_dimensions[column_letter].width = adjusted_width

                for cell in linhas_colunas_p_edicao(sheet, 2, sheet.max_row, 7, 9):
                    cell.number_format = '0.000'

                desktop = Path.home() / "Desktop"
                desk_str = str(desktop)
                nome_req = f'\Estoque Final {date_string}.xlsx'
                caminho = (desk_str + nome_req)

                workbook.save(caminho)

                mensagem_alerta(f'Relatório do Estoque Final do dia {date_string} criado com sucesso!!')

                self.table_Estoque.setRowCount(0)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            tratar_notificar_erros(e, nome_funcao, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaEstEstoque()
    tela.show()
    qt.exec_()
