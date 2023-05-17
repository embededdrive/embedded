# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 293)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.chartBtn2 = QPushButton(self.centralwidget)
        self.chartBtn2.setObjectName(u"chartBtn2")

        self.gridLayout.addWidget(self.chartBtn2, 1, 1, 1, 1)

        self.chartBtn1 = QPushButton(self.centralwidget)
        self.chartBtn1.setObjectName(u"chartBtn1")

        self.gridLayout.addWidget(self.chartBtn1, 1, 0, 1, 1)

        self.lay = QVBoxLayout()
        self.lay.setObjectName(u"lay")

        self.gridLayout.addLayout(self.lay, 0, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chartBtn1.clicked.connect(MainWindow.chart1)
        self.chartBtn2.clicked.connect(MainWindow.chart2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chartBtn2.setText(QCoreApplication.translate("MainWindow", u"Chart2", None))
        self.chartBtn1.setText(QCoreApplication.translate("MainWindow", u"Chart1", None))
    # retranslateUi

