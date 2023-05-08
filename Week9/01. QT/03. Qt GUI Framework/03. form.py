from PySide6.QtWidgets import *

app = QApplication()
win = QWidget()

mainlay = QVBoxLayout()

form = QFormLayout()
line1 = QLineEdit()
form.addRow("name", line1)
line2 = QLineEdit()
checkbtn = QPushButton('나이확인')

hlay = QHBoxLayout()
hlay.addWidget(line2)
hlay.addWidget(checkbtn)

form.addRow("age", hlay)

lbl = QLabel('안녕')
form.addWidget(lbl)

btn = QPushButton("회원가입")
mainlay.addLayout(form)
mainlay.addWidget(btn)
win.setLayout(mainlay)

win.show()
app.exec()