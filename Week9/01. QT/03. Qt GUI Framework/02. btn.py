from PySide6.QtWidgets import *

app = QApplication()

win = QWidget()

def gogo():
    print(tbox.text())

tbox = QLineEdit(win)
btn = QPushButton('PUSH', win)

hlay = QHBoxLayout()
hlay.addWidget(tbox)
hlay.addWidget(btn)
win.setLayout(hlay)
btn.clicked.connect(gogo)

win.show()

app.exec()