# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_pcp_previsao.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.widget.setMaximumSize(QtCore.QSize(16777215, 240))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_11.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_Cor1 = QtWidgets.QWidget(self.widget_11)
        self.widget_Cor1.setMinimumSize(QtCore.QSize(0, 95))
        self.widget_Cor1.setMaximumSize(QtCore.QSize(16777215, 95))
        self.widget_Cor1.setStyleSheet("")
        self.widget_Cor1.setObjectName("widget_Cor1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_Cor1)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_8 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.date_Inicio = QtWidgets.QDateEdit(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Inicio.sizePolicy().hasHeightForWidth())
        self.date_Inicio.setSizePolicy(sizePolicy)
        self.date_Inicio.setMinimumSize(QtCore.QSize(100, 0))
        self.date_Inicio.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_Inicio.setFont(font)
        self.date_Inicio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Inicio.setObjectName("date_Inicio")
        self.horizontalLayout_11.addWidget(self.date_Inicio)
        self.verticalLayout_6.addWidget(self.widget_8)
        self.widget_17 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.line_Func = QtWidgets.QLineEdit(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Func.sizePolicy().hasHeightForWidth())
        self.line_Func.setSizePolicy(sizePolicy)
        self.line_Func.setMinimumSize(QtCore.QSize(90, 0))
        self.line_Func.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Func.setFont(font)
        self.line_Func.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Func.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Func.setObjectName("line_Func")
        self.horizontalLayout_12.addWidget(self.line_Func)
        self.verticalLayout_6.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_Cor1)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        self.line_HorasDia = QtWidgets.QLineEdit(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_HorasDia.sizePolicy().hasHeightForWidth())
        self.line_HorasDia.setSizePolicy(sizePolicy)
        self.line_HorasDia.setMinimumSize(QtCore.QSize(90, 0))
        self.line_HorasDia.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_HorasDia.setFont(font)
        self.line_HorasDia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_HorasDia.setAlignment(QtCore.Qt.AlignCenter)
        self.line_HorasDia.setObjectName("line_HorasDia")
        self.horizontalLayout_13.addWidget(self.line_HorasDia)
        self.verticalLayout_6.addWidget(self.widget_18)
        self.verticalLayout_4.addWidget(self.widget_Cor1)
        self.widget_Cor2 = QtWidgets.QWidget(self.widget_11)
        self.widget_Cor2.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_Cor2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_Cor2.setStyleSheet("")
        self.widget_Cor2.setObjectName("widget_Cor2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_Cor2)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_70 = QtWidgets.QWidget(self.widget_Cor2)
        self.widget_70.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_70.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_70.setStyleSheet("")
        self.widget_70.setObjectName("widget_70")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_70)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_Atualizar = QtWidgets.QPushButton(self.widget_70)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Atualizar.sizePolicy().hasHeightForWidth())
        self.btn_Atualizar.setSizePolicy(sizePolicy)
        self.btn_Atualizar.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_Atualizar.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Atualizar.setFont(font)
        self.btn_Atualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Atualizar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Atualizar.setAutoFillBackground(False)
        self.btn_Atualizar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Atualizar.setCheckable(False)
        self.btn_Atualizar.setAutoDefault(False)
        self.btn_Atualizar.setDefault(False)
        self.btn_Atualizar.setFlat(False)
        self.btn_Atualizar.setObjectName("btn_Atualizar")
        self.horizontalLayout_4.addWidget(self.btn_Atualizar)
        self.verticalLayout_9.addWidget(self.widget_70)
        self.verticalLayout_4.addWidget(self.widget_Cor2)
        self.widget_Cor3 = QtWidgets.QWidget(self.widget_11)
        self.widget_Cor3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Cor3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_Cor3.setStyleSheet("")
        self.widget_Cor3.setObjectName("widget_Cor3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_Cor3)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_22 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.widget_22)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.date_Final = QtWidgets.QDateEdit(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Final.sizePolicy().hasHeightForWidth())
        self.date_Final.setSizePolicy(sizePolicy)
        self.date_Final.setMinimumSize(QtCore.QSize(110, 0))
        self.date_Final.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_Final.setFont(font)
        self.date_Final.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Final.setAlignment(QtCore.Qt.AlignCenter)
        self.date_Final.setObjectName("date_Final")
        self.horizontalLayout_15.addWidget(self.date_Final)
        self.verticalLayout_7.addWidget(self.widget_22)
        self.widget_23 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_19 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_16.addWidget(self.label_19)
        self.line_Folga = QtWidgets.QLineEdit(self.widget_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Folga.sizePolicy().hasHeightForWidth())
        self.line_Folga.setSizePolicy(sizePolicy)
        self.line_Folga.setMinimumSize(QtCore.QSize(110, 0))
        self.line_Folga.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Folga.setFont(font)
        self.line_Folga.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Folga.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Folga.setObjectName("line_Folga")
        self.horizontalLayout_16.addWidget(self.line_Folga)
        self.verticalLayout_7.addWidget(self.widget_23)
        self.widget_24 = QtWidgets.QWidget(self.widget_Cor3)
        self.widget_24.setStyleSheet("")
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_20 = QtWidgets.QLabel(self.widget_24)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_17.addWidget(self.label_20)
        self.line_TotalItens = QtWidgets.QLineEdit(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_TotalItens.sizePolicy().hasHeightForWidth())
        self.line_TotalItens.setSizePolicy(sizePolicy)
        self.line_TotalItens.setMinimumSize(QtCore.QSize(110, 0))
        self.line_TotalItens.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_TotalItens.setFont(font)
        self.line_TotalItens.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_TotalItens.setAlignment(QtCore.Qt.AlignCenter)
        self.line_TotalItens.setObjectName("line_TotalItens")
        self.horizontalLayout_17.addWidget(self.line_TotalItens)
        self.verticalLayout_7.addWidget(self.widget_24)
        self.verticalLayout_4.addWidget(self.widget_Cor3)
        self.horizontalLayout_3.addWidget(self.widget_11)
        self.widget_Cor4 = QtWidgets.QWidget(self.widget)
        self.widget_Cor4.setStyleSheet("")
        self.widget_Cor4.setObjectName("widget_Cor4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_Cor4)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget_Cor4)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.table_PI = QtWidgets.QTableWidget(self.widget_Cor4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_PI.sizePolicy().hasHeightForWidth())
        self.table_PI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.table_PI.setFont(font)
        self.table_PI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_PI.setObjectName("table_PI")
        self.table_PI.setColumnCount(9)
        self.table_PI.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_PI.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.table_PI)
        self.horizontalLayout_3.addWidget(self.widget_Cor4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_Cor5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor5.setMinimumSize(QtCore.QSize(0, 328))
        self.widget_Cor5.setStyleSheet("")
        self.widget_Cor5.setObjectName("widget_Cor5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_Cor5)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget_Cor5)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.table_Previsao = QtWidgets.QTableWidget(self.widget_Cor5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Previsao.sizePolicy().hasHeightForWidth())
        self.table_Previsao.setSizePolicy(sizePolicy)
        self.table_Previsao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Previsao.setObjectName("table_Previsao")
        self.table_Previsao.setColumnCount(10)
        self.table_Previsao.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Previsao.setHorizontalHeaderItem(9, item)
        self.verticalLayout_5.addWidget(self.table_Previsao)
        self.verticalLayout.addWidget(self.widget_Cor5)
        self.widget_Cor6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cor6.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_Cor6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_Cor6.setStyleSheet("")
        self.widget_Cor6.setObjectName("widget_Cor6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_Cor6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_Barra0 = QtWidgets.QWidget(self.widget_Cor6)
        self.widget_Barra0.setObjectName("widget_Barra0")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_Barra0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_Barra = QtWidgets.QWidget(self.widget_Barra0)
        self.widget_Barra.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_Barra.setObjectName("widget_Barra")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_Barra)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_procura = QtWidgets.QLabel(self.widget_Barra)
        self.label_procura.setMinimumSize(QtCore.QSize(150, 0))
        self.label_procura.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_procura.setFont(font)
        self.label_procura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_procura.setText("")
        self.label_procura.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_procura.setObjectName("label_procura")
        self.horizontalLayout_9.addWidget(self.label_procura)
        self.label_procura1 = QtWidgets.QLabel(self.widget_Barra)
        self.label_procura1.setMinimumSize(QtCore.QSize(120, 0))
        self.label_procura1.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_procura1.setFont(font)
        self.label_procura1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_procura1.setText("")
        self.label_procura1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_procura1.setObjectName("label_procura1")
        self.horizontalLayout_9.addWidget(self.label_procura1)
        self.label_procura2 = QtWidgets.QLabel(self.widget_Barra)
        self.label_procura2.setMinimumSize(QtCore.QSize(250, 0))
        self.label_procura2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_procura2.setFont(font)
        self.label_procura2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_procura2.setText("")
        self.label_procura2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_procura2.setObjectName("label_procura2")
        self.horizontalLayout_9.addWidget(self.label_procura2)
        self.progressBar = QtWidgets.QProgressBar(self.widget_Barra)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.horizontalLayout_7.addWidget(self.widget_Barra)
        self.horizontalLayout_6.addWidget(self.widget_Barra0)
        self.widget_10 = QtWidgets.QWidget(self.widget_Cor6)
        self.widget_10.setMinimumSize(QtCore.QSize(210, 0))
        self.widget_10.setMaximumSize(QtCore.QSize(210, 16777215))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Excel = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Excel.setFont(font)
        self.label_Excel.setText("")
        self.label_Excel.setObjectName("label_Excel")
        self.horizontalLayout_5.addWidget(self.label_Excel)
        self.btn_GeraExcel = QtWidgets.QPushButton(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_GeraExcel.sizePolicy().hasHeightForWidth())
        self.btn_GeraExcel.setSizePolicy(sizePolicy)
        self.btn_GeraExcel.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_GeraExcel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_GeraExcel.setFont(font)
        self.btn_GeraExcel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_GeraExcel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_GeraExcel.setAutoFillBackground(False)
        self.btn_GeraExcel.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_GeraExcel.setCheckable(False)
        self.btn_GeraExcel.setAutoDefault(False)
        self.btn_GeraExcel.setDefault(False)
        self.btn_GeraExcel.setFlat(False)
        self.btn_GeraExcel.setObjectName("btn_GeraExcel")
        self.horizontalLayout_5.addWidget(self.btn_GeraExcel)
        self.horizontalLayout_6.addWidget(self.widget_10)
        self.verticalLayout.addWidget(self.widget_Cor6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Previsão e Materiais Pendentes"))
        self.label_13.setText(_translate("MainWindow", "Previsão de Entrega e Materiais Pendentes"))
        self.label_14.setText(_translate("MainWindow", "     Data de Início:"))
        self.label_15.setText(_translate("MainWindow", "     Nº Funcionários:"))
        self.label_16.setText(_translate("MainWindow", "     Horas p/ Dia:"))
        self.btn_Atualizar.setText(_translate("MainWindow", "Calcular Previsão"))
        self.label_18.setText(_translate("MainWindow", "     Data Final:"))
        self.label_19.setText(_translate("MainWindow", "     Dias de Folga:"))
        self.label_20.setText(_translate("MainWindow", "     Total de Itens:"))
        self.label_7.setText(_translate("MainWindow", "Pedidos Internos Pendentes"))
        item = self.table_PI.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nº PI"))
        item = self.table_PI.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CÓDIGO"))
        item = self.table_PI.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.table_PI.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "REFERÊNCIA"))
        item = self.table_PI.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UM"))
        item = self.table_PI.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "QTDE"))
        item = self.table_PI.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DT LIMITE"))
        item = self.table_PI.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "DT PREVISÃO"))
        item = self.table_PI.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ITENS"))
        self.label_8.setText(_translate("MainWindow", "Lista de Materiais Pendentes"))
        item = self.table_Previsao.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NIVEL"))
        item = self.table_Previsao.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CODIGO"))
        item = self.table_Previsao.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DESCRIÇÃO"))
        item = self.table_Previsao.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "REFERÊNCIA"))
        item = self.table_Previsao.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UM"))
        item = self.table_Previsao.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "QTDE"))
        item = self.table_Previsao.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ENTREGA"))
        item = self.table_Previsao.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CONJUNTO"))
        item = self.table_Previsao.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ORIGEM"))
        item = self.table_Previsao.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ESTRUTURA"))
        self.btn_GeraExcel.setText(_translate("MainWindow", "Gerar Excel"))
