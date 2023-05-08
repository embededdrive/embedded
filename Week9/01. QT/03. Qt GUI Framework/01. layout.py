from PySide6.QtWidgets import *

app = QApplication()

win = QWidget()

hbtn1 = QPushButton('ONE')
hbtn2 = QPushButton('TWO')
hbtn3 = QPushButton('THREE')

vbtn1 = QPushButton('ONE')
vbtn2 = QPushButton('TWO')
vbtn3 = QPushButton('THREE')

headLayout = QHBoxLayout()
bodyLayout = QVBoxLayout()

headLayout.addWidget(hbtn1)
headLayout.addWidget(hbtn2)
headLayout.addWidget(hbtn3)
bodyLayout.addWidget(vbtn1)
bodyLayout.addWidget(vbtn2)
bodyLayout.addWidget(vbtn3)

mainLayout = QVBoxLayout()

mainLayout.addLayout(headLayout)
mainLayout.addLayout(bodyLayout)

win.setLayout(mainLayout)
win.show()

app.exec()