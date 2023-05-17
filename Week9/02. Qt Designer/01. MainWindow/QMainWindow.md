# QMainWindow

## QMainWindow

- QWidget을 상속받은 하나의 클래스
- QWidget을 기반으로 메뉴 / 상태바 / 툴바 등 자주쓰는 Window 형태를 미리 구현해 둔 클래스
- 메뉴 / 상태표시줄 / 툴바를 쓰기 위해서는 QWidget이 아닌 QMainWindow를 써야 한다

## Qt에서 GUI Window Class 종류

- QWidget
  - GUI의 기본 객체, Window에서 컨트롤 개념
  - 화면에 출력되는 컨트롤을 나타냄
- QDialog
  - 단순한 정보를 알리는 알림 창 / 단순 정보 입력 창 용도로 쓰임
  - 하단에 `확인`, `취소` 버튼이 있음
- QMainWindow
  - 메뉴 / 툴바 / 상태표시줄 / 전용 레이아웃 등을 가지고 있음
  - 보편적인 최상위 Form을 나타냄

## 창의 종류

### Modal 창

- 최상위 Modal 창만 사용 가능
  - 하위 창 제어 불가
- `exec()` 메서드 사용

### Modeless 창

- 최상위 Modal 창 및 하위 창 사용 가능
- `show()` 메서드 사용

## QMainWindow 생성

- QWidget과 동일하게 사용할 수 있다

``` py
from PySide6.QtWidgets import *

app = QApplication()

win = QMainWindow()
win.setGeometry(100, 100, 500, 500)

win.show()
app.exec()
```

## statusBar 추가

- 화면 하단에 표시되는 정보 출력 창

``` py
bar = win.statusBar()
bar.showMessage("메시지 내용.")
```

## menuBar 추가

``` py
menu = win.menuBar()
menu.addMenu("File")
menu.addMenu("Edit")
```

> 메뉴명 앞에 `&` 문자를 추가하면 `Alt + 앞글자` 단축키로 메뉴 접근이 가능해진다

# CentralWidget

## Qt Main Window Framework

- QMainWindow의 Layout 규칙

1. QWidget을 하나 더 만들어야 함
2. 컨트롤 용도 Widget은 Central Widget 영역에 추가하여야 함

## Central Widget 추가

- QWidget을 만들고, MainWindow의 CentralWidget으로 등록

``` py
win = QMainWindow()
win.setGeometry(100, 100, 500, 500)


menu = win.menuBar()
menu.addMenu("File")
menu.addMenu("Edit")

main = QWidget()
win.setCentralWidget(main)

lbl = QLabel("BBQ 맛있다", main)
lbl.adjustSize()
```

# Menu 바 꾸미기

## 하위 메뉴 추가

### QAction

- 메뉴 / 툴바 버튼 / 단축키를 통해 명령을 내릴 수 있는 객체
- QAction에 단축키도 등록할 수 있다
- QtGui를 import 해야 한다

``` py
from PySide6.QtGui import *
```

- Action의 이름과, 소속될 곳을 반드시 입력한다

``` py
menu = win.menuBar()
menuFile = menu.addMenu("File")
menuEdit = menu.addMenu("Edit")

open = QAction("Open", win)
menuFile.addAction(open)
```