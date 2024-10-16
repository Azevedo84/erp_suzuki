# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_estrut_versao.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(48, 0))
        self.label_4.setMaximumSize(QtCore.QSize(48, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.line_Num = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Num.sizePolicy().hasHeightForWidth())
        self.line_Num.setSizePolicy(sizePolicy)
        self.line_Num.setMinimumSize(QtCore.QSize(92, 0))
        self.line_Num.setMaximumSize(QtCore.QSize(92, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.horizontalLayout.addWidget(self.line_Num)
        self.label_13 = QtWidgets.QLabel(self.widget)
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
        self.label_11 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.date_Emissao = QtWidgets.QDateEdit(self.widget)
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
        self.horizontalLayout.addWidget(self.date_Emissao)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(450, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Cor1.sizePolicy().hasHeightForWidth())
        self.widget_Cor1.setSizePolicy(sizePolicy)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_Cor1.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 3)
        self.verticalLayout_8.setSpacing(1)
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
        self.label_53 = QtWidgets.QLabel(self.widget_28)
        self.label_53.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_22.addWidget(self.label_53)
        self.verticalLayout_8.addWidget(self.widget_28)
        self.widget_29 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_29.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_29.setStyleSheet("")
        self.widget_29.setObjectName("widget_29")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_29)
        self.horizontalLayout_25.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_57 = QtWidgets.QLabel(self.widget_29)
        self.label_57.setMinimumSize(QtCore.QSize(70, 0))
        self.label_57.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_25.addWidget(self.label_57)
        self.line_Codigo = QtWidgets.QLineEdit(self.widget_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Codigo.sizePolicy().hasHeightForWidth())
        self.line_Codigo.setSizePolicy(sizePolicy)
        self.line_Codigo.setMinimumSize(QtCore.QSize(80, 0))
        self.line_Codigo.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Codigo.setFont(font)
        self.line_Codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Codigo.setPlaceholderText("")
        self.line_Codigo.setObjectName("line_Codigo")
        self.horizontalLayout_25.addWidget(self.line_Codigo)
        self.label_7 = QtWidgets.QLabel(self.widget_29)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_25.addWidget(self.label_7)
        self.label_23 = QtWidgets.QLabel(self.widget_29)
        self.label_23.setMinimumSize(QtCore.QSize(30, 0))
        self.label_23.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_25.addWidget(self.label_23)
        self.line_UM = QtWidgets.QLineEdit(self.widget_29)
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
        self.horizontalLayout_25.addWidget(self.line_UM)
        self.verticalLayout_8.addWidget(self.widget_29)
        self.widget_31 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_31.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_31.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_31.setStyleSheet("")
        self.widget_31.setObjectName("widget_31")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_31)
        self.horizontalLayout_27.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_58 = QtWidgets.QLabel(self.widget_31)
        self.label_58.setMinimumSize(QtCore.QSize(70, 0))
        self.label_58.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_27.addWidget(self.label_58)
        self.line_Referencia = QtWidgets.QLineEdit(self.widget_31)
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
        self.line_Referencia.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Referencia.setObjectName("line_Referencia")
        self.horizontalLayout_27.addWidget(self.line_Referencia)
        self.label_62 = QtWidgets.QLabel(self.widget_31)
        self.label_62.setMinimumSize(QtCore.QSize(0, 0))
        self.label_62.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setText("")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_27.addWidget(self.label_62)
        self.verticalLayout_8.addWidget(self.widget_31)
        self.widget_30 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_30.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_30.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_30.setStyleSheet("")
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_26.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_59 = QtWidgets.QLabel(self.widget_30)
        self.label_59.setMinimumSize(QtCore.QSize(70, 0))
        self.label_59.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_26.addWidget(self.label_59)
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
        self.verticalLayout_2.addWidget(self.widget_Cor1)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_8.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 3)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_32 = QtWidgets.QWidget(self.widget_8)
        self.widget_32.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_32.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_32.setStyleSheet("")
        self.widget_32.setObjectName("widget_32")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.widget_32)
        self.horizontalLayout_28.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_60 = QtWidgets.QLabel(self.widget_32)
        self.label_60.setMinimumSize(QtCore.QSize(70, 0))
        self.label_60.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_28.addWidget(self.label_60)
        self.line_Num_Versao = QtWidgets.QLineEdit(self.widget_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Num_Versao.sizePolicy().hasHeightForWidth())
        self.line_Num_Versao.setSizePolicy(sizePolicy)
        self.line_Num_Versao.setMinimumSize(QtCore.QSize(100, 0))
        self.line_Num_Versao.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Num_Versao.setFont(font)
        self.line_Num_Versao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Num_Versao.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Num_Versao.setObjectName("line_Num_Versao")
        self.horizontalLayout_28.addWidget(self.line_Num_Versao)
        self.label_3 = QtWidgets.QLabel(self.widget_32)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_28.addWidget(self.label_3)
        self.label_65 = QtWidgets.QLabel(self.widget_32)
        self.label_65.setMinimumSize(QtCore.QSize(50, 0))
        self.label_65.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_28.addWidget(self.label_65)
        self.combo_Status = QtWidgets.QComboBox(self.widget_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_Status.sizePolicy().hasHeightForWidth())
        self.combo_Status.setSizePolicy(sizePolicy)
        self.combo_Status.setMinimumSize(QtCore.QSize(110, 0))
        self.combo_Status.setMaximumSize(QtCore.QSize(110, 16777215))
        self.combo_Status.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Status.setObjectName("combo_Status")
        self.combo_Status.addItem("")
        self.combo_Status.setItemText(0, "")
        self.combo_Status.addItem("")
        self.combo_Status.addItem("")
        self.horizontalLayout_28.addWidget(self.combo_Status)
        self.verticalLayout_6.addWidget(self.widget_32)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_Cor6 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Cor6.sizePolicy().hasHeightForWidth())
        self.widget_Cor6.setSizePolicy(sizePolicy)
        self.widget_Cor6.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_Cor6.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_Cor6.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_Cor6.setObjectName("widget_Cor6")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_Cor6)
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_21.setSpacing(1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_24 = QtWidgets.QWidget(self.widget_Cor6)
        self.widget_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_24.setStyleSheet("")
        self.widget_24.setObjectName("widget_24")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_24)
        self.verticalLayout_3.setContentsMargins(5, 3, 5, 3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_24)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_28 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.plain_Obs = QtWidgets.QPlainTextEdit(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plain_Obs.sizePolicy().hasHeightForWidth())
        self.plain_Obs.setSizePolicy(sizePolicy)
        self.plain_Obs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plain_Obs.setObjectName("plain_Obs")
        self.verticalLayout_3.addWidget(self.plain_Obs)
        self.horizontalLayout_21.addWidget(self.widget_24)
        self.verticalLayout_2.addWidget(self.widget_Cor6)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Excluir = QtWidgets.QPushButton(self.widget_3)
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
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.btn_Limpar = QtWidgets.QPushButton(self.widget_3)
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
        self.btn_Salvar = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy)
        self.btn_Salvar.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.horizontalLayout_2.addWidget(self.btn_Salvar)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget_11)
        self.label_5.setMinimumSize(QtCore.QSize(0, 18))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.table_Lista = QtWidgets.QTableWidget(self.widget_11)
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
        self.table_Lista.setColumnCount(6)
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
        self.table_Lista.verticalHeader().setDefaultSectionSize(0)
        self.table_Lista.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_4.addWidget(self.table_Lista)
        self.verticalLayout_5.addWidget(self.widget_11)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle de Versões de Estrutura"))
        self.label_4.setText(_translate("MainWindow", "Código:"))
        self.label_13.setText(_translate("MainWindow", "Cadastro de Versões de Estrutura"))
        self.label_11.setText(_translate("MainWindow", "Data Emissao: "))
        self.label_53.setText(_translate("MainWindow", "Dados do Produto"))
        self.label_57.setText(_translate("MainWindow", "Código:"))
        self.label_23.setText(_translate("MainWindow", "UM:"))
        self.label_58.setText(_translate("MainWindow", "Referência:"))
        self.label_59.setText(_translate("MainWindow", "Descrição:"))
        self.label_60.setText(_translate("MainWindow", "Nº Versão:"))
        self.label_65.setText(_translate("MainWindow", "Status:"))
        self.combo_Status.setItemText(1, _translate("MainWindow", "ATIVO"))
        self.combo_Status.setItemText(2, _translate("MainWindow", "INATIVO"))
        self.label_28.setText(_translate("MainWindow", "Observação:"))
        self.btn_Excluir.setText(_translate("MainWindow", "Excluir"))
        self.btn_Limpar.setText(_translate("MainWindow", "Limpar"))
        self.btn_Salvar.setText(_translate("MainWindow", "Salvar"))
        self.label_5.setText(_translate("MainWindow", "Lista de Versões"))
        item = self.table_Lista.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CÓDIGO"))
        item = self.table_Lista.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nº VERSÃO"))
        item = self.table_Lista.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.table_Lista.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "STATUS"))
        item = self.table_Lista.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OBS"))
        item = self.table_Lista.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CRIAÇÃO"))
