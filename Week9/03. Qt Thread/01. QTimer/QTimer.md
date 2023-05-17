# QTimer

## QTimer의 메서드

- 특정 시간 주기로 Signal을 보내는 객체
  - `QtCore` import 필요

### QTimer에서 자주 사용하는 메서드

- start()
  - 시작
- stop()
  - 일시중지
- setInterval()
  - ms 단위로 시간 단위 설정
- interval()
  - 현재 세팅된 interval 값 리턴
- isActivate()
  - Timer가 동작중인지 True/False

## QTimer 사용순서

1. 객체 생성
2. interval을 설정한다 (ms 단위)
3. timeout signal의 slot 지정
4. timer start 메서드 호출
5. timer stop 종료

``` py
from PySide6.QtWidgets import *
from book_ui import Ui_Form

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

app = QApplication()
win = MyApp()

win.show()
app.exec()
```

## 

``` bash
pyside6-uic.exe ProgressBar.ui -o ProgressBar.py
```
