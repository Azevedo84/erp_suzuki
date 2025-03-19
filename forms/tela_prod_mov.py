# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_prod_mov.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1098, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_cabecalho = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_cabecalho.sizePolicy().hasHeightForWidth())
        self.widget_cabecalho.setSizePolicy(sizePolicy)
        self.widget_cabecalho.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_cabecalho.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_cabecalho.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widget_cabecalho.setObjectName("widget_cabecalho")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_cabecalho)
        self.horizontalLayout.setContentsMargins(15, 6, 15, 6)
        self.horizontalLayout.setSpacing(0)
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
        self.verticalLayout_2.addWidget(self.widget_cabecalho)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 101))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 101))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Cor1.sizePolicy().hasHeightForWidth())
        self.widget_Cor1.setSizePolicy(sizePolicy)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_Cor1.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(6, 5, 6, 5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(75, 0))
        self.label_12.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.line_Codigo = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Codigo.sizePolicy().hasHeightForWidth())
        self.line_Codigo.setSizePolicy(sizePolicy)
        self.line_Codigo.setMaximumSize(QtCore.QSize(95, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Codigo.setFont(font)
        self.line_Codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Codigo.setObjectName("line_Codigo")
        self.horizontalLayout_2.addWidget(self.line_Codigo)
        self.label_19 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.line_UM = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_UM.sizePolicy().hasHeightForWidth())
        self.line_UM.setSizePolicy(sizePolicy)
        self.line_UM.setMinimumSize(QtCore.QSize(40, 0))
        self.line_UM.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_UM.setFont(font)
        self.line_UM.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.line_UM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_UM.setInputMask("")
        self.line_UM.setText("")
        self.line_UM.setFrame(True)
        self.line_UM.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_UM.setAlignment(QtCore.Qt.AlignCenter)
        self.line_UM.setReadOnly(True)
        self.line_UM.setObjectName("line_UM")
        self.horizontalLayout_2.addWidget(self.line_UM)
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.line_Referencia = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Referencia.sizePolicy().hasHeightForWidth())
        self.line_Referencia.setSizePolicy(sizePolicy)
        self.line_Referencia.setMinimumSize(QtCore.QSize(250, 0))
        self.line_Referencia.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Referencia.setFont(font)
        self.line_Referencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Referencia.setReadOnly(True)
        self.line_Referencia.setObjectName("line_Referencia")
        self.horizontalLayout_2.addWidget(self.line_Referencia)
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.line_Saldo = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Saldo.sizePolicy().hasHeightForWidth())
        self.line_Saldo.setSizePolicy(sizePolicy)
        self.line_Saldo.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Saldo.setFont(font)
        self.line_Saldo.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.line_Saldo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Saldo.setInputMask("")
        self.line_Saldo.setText("")
        self.line_Saldo.setFrame(True)
        self.line_Saldo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Saldo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Saldo.setReadOnly(True)
        self.line_Saldo.setObjectName("line_Saldo")
        self.horizontalLayout_2.addWidget(self.line_Saldo)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_7 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(6, 5, 6, 5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(75, 0))
        self.label_15.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.line_Descricao = QtWidgets.QLineEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Descricao.sizePolicy().hasHeightForWidth())
        self.line_Descricao.setSizePolicy(sizePolicy)
        self.line_Descricao.setMinimumSize(QtCore.QSize(345, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Descricao.setFont(font)
        self.line_Descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Descricao.setReadOnly(True)
        self.line_Descricao.setObjectName("line_Descricao")
        self.horizontalLayout_3.addWidget(self.line_Descricao)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(6, 5, 6, 5)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(75, 0))
        self.label_22.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.line_DescrCompl = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_DescrCompl.sizePolicy().hasHeightForWidth())
        self.line_DescrCompl.setSizePolicy(sizePolicy)
        self.line_DescrCompl.setMinimumSize(QtCore.QSize(345, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_DescrCompl.setFont(font)
        self.line_DescrCompl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_DescrCompl.setReadOnly(True)
        self.line_DescrCompl.setObjectName("line_DescrCompl")
        self.horizontalLayout_4.addWidget(self.line_DescrCompl)
        self.label_20 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.line_Conjunto = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Conjunto.sizePolicy().hasHeightForWidth())
        self.line_Conjunto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Conjunto.setFont(font)
        self.line_Conjunto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Conjunto.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Conjunto.setReadOnly(True)
        self.line_Conjunto.setObjectName("line_Conjunto")
        self.horizontalLayout_4.addWidget(self.line_Conjunto)
        self.verticalLayout.addWidget(self.widget_6)
        self.horizontalLayout_6.addWidget(self.widget_Cor1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.btn_Excluir = QtWidgets.QPushButton(self.widget_2)
        self.btn_Excluir.setGeometry(QtCore.QRect(70, 30, 120, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy)
        self.btn_Excluir.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_Excluir.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Excluir.setFont(font)
        self.btn_Excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Excluir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Excluir.setAutoFillBackground(False)
        self.btn_Excluir.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Excluir.setCheckable(False)
        self.btn_Excluir.setAutoDefault(False)
        self.btn_Excluir.setDefault(False)
        self.btn_Excluir.setFlat(False)
        self.btn_Excluir.setObjectName("btn_Excluir")
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_Cor2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor2.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_Cor2)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_Mov = QtWidgets.QTableWidget(self.widget_Cor2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Mov.sizePolicy().hasHeightForWidth())
        self.table_Mov.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_Mov.setFont(font)
        self.table_Mov.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Mov.setObjectName("table_Mov")
        self.table_Mov.setColumnCount(10)
        self.table_Mov.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Mov.setHorizontalHeaderItem(9, item)
        self.verticalLayout_3.addWidget(self.table_Mov)
        self.verticalLayout_2.addWidget(self.widget_Cor2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movimentação de Produtos"))
        self.label_13.setText(_translate("MainWindow", "Movimentação"))
        self.label_12.setText(_translate("MainWindow", "Código:"))
        self.label_19.setText(_translate("MainWindow", "UM:"))
        self.label_16.setText(_translate("MainWindow", "Referência:"))
        self.label_18.setText(_translate("MainWindow", "Saldo:"))
        self.label_15.setText(_translate("MainWindow", "Descrição:"))
        self.label_22.setText(_translate("MainWindow", "D. Compl.:"))
        self.label_20.setText(_translate("MainWindow", "Conjunto:"))
        self.btn_Excluir.setText(_translate("MainWindow", "Excluir Movimento"))
        item = self.table_Mov.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.table_Mov.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "L. ESTOQUE"))
        item = self.table_Mov.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ENTRADA"))
        item = self.table_Mov.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SAÍDA"))
        item = self.table_Mov.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SALDO"))
        item = self.table_Mov.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "REGISTRO"))
        item = self.table_Mov.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "OC/OV"))
        item = self.table_Mov.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CFOP"))
        item = self.table_Mov.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "SOLICITANTE"))
        item = self.table_Mov.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "OBS"))
