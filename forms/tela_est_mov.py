# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_est_mov.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultaOP(object):
    def setupUi(self, ConsultaOP):
        ConsultaOP.setObjectName("ConsultaOP")
        ConsultaOP.resize(1117, 728)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConsultaOP.sizePolicy().hasHeightForWidth())
        ConsultaOP.setSizePolicy(sizePolicy)
        ConsultaOP.setMaximumSize(QtCore.QSize(16777215, 16777211))
        self.centralwidget = QtWidgets.QWidget(ConsultaOP)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_cabecalho = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_cabecalho.sizePolicy().hasHeightForWidth())
        self.widget_cabecalho.setSizePolicy(sizePolicy)
        self.widget_cabecalho.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_cabecalho.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.widget_cabecalho.setFont(font)
        self.widget_cabecalho.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widget_cabecalho.setObjectName("widget_cabecalho")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_cabecalho)
        self.horizontalLayout.setContentsMargins(15, 6, 15, 6)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.widget_cabecalho)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.verticalLayout.addWidget(self.widget_cabecalho)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget_2)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_Cor1.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.date_Inicio = QtWidgets.QDateEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Inicio.sizePolicy().hasHeightForWidth())
        self.date_Inicio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_Inicio.setFont(font)
        self.date_Inicio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Inicio.setAlignment(QtCore.Qt.AlignCenter)
        self.date_Inicio.setObjectName("date_Inicio")
        self.horizontalLayout_3.addWidget(self.date_Inicio)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.date_Final = QtWidgets.QDateEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Final.sizePolicy().hasHeightForWidth())
        self.date_Final.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_Final.setFont(font)
        self.date_Final.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Final.setAlignment(QtCore.Qt.AlignCenter)
        self.date_Final.setObjectName("date_Final")
        self.horizontalLayout_4.addWidget(self.date_Final)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.btn_Conultar = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Conultar.sizePolicy().hasHeightForWidth())
        self.btn_Conultar.setSizePolicy(sizePolicy)
        self.btn_Conultar.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_Conultar.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Conultar.setFont(font)
        self.btn_Conultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Conultar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Conultar.setObjectName("btn_Conultar")
        self.horizontalLayout_5.addWidget(self.btn_Conultar)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.horizontalLayout_2.addWidget(self.widget_Cor1)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radio_Almox = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_Almox.sizePolicy().hasHeightForWidth())
        self.radio_Almox.setSizePolicy(sizePolicy)
        self.radio_Almox.setMinimumSize(QtCore.QSize(100, 0))
        self.radio_Almox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radio_Almox.setFont(font)
        self.radio_Almox.setChecked(True)
        self.radio_Almox.setObjectName("radio_Almox")
        self.horizontalLayout_8.addWidget(self.radio_Almox)
        self.radio_Todos = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_Todos.sizePolicy().hasHeightForWidth())
        self.radio_Todos.setSizePolicy(sizePolicy)
        self.radio_Todos.setMinimumSize(QtCore.QSize(100, 0))
        self.radio_Todos.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radio_Todos.setFont(font)
        self.radio_Todos.setChecked(False)
        self.radio_Todos.setObjectName("radio_Todos")
        self.horizontalLayout_8.addWidget(self.radio_Todos)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.widget)
        self.label_Msg = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Msg.setFont(font)
        self.label_Msg.setText("")
        self.label_Msg.setObjectName("label_Msg")
        self.verticalLayout_3.addWidget(self.label_Msg)
        self.widget_Progress = QtWidgets.QWidget(self.widget_5)
        self.widget_Progress.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_Progress.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_Progress.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Progress.setObjectName("widget_Progress")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_Progress)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.widget_Progress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.verticalLayout_3.addWidget(self.widget_Progress)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_Cor2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor2.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_Cor2)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Titulo = QtWidgets.QLabel(self.widget_Cor2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName("label_Titulo")
        self.verticalLayout_4.addWidget(self.label_Titulo)
        self.table_OP = QtWidgets.QTableWidget(self.widget_Cor2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_OP.setFont(font)
        self.table_OP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_OP.setObjectName("table_OP")
        self.table_OP.setColumnCount(13)
        self.table_OP.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_OP.setHorizontalHeaderItem(12, item)
        self.verticalLayout_4.addWidget(self.table_OP)
        self.verticalLayout.addWidget(self.widget_Cor2)
        self.widget_Cor3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor3.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor3.setObjectName("widget_Cor3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_Cor3)
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget_Cor3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.label_Excel = QtWidgets.QLabel(self.widget_Cor3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Excel.setFont(font)
        self.label_Excel.setText("")
        self.label_Excel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Excel.setObjectName("label_Excel")
        self.horizontalLayout_6.addWidget(self.label_Excel)
        self.btn_Salvar = QtWidgets.QPushButton(self.widget_Cor3)
        self.btn_Salvar.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_Salvar.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.horizontalLayout_6.addWidget(self.btn_Salvar)
        self.verticalLayout.addWidget(self.widget_Cor3)
        ConsultaOP.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConsultaOP)
        QtCore.QMetaObject.connectSlotsByName(ConsultaOP)

    def retranslateUi(self, ConsultaOP):
        _translate = QtCore.QCoreApplication.translate
        ConsultaOP.setWindowTitle(_translate("ConsultaOP", "Movimentação do Estoque"))
        self.label_13.setText(_translate("ConsultaOP", "Relatório de Movimentação do Estoque"))
        self.label.setText(_translate("ConsultaOP", "Data Inicial"))
        self.label_2.setText(_translate("ConsultaOP", "Data Final"))
        self.btn_Conultar.setText(_translate("ConsultaOP", "Consultar"))
        self.radio_Almox.setText(_translate("ConsultaOP", "Almox"))
        self.radio_Todos.setText(_translate("ConsultaOP", "Todos"))
        self.label_Titulo.setText(_translate("ConsultaOP", "Movimentação"))
        item = self.table_OP.horizontalHeaderItem(0)
        item.setText(_translate("ConsultaOP", "DATA"))
        item = self.table_OP.horizontalHeaderItem(1)
        item.setText(_translate("ConsultaOP", "CÓD."))
        item = self.table_OP.horizontalHeaderItem(2)
        item.setText(_translate("ConsultaOP", "DESCRIÇÃO"))
        item = self.table_OP.horizontalHeaderItem(3)
        item.setText(_translate("ConsultaOP", "REFERÊNCIA"))
        item = self.table_OP.horizontalHeaderItem(4)
        item.setText(_translate("ConsultaOP", "UM"))
        item = self.table_OP.horizontalHeaderItem(5)
        item.setText(_translate("ConsultaOP", "ENTRADA"))
        item = self.table_OP.horizontalHeaderItem(6)
        item.setText(_translate("ConsultaOP", "SAIDA"))
        item = self.table_OP.horizontalHeaderItem(7)
        item.setText(_translate("ConsultaOP", "SALDO"))
        item = self.table_OP.horizontalHeaderItem(8)
        item.setText(_translate("ConsultaOP", "OS/NF/CI"))
        item = self.table_OP.horizontalHeaderItem(9)
        item.setText(_translate("ConsultaOP", "CFOP"))
        item = self.table_OP.horizontalHeaderItem(10)
        item.setText(_translate("ConsultaOP", "LOCAL"))
        item = self.table_OP.horizontalHeaderItem(11)
        item.setText(_translate("ConsultaOP", "SOLICITANTE"))
        item = self.table_OP.horizontalHeaderItem(12)
        item.setText(_translate("ConsultaOP", "OBS"))
        self.btn_Salvar.setText(_translate("ConsultaOP", "Salvar\n"
"Excel"))
