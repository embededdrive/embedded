# 쉘 (Shell)

## shell의 이해

### 인터페이스란?

- 사용자가 쉽게 동작 및 사용하는데 도움을 주는 시스템
  - HW Interface
    - 물리적 접점
  - SW Interface
    - API 소스코드 접근 형태
    - 추상화 구현


### Shell 이란?

- 시스템 사용자가 `커널`을 다룰 수 있도록 도와주는 `인터페이스`.
- 컴퓨터를 켜면 OS가 부팅된 후, 실행되는 프로그램
  - 시스템 사용자는 Shell을 통해 명령을 커널에 던지고 명령에 대한 결과를 확인한다

> 컴퓨터 유저는 커널을 직접 다루지 않고 shell을 이용해서 다루고 있었다

- Shell은 무조건 글자 기반이 아니다.
  - CLI (Command-Line Interface) Shell
    - 글자 기반 인터페이스
  - GUI (Graphical User Interface) Shell
    - 그래픽 기반 인터페이스

### Shell의 정확한 의미

- 쉘은 프로그램이다
- 운영체제 내부에 접근하기 위한 프로그램
- "커널을 감싼다" 라는 의미에서 "shell(=껍데기)"라는 용어를 사용

> 명령 프롬프트 (cmd) App은 MS-DOS에서 사용하든 CLI Shell을 모방해서 만든 Windows의 `CLI Shell` 이다