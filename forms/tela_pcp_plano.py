# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_pcp_plano.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultaPcp_Prod(object):
    def setupUi(self, ConsultaPcp_Prod):
        ConsultaPcp_Prod.setObjectName("ConsultaPcp_Prod")
        ConsultaPcp_Prod.resize(1073, 796)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConsultaPcp_Prod.sizePolicy().hasHeightForWidth())
        ConsultaPcp_Prod.setSizePolicy(sizePolicy)
        ConsultaPcp_Prod.setMaximumSize(QtCore.QSize(16777215, 16777211))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Desktop/Sem título.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConsultaPcp_Prod.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ConsultaPcp_Prod)
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
        self.widget_cabecalho.setStyleSheet("")
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
        self.verticalLayout.addWidget(self.widget_cabecalho)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(650, 120))
        self.widget_Cor1.setStyleSheet("")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_10 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setMinimumSize(QtCore.QSize(65, 0))
        self.label_12.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.line_Codigo = QtWidgets.QLineEdit(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Codigo.sizePolicy().hasHeightForWidth())
        self.line_Codigo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Codigo.setFont(font)
        self.line_Codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Codigo.setObjectName("line_Codigo")
        self.horizontalLayout_4.addWidget(self.line_Codigo)
        self.btn_Consultar_Cod = QtWidgets.QPushButton(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Consultar_Cod.sizePolicy().hasHeightForWidth())
        self.btn_Consultar_Cod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Consultar_Cod.setFont(font)
        self.btn_Consultar_Cod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Consultar_Cod.setObjectName("btn_Consultar_Cod")
        self.horizontalLayout_4.addWidget(self.btn_Consultar_Cod)
        self.label_16 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.line_Ref = QtWidgets.QLineEdit(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Ref.sizePolicy().hasHeightForWidth())
        self.line_Ref.setSizePolicy(sizePolicy)
        self.line_Ref.setMinimumSize(QtCore.QSize(180, 0))
        self.line_Ref.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Ref.setFont(font)
        self.line_Ref.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Ref.setReadOnly(True)
        self.line_Ref.setObjectName("line_Ref")
        self.horizontalLayout_4.addWidget(self.line_Ref)
        self.label_18 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_4.addWidget(self.label_18)
        self.line_Saldo = QtWidgets.QLineEdit(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Saldo.sizePolicy().hasHeightForWidth())
        self.line_Saldo.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_4.addWidget(self.line_Saldo)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_5.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.widget_11)
        self.label_15.setMinimumSize(QtCore.QSize(65, 0))
        self.label_15.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.line_Descricao = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Descricao.sizePolicy().hasHeightForWidth())
        self.line_Descricao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Descricao.setFont(font)
        self.line_Descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Descricao.setReadOnly(True)
        self.line_Descricao.setObjectName("line_Descricao")
        self.horizontalLayout_5.addWidget(self.line_Descricao)
        self.label_20 = QtWidgets.QLabel(self.widget_11)
        self.label_20.setMinimumSize(QtCore.QSize(65, 0))
        self.label_20.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_5.addWidget(self.label_20)
        self.line_Conjunto = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Conjunto.sizePolicy().hasHeightForWidth())
        self.line_Conjunto.setSizePolicy(sizePolicy)
        self.line_Conjunto.setMinimumSize(QtCore.QSize(210, 0))
        self.line_Conjunto.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Conjunto.setFont(font)
        self.line_Conjunto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Conjunto.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Conjunto.setReadOnly(True)
        self.line_Conjunto.setObjectName("line_Conjunto")
        self.horizontalLayout_5.addWidget(self.line_Conjunto)
        self.verticalLayout_7.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_22 = QtWidgets.QLabel(self.widget_12)
        self.label_22.setMinimumSize(QtCore.QSize(65, 0))
        self.label_22.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_6.addWidget(self.label_22)
        self.line_Compl = QtWidgets.QLineEdit(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Compl.sizePolicy().hasHeightForWidth())
        self.line_Compl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Compl.setFont(font)
        self.line_Compl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Compl.setReadOnly(True)
        self.line_Compl.setObjectName("line_Compl")
        self.horizontalLayout_6.addWidget(self.line_Compl)
        self.label_19 = QtWidgets.QLabel(self.widget_12)
        self.label_19.setMinimumSize(QtCore.QSize(25, 0))
        self.label_19.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.line_UM = QtWidgets.QLineEdit(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.horizontalLayout_6.addWidget(self.line_UM)
        self.label_14 = QtWidgets.QLabel(self.widget_12)
        self.label_14.setMinimumSize(QtCore.QSize(35, 0))
        self.label_14.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.line_Qtde = QtWidgets.QLineEdit(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Qtde.sizePolicy().hasHeightForWidth())
        self.line_Qtde.setSizePolicy(sizePolicy)
        self.line_Qtde.setMinimumSize(QtCore.QSize(80, 0))
        self.line_Qtde.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Qtde.setFont(font)
        self.line_Qtde.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.line_Qtde.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Qtde.setInputMask("")
        self.line_Qtde.setText("")
        self.line_Qtde.setFrame(True)
        self.line_Qtde.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Qtde.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Qtde.setObjectName("line_Qtde")
        self.horizontalLayout_6.addWidget(self.line_Qtde)
        self.btn_Consulta_Estrut = QtWidgets.QPushButton(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Consulta_Estrut.sizePolicy().hasHeightForWidth())
        self.btn_Consulta_Estrut.setSizePolicy(sizePolicy)
        self.btn_Consulta_Estrut.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_Consulta_Estrut.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Consulta_Estrut.setFont(font)
        self.btn_Consulta_Estrut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Consulta_Estrut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Consulta_Estrut.setAutoFillBackground(False)
        self.btn_Consulta_Estrut.setCheckable(False)
        self.btn_Consulta_Estrut.setAutoDefault(False)
        self.btn_Consulta_Estrut.setDefault(False)
        self.btn_Consulta_Estrut.setFlat(False)
        self.btn_Consulta_Estrut.setObjectName("btn_Consulta_Estrut")
        self.horizontalLayout_6.addWidget(self.btn_Consulta_Estrut)
        self.verticalLayout_7.addWidget(self.widget_12)
        self.horizontalLayout_2.addWidget(self.widget_Cor1)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_2.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget)
        self.widget_Cor2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor2.setStyleSheet("")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_Cor2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Titulo = QtWidgets.QLabel(self.widget_Cor2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName("label_Titulo")
        self.verticalLayout_2.addWidget(self.label_Titulo)
        self.table_Estrutura = QtWidgets.QTableWidget(self.widget_Cor2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_Estrutura.setFont(font)
        self.table_Estrutura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Estrutura.setObjectName("table_Estrutura")
        self.table_Estrutura.setColumnCount(7)
        self.table_Estrutura.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Estrutura.setHorizontalHeaderItem(6, item)
        self.verticalLayout_2.addWidget(self.table_Estrutura)
        self.verticalLayout.addWidget(self.widget_Cor2)
        self.widget_Cor3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Cor3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_Cor3.setStyleSheet("")
        self.widget_Cor3.setObjectName("widget_Cor3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_Cor3)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.combo_Classifica = QtWidgets.QComboBox(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_Classifica.setFont(font)
        self.combo_Classifica.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Classifica.setObjectName("combo_Classifica")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.combo_Classifica.addItem("")
        self.verticalLayout_3.addWidget(self.combo_Classifica)
        self.checkBox_Crescente = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_Crescente.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_Crescente.setSizeIncrement(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Crescente.setFont(font)
        self.checkBox_Crescente.setObjectName("checkBox_Crescente")
        self.verticalLayout_3.addWidget(self.checkBox_Crescente)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_24 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_4.addWidget(self.label_24)
        self.combo_Tipo = QtWidgets.QComboBox(self.widget_6)
        self.combo_Tipo.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_Tipo.setFont(font)
        self.combo_Tipo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Tipo.setObjectName("combo_Tipo")
        self.combo_Tipo.addItem("")
        self.verticalLayout_4.addWidget(self.combo_Tipo)
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_Comprados = QtWidgets.QCheckBox(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Comprados.setFont(font)
        self.checkBox_Comprados.setObjectName("checkBox_Comprados")
        self.verticalLayout_5.addWidget(self.checkBox_Comprados)
        self.checkBox_Sem_Saldo = QtWidgets.QCheckBox(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Sem_Saldo.setFont(font)
        self.checkBox_Sem_Saldo.setObjectName("checkBox_Sem_Saldo")
        self.verticalLayout_5.addWidget(self.checkBox_Sem_Saldo)
        self.checkBox_Saldo_Acabado = QtWidgets.QCheckBox(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Saldo_Acabado.setFont(font)
        self.checkBox_Saldo_Acabado.setObjectName("checkBox_Saldo_Acabado")
        self.verticalLayout_5.addWidget(self.checkBox_Saldo_Acabado)
        self.horizontalLayout_3.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_Compra_Pend = QtWidgets.QCheckBox(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Compra_Pend.setFont(font)
        self.checkBox_Compra_Pend.setObjectName("checkBox_Compra_Pend")
        self.verticalLayout_6.addWidget(self.checkBox_Compra_Pend)
        self.checkBox_OP_Pend = QtWidgets.QCheckBox(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_OP_Pend.setFont(font)
        self.checkBox_OP_Pend.setObjectName("checkBox_OP_Pend")
        self.verticalLayout_6.addWidget(self.checkBox_OP_Pend)
        self.widget_2 = QtWidgets.QWidget(self.widget_8)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.btn_Atualizar = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Atualizar.setFont(font)
        self.btn_Atualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Atualizar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Atualizar.setAutoFillBackground(False)
        self.btn_Atualizar.setCheckable(False)
        self.btn_Atualizar.setAutoDefault(False)
        self.btn_Atualizar.setDefault(False)
        self.btn_Atualizar.setFlat(False)
        self.btn_Atualizar.setObjectName("btn_Atualizar")
        self.horizontalLayout_7.addWidget(self.btn_Atualizar)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_Cor3)
        ConsultaPcp_Prod.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConsultaPcp_Prod)
        QtCore.QMetaObject.connectSlotsByName(ConsultaPcp_Prod)

    def retranslateUi(self, ConsultaPcp_Prod):
        _translate = QtCore.QCoreApplication.translate
        ConsultaPcp_Prod.setWindowTitle(_translate("ConsultaPcp_Prod", "PCP - Consulta Produto"))
        self.label_13.setText(_translate("ConsultaPcp_Prod", "Consulta Estrutura do Produto pelo Plano de Produção"))
        self.label_12.setText(_translate("ConsultaPcp_Prod", "Código:"))
        self.btn_Consultar_Cod.setText(_translate("ConsultaPcp_Prod", "Consulta"))
        self.label_16.setText(_translate("ConsultaPcp_Prod", "Referência:"))
        self.label_18.setText(_translate("ConsultaPcp_Prod", "Saldo:"))
        self.label_15.setText(_translate("ConsultaPcp_Prod", "Descrição:"))
        self.label_20.setText(_translate("ConsultaPcp_Prod", "Conjunto:"))
        self.label_22.setText(_translate("ConsultaPcp_Prod", "D. Compl.:"))
        self.label_19.setText(_translate("ConsultaPcp_Prod", "UM:"))
        self.label_14.setText(_translate("ConsultaPcp_Prod", "Qtde:"))
        self.btn_Consulta_Estrut.setText(_translate("ConsultaPcp_Prod", "Estrutura"))
        self.label_Titulo.setText(_translate("ConsultaPcp_Prod", "Estrutura"))
        item = self.table_Estrutura.horizontalHeaderItem(0)
        item.setText(_translate("ConsultaPcp_Prod", "CÓD."))
        item = self.table_Estrutura.horizontalHeaderItem(1)
        item.setText(_translate("ConsultaPcp_Prod", "DESCRIÇÃO"))
        item = self.table_Estrutura.horizontalHeaderItem(2)
        item.setText(_translate("ConsultaPcp_Prod", "REFERÊNCIA"))
        item = self.table_Estrutura.horizontalHeaderItem(3)
        item.setText(_translate("ConsultaPcp_Prod", "UM"))
        item = self.table_Estrutura.horizontalHeaderItem(4)
        item.setText(_translate("ConsultaPcp_Prod", "QTDE"))
        item = self.table_Estrutura.horizontalHeaderItem(5)
        item.setText(_translate("ConsultaPcp_Prod", "TIPO MATERIAL"))
        item = self.table_Estrutura.horizontalHeaderItem(6)
        item.setText(_translate("ConsultaPcp_Prod", "SALDO"))
        self.label_25.setText(_translate("ConsultaPcp_Prod", "Classificar Por:"))
        self.combo_Classifica.setItemText(0, _translate("ConsultaPcp_Prod", "CÓD."))
        self.combo_Classifica.setItemText(1, _translate("ConsultaPcp_Prod", "DESCRIÇÃO"))
        self.combo_Classifica.setItemText(2, _translate("ConsultaPcp_Prod", "REFERÊNCIA"))
        self.combo_Classifica.setItemText(3, _translate("ConsultaPcp_Prod", "UM"))
        self.combo_Classifica.setItemText(4, _translate("ConsultaPcp_Prod", "QTDE"))
        self.combo_Classifica.setItemText(5, _translate("ConsultaPcp_Prod", "TIPO DE MATERIAL"))
        self.combo_Classifica.setItemText(6, _translate("ConsultaPcp_Prod", "SALDO"))
        self.checkBox_Crescente.setText(_translate("ConsultaPcp_Prod", "Ordem Crescente"))
        self.label_24.setText(_translate("ConsultaPcp_Prod", "Tipo de Material:"))
        self.combo_Tipo.setItemText(0, _translate("ConsultaPcp_Prod", "0 - TODOS"))
        self.checkBox_Comprados.setText(_translate("ConsultaPcp_Prod", "Materiais Comprados"))
        self.checkBox_Sem_Saldo.setText(_translate("ConsultaPcp_Prod", "Materiais sem Saldo"))
        self.checkBox_Saldo_Acabado.setText(_translate("ConsultaPcp_Prod", "Saldo Produto Acabado"))
        self.checkBox_Compra_Pend.setText(_translate("ConsultaPcp_Prod", "Compras Pendentes"))
        self.checkBox_OP_Pend.setText(_translate("ConsultaPcp_Prod", "OP\'s Pendentes"))
        self.btn_Atualizar.setText(_translate("ConsultaPcp_Prod", "Atualizar"))
