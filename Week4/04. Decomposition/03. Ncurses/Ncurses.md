# 엔컬즈스 (ncurses)

- new curses
- CLI로 GUI같은 App을 만들고자 할 떄 사용하는 라이브러리
- ex) raspi-config, menu config, htop

## ncurses 설치

``` Shell
$ sudo apt install libncursesw5-dev
```

## ncurses 빌드

``` Shell
$ gcc ./main.c -o ./main -lncursesw
```

## ncurses 명령어

- `initscr()`
  - ncurses시작을 위한 내부 세팅
- `printw([문자열])`
  - 문자열 출력 명령어
- `refresh()`
  - 화면 갱신 명령어
  - printw를 수행한뒤 화면에 글씨를 출력할 때 사용한다
- `clear()`
  - 화면 전체를 지운다
- `getch()`
  - 키입력을 받는 명령어
  - 키를 받기 전까지는 프로그램이 종료되지 않는다
- `endwin()`
  - ncurses 종료를 위한 내부 정리