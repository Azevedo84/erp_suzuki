# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_op_excluir.ui'
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
        MainWindow.setStyleSheet("")
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_cabecalho)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.widget_cabecalho)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.verticalLayout.addWidget(self.widget_cabecalho)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(375, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(375, 16777215))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Cor1.sizePolicy().hasHeightForWidth())
        self.widget_Cor1.setSizePolicy(sizePolicy)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(16777215, 170))
        self.widget_Cor1.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_28 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_28.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_28.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget_28.setStyleSheet("")
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_22.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_22.setSpacing(3)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_54 = QtWidgets.QLabel(self.widget_28)
        self.label_54.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_22.addWidget(self.label_54)
        self.verticalLayout_8.addWidget(self.widget_28)
        self.widget_31 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_31.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_31.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_31.setStyleSheet("")
        self.widget_31.setObjectName("widget_31")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_31)
        self.horizontalLayout_27.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_10 = QtWidgets.QLabel(self.widget_31)
        self.label_10.setMinimumSize(QtCore.QSize(65, 0))
        self.label_10.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_27.addWidget(self.label_10)
        self.line_Num = QtWidgets.QLineEdit(self.widget_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Num.sizePolicy().hasHeightForWidth())
        self.line_Num.setSizePolicy(sizePolicy)
        self.line_Num.setMinimumSize(QtCore.QSize(70, 0))
        self.line_Num.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Num.setFont(font)
        self.line_Num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Num.setInputMask("")
        self.line_Num.setText("")
        self.line_Num.setFrame(True)
        self.line_Num.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Num.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Num.setDragEnabled(False)
        self.line_Num.setPlaceholderText("")
        self.line_Num.setObjectName("line_Num")
        self.horizontalLayout_27.addWidget(self.line_Num)
        self.label_3 = QtWidgets.QLabel(self.widget_31)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_27.addWidget(self.label_3)
        self.label_12 = QtWidgets.QLabel(self.widget_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_27.addWidget(self.label_12)
        self.date_Emissao = QtWidgets.QDateEdit(self.widget_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Emissao.sizePolicy().hasHeightForWidth())
        self.date_Emissao.setSizePolicy(sizePolicy)
        self.date_Emissao.setMinimumSize(QtCore.QSize(101, 0))
        self.date_Emissao.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_Emissao.setFont(font)
        self.date_Emissao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Emissao.setAlignment(QtCore.Qt.AlignCenter)
        self.date_Emissao.setObjectName("date_Emissao")
        self.horizontalLayout_27.addWidget(self.date_Emissao)
        self.verticalLayout_8.addWidget(self.widget_31)
        self.widget_29 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_29.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_29.setStyleSheet("")
        self.widget_29.setObjectName("widget_29")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_29)
        self.horizontalLayout_25.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_60 = QtWidgets.QLabel(self.widget_29)
        self.label_60.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_25.addWidget(self.label_60)
        self.line_Codigo = QtWidgets.QLineEdit(self.widget_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Codigo.sizePolicy().hasHeightForWidth())
        self.line_Codigo.setSizePolicy(sizePolicy)
        self.line_Codigo.setMinimumSize(QtCore.QSize(70, 0))
        self.line_Codigo.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Codigo.setFont(font)
        self.line_Codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Codigo.setObjectName("line_Codigo")
        self.horizontalLayout_25.addWidget(self.line_Codigo)
        self.label_61 = QtWidgets.QLabel(self.widget_29)
        self.label_61.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_25.addWidget(self.label_61)
        self.line_Referencia = QtWidgets.QLineEdit(self.widget_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Referencia.sizePolicy().hasHeightForWidth())
        self.line_Referencia.setSizePolicy(sizePolicy)
        self.line_Referencia.setMinimumSize(QtCore.QSize(0, 0))
        self.line_Referencia.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Referencia.setFont(font)
        self.line_Referencia.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.line_Referencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Referencia.setInputMask("")
        self.line_Referencia.setText("")
        self.line_Referencia.setMaxLength(20)
        self.line_Referencia.setFrame(True)
        self.line_Referencia.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Referencia.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Referencia.setObjectName("line_Referencia")
        self.horizontalLayout_25.addWidget(self.line_Referencia)
        self.verticalLayout_8.addWidget(self.widget_29)
        self.widget_30 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_30.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_30.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_30.setStyleSheet("")
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_26.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_62 = QtWidgets.QLabel(self.widget_30)
        self.label_62.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_26.addWidget(self.label_62)
        self.line_Descricao = QtWidgets.QLineEdit(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Descricao.sizePolicy().hasHeightForWidth())
        self.line_Descricao.setSizePolicy(sizePolicy)
        self.line_Descricao.setMinimumSize(QtCore.QSize(0, 0))
        self.line_Descricao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Descricao.setFont(font)
        self.line_Descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Descricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Descricao.setObjectName("line_Descricao")
        self.horizontalLayout_26.addWidget(self.line_Descricao)
        self.verticalLayout_8.addWidget(self.widget_30)
        self.widget_33 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_33.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_33.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_33.setStyleSheet("")
        self.widget_33.setObjectName("widget_33")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_33)
        self.horizontalLayout_13.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_24 = QtWidgets.QLabel(self.widget_33)
        self.label_24.setMinimumSize(QtCore.QSize(65, 0))
        self.label_24.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.line_UM = QtWidgets.QLineEdit(self.widget_33)
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
        self.line_UM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_UM.setAlignment(QtCore.Qt.AlignCenter)
        self.line_UM.setObjectName("line_UM")
        self.horizontalLayout_13.addWidget(self.line_UM)
        self.label_34 = QtWidgets.QLabel(self.widget_33)
        self.label_34.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_13.addWidget(self.label_34)
        self.line_Qtde = QtWidgets.QLineEdit(self.widget_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Qtde.sizePolicy().hasHeightForWidth())
        self.line_Qtde.setSizePolicy(sizePolicy)
        self.line_Qtde.setMinimumSize(QtCore.QSize(85, 0))
        self.line_Qtde.setMaximumSize(QtCore.QSize(85, 16777215))
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
        self.horizontalLayout_13.addWidget(self.line_Qtde)
        self.label_8 = QtWidgets.QLabel(self.widget_33)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget_33)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.verticalLayout_8.addWidget(self.widget_33)
        self.verticalLayout_3.addWidget(self.widget_Cor1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_Cor2 = QtWidgets.QWidget(self.widget_4)
        self.widget_Cor2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_Cor2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_Cor2.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_Cor2)
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Limpar = QtWidgets.QPushButton(self.widget_Cor2)
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
        self.horizontalLayout_2.addWidget(self.btn_Limpar)
        self.label = QtWidgets.QLabel(self.widget_Cor2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.btn_Excluir = QtWidgets.QPushButton(self.widget_Cor2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy)
        self.btn_Excluir.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
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
        self.horizontalLayout_2.addWidget(self.btn_Excluir)
        self.verticalLayout_2.addWidget(self.widget_Cor2)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_Cor3 = QtWidgets.QWidget(self.widget_2)
        self.widget_Cor3.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor3.setObjectName("widget_Cor3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_Cor3)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_Cor3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.table_Lista = QtWidgets.QTableWidget(self.widget_Cor3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Lista.sizePolicy().hasHeightForWidth())
        self.table_Lista.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.table_Lista.setFont(font)
        self.table_Lista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Lista.setObjectName("table_Lista")
        self.table_Lista.setColumnCount(9)
        self.table_Lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(8, item)
        self.table_Lista.verticalHeader().setDefaultSectionSize(0)
        self.table_Lista.verticalHeader().setMinimumSectionSize(0)
        self.gridLayout.addWidget(self.table_Lista, 1, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.widget_Cor3)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excluir Ordens de Produção"))
        self.label_13.setText(_translate("MainWindow", "Excluir Ordens de Produção"))
        self.label_54.setText(_translate("MainWindow", "Dados Produto OP"))
        self.label_10.setText(_translate("MainWindow", "Nº OP:"))
        self.label_12.setText(_translate("MainWindow", "Data Emissao: "))
        self.label_60.setText(_translate("MainWindow", "Código:"))
        self.label_61.setText(_translate("MainWindow", "Referência:"))
        self.label_62.setText(_translate("MainWindow", "Descrição:"))
        self.label_24.setText(_translate("MainWindow", "UM:"))
        self.label_34.setText(_translate("MainWindow", "Qtde:"))
        self.btn_Limpar.setText(_translate("MainWindow", "Limpar"))
        self.btn_Excluir.setText(_translate("MainWindow", "Excluir OP"))
        self.label_5.setText(_translate("MainWindow", "Lista de OP\'S Abertas sem Consumo"))
        item = self.table_Lista.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "EMISSÃO"))
        item = self.table_Lista.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PREVISÃO"))
        item = self.table_Lista.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nº OP"))
        item = self.table_Lista.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CÓD."))
        item = self.table_Lista.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.table_Lista.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "REFERÊNCIA"))
        item = self.table_Lista.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "UM"))
        item = self.table_Lista.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "QTDE"))
        item = self.table_Lista.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "EST/CON"))
