from PySide6.QtWidgets import *

app = QApplication()
win = QWidget()

id = "id"
pwd = "password"
cnt = 0

def logIn():
    global cnt

    alert = QMessageBox()
    len1 = len(line1.text())
    len2 = len(line2.text())

    if len1 == 0 and len2 == 0:
        alert.setText("id, password를 입력해주세요")
    elif len1 == 0:
        alert.setText("id를 입력해주세요")
    elif len2 == 0:
        alert.setText("password를 입력해주세요")
    else:
        if len2 < 8:
            alert.setText("password는 8글자 이상이어야 합니다")
        else:
            if line1.text() == id and line2.text() == pwd:
                alert.setText("로그인 성공")
                alert.show()
                alert.exec()
                app.exit()
            else:
                alert.setText("로그인 실패")
                cnt += 1
                if cnt == 3:
                    alert.setText("로그인 3회 실패")
                    alert.show()
                    alert.exec()
                    app.exit()

    alert.show()
    alert.exec()

def terminate():
    app.exit()

line1 = QLineEdit(win)
line2 = QLineEdit(win)

btn1 = QPushButton('로그인')
btn1.clicked.connect(logIn)
btn2 = QPushButton('종료')
btn2.clicked.connect(terminate)
hlay = QHBoxLayout()
hlay.addWidget(btn1)
hlay.addWidget(btn2)

form = QFormLayout()
form.addRow('id', line1)
form.addRow('pass', line2)
form.addRow(hlay)
win.setLayout(form)

win.show()
app.exec()