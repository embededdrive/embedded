# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnName = QPushButton(Form)
        self.btnName.setObjectName(u"btnName")

        self.gridLayout.addWidget(self.btnName, 1, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 120, 81, 16))
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.btnColor = QPushButton(Form)
        self.btnColor.setObjectName(u"btnColor")

        self.gridLayout.addWidget(self.btnColor, 1, 1, 1, 1)

        self.btnReset = QPushButton(Form)
        self.btnReset.setObjectName(u"btnReset")

        self.gridLayout.addWidget(self.btnReset, 2, 1, 1, 1)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)
        self.btnName.clicked.connect(Form.showDiagram)
        self.btnColor.clicked.connect(Form.showDiagram)
        self.btnReset.clicked.connect(Form.resetCnt)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnName.setText(QCoreApplication.translate("Form", u"\uc774\ub984\ubcc0\uacbd", None))
        self.label.setText(QCoreApplication.translate("Form", u"Don't Click ME", None))
        self.btnColor.setText(QCoreApplication.translate("Form", u"\uceec\ub7ec\ubcc0\uacbd", None))
        self.btnReset.setText(QCoreApplication.translate("Form", u"\ucd08\uae30\ud654", None))
    # retranslateUi

