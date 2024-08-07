# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_est_estoque.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_cabecalho = QtWidgets.QWidget(self.centralwidget)
        self.widget_cabecalho.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_cabecalho.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_cabecalho.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widget_cabecalho.setObjectName("widget_cabecalho")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_cabecalho)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget_cabecalho)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.verticalLayout.addWidget(self.widget_cabecalho)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget_4)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_Cor1.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_Cor1)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.widget = QtWidgets.QWidget(self.widget_Cor1)
        self.widget.setMinimumSize(QtCore.QSize(0, 30))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setMinimumSize(QtCore.QSize(115, 0))
        self.label_24.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_4.addWidget(self.label_24)
        self.date_relatorio = QtWidgets.QDateEdit(self.widget)
        self.date_relatorio.setMinimumSize(QtCore.QSize(100, 25))
        self.date_relatorio.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_relatorio.setFont(font)
        self.date_relatorio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_relatorio.setAlignment(QtCore.Qt.AlignCenter)
        self.date_relatorio.setObjectName("date_relatorio")
        self.horizontalLayout_4.addWidget(self.date_relatorio)
        self.verticalLayout_4.addWidget(self.widget)
        self.label_25 = QtWidgets.QLabel(self.widget_Cor1)
        self.label_25.setMinimumSize(QtCore.QSize(0, 30))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_4.addWidget(self.label_25)
        self.check_Almox = QtWidgets.QCheckBox(self.widget_Cor1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.check_Almox.setFont(font)
        self.check_Almox.setChecked(True)
        self.check_Almox.setObjectName("check_Almox")
        self.verticalLayout_4.addWidget(self.check_Almox)
        self.check_Obsoleto = QtWidgets.QCheckBox(self.widget_Cor1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.check_Obsoleto.setFont(font)
        self.check_Obsoleto.setChecked(True)
        self.check_Obsoleto.setObjectName("check_Obsoleto")
        self.verticalLayout_4.addWidget(self.check_Obsoleto)
        self.label = QtWidgets.QLabel(self.widget_Cor1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.btn_Gerar_Classifica = QtWidgets.QPushButton(self.widget_Cor1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Gerar_Classifica.sizePolicy().hasHeightForWidth())
        self.btn_Gerar_Classifica.setSizePolicy(sizePolicy)
        self.btn_Gerar_Classifica.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Gerar_Classifica.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Gerar_Classifica.setFont(font)
        self.btn_Gerar_Classifica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Gerar_Classifica.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Gerar_Classifica.setAutoFillBackground(False)
        self.btn_Gerar_Classifica.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Gerar_Classifica.setCheckable(False)
        self.btn_Gerar_Classifica.setAutoDefault(False)
        self.btn_Gerar_Classifica.setDefault(False)
        self.btn_Gerar_Classifica.setFlat(False)
        self.btn_Gerar_Classifica.setObjectName("btn_Gerar_Classifica")
        self.verticalLayout_4.addWidget(self.btn_Gerar_Classifica)
        self.verticalLayout_3.addWidget(self.widget_Cor1)
        self.widget_Cor3 = QtWidgets.QWidget(self.widget_4)
        self.widget_Cor3.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor3.setObjectName("widget_Cor3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_Cor3)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_Cor3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.btn_Gerar_Acinplas = QtWidgets.QPushButton(self.widget_Cor3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Gerar_Acinplas.sizePolicy().hasHeightForWidth())
        self.btn_Gerar_Acinplas.setSizePolicy(sizePolicy)
        self.btn_Gerar_Acinplas.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Gerar_Acinplas.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Gerar_Acinplas.setFont(font)
        self.btn_Gerar_Acinplas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Gerar_Acinplas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Gerar_Acinplas.setAutoFillBackground(False)
        self.btn_Gerar_Acinplas.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Gerar_Acinplas.setCheckable(False)
        self.btn_Gerar_Acinplas.setAutoDefault(False)
        self.btn_Gerar_Acinplas.setDefault(False)
        self.btn_Gerar_Acinplas.setFlat(False)
        self.btn_Gerar_Acinplas.setObjectName("btn_Gerar_Acinplas")
        self.gridLayout_2.addWidget(self.btn_Gerar_Acinplas, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_Cor3)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_Cor3)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_Cor2 = QtWidgets.QWidget(self.widget_2)
        self.widget_Cor2.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_Cor2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Titulo = QtWidgets.QLabel(self.widget_Cor2)
        self.label_Titulo.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName("label_Titulo")
        self.verticalLayout_2.addWidget(self.label_Titulo)
        self.table_Estoque = QtWidgets.QTableWidget(self.widget_Cor2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Estoque.sizePolicy().hasHeightForWidth())
        self.table_Estoque.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_Estoque.setFont(font)
        self.table_Estoque.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Estoque.setObjectName("table_Estoque")
        self.table_Estoque.setColumnCount(7)
        self.table_Estoque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estoque.setHorizontalHeaderItem(6, item)
        self.table_Estoque.horizontalHeader().setDefaultSectionSize(100)
        self.table_Estoque.horizontalHeader().setMinimumSectionSize(39)
        self.table_Estoque.verticalHeader().setDefaultSectionSize(0)
        self.table_Estoque.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_2.addWidget(self.table_Estoque)
        self.horizontalLayout.addWidget(self.widget_Cor2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_Cor4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_Cor4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_Cor4.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor4.setObjectName("widget_Cor4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_Cor4)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_Cor4)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.btn_Limpar = QtWidgets.QPushButton(self.widget_Cor4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Limpar.sizePolicy().hasHeightForWidth())
        self.btn_Limpar.setSizePolicy(sizePolicy)
        self.btn_Limpar.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Limpar.setFont(font)
        self.btn_Limpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Limpar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Limpar.setAutoFillBackground(False)
        self.btn_Limpar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Limpar.setCheckable(False)
        self.btn_Limpar.setAutoDefault(False)
        self.btn_Limpar.setDefault(False)
        self.btn_Limpar.setFlat(False)
        self.btn_Limpar.setObjectName("btn_Limpar")
        self.horizontalLayout_3.addWidget(self.btn_Limpar)
        self.btn_Salvar = QtWidgets.QPushButton(self.widget_Cor4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy)
        self.btn_Salvar.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.horizontalLayout_3.addWidget(self.btn_Salvar)
        self.verticalLayout.addWidget(self.widget_Cor4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatório de Estoque"))
        self.label_13.setText(_translate("MainWindow", "Relatório de Estoque (Físico)"))
        self.label_2.setText(_translate("MainWindow", "Classificação"))
        self.label_24.setText(_translate("MainWindow", "Data Final:"))
        self.label_25.setText(_translate("MainWindow", "Local de Estoque:"))
        self.check_Almox.setText(_translate("MainWindow", "Almox"))
        self.check_Obsoleto.setText(_translate("MainWindow", "Obsoleto"))
        self.btn_Gerar_Classifica.setText(_translate("MainWindow", "Gerar Relatório Classificado"))
        self.label_3.setText(_translate("MainWindow", "Predefinido"))
        self.btn_Gerar_Acinplas.setText(_translate("MainWindow", "Gerar Relatório Acinplas"))
        self.label_Titulo.setText(_translate("MainWindow", "Lista de Estoque"))
        item = self.table_Estoque.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CÓD"))
        item = self.table_Estoque.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.table_Estoque.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "REFERÊNCIA"))
        item = self.table_Estoque.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UM"))
        item = self.table_Estoque.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ALMOX"))
        item = self.table_Estoque.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "OBSOLETO"))
        item = self.table_Estoque.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TOTAL"))
        self.btn_Limpar.setText(_translate("MainWindow", "Limpar"))
        self.btn_Salvar.setText(_translate("MainWindow", "Salvar Excel"))
