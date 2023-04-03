# 시스템 프로그래밍

## 시스템

- 구성 요소들이 상호작용하는 집합체

### 컴퓨팅 시스템

- CPU, 기억장치, 입출력장치 등이 상호작용을 하는 집합체

### 임베디드 시스템

- 컴퓨팅 시스템 중, 전용 기능을 수행하도록 만들어진 시스템
- PC와 달리 특정목적을 가짐

## 컴퓨팅 시스템

- HW
  - CPU / 메모리
  - 주변장치 (Peripheral)
    - 저장장치
    - Graphic
    - 입출력장치
    - LAN Card
    - USB Interaface

## 컴퓨팅 시스템 구성

- Application Level
  - App
  - Shell
- Middleware Level
  - API
  - Library
- Low Level
  - 리눅스 커널

# 시스템 프로그래밍

- System Call을 사용하여 Application을 개발
  - POSIX
  - Thread Programming

## 모바일 시스템 개발

- 모델마다 OS를 새롭게 개발
- 대규모 Firmware 개발자 필요


# POSIX

## POSIX란?

- OS들이 지원하는 API들의 표준 규격
- IEEE에서 제정
- POSIX 함수 형태는 똑같지만, 내부 구현은 OS마다 다르다
- POSIX API로 개발한 소스코드를 다른 운영체제에서 빌드하면 잘 동작한다

## System Call과 POSIX의 차이

- POSIX
  - OS가 App에게 제공하는 API들의 표준
- System Call
  - 리눅스가 App 개발자들을 위해 제공하는 API

## 과거의 임베디드 시스템

||과거|현재|
|:---:|:---:|:---:|
|APP|전용 OS에 맞게 맞춤제작|System Call API (리눅스)  POSIX API (리눅스, RTOS)|
|OS|맞춤제작 필요|Firmware 자체 제작 기존 만들어진 OS 사용|
|HW|맞춤제작 필요|맞춤제작 필요|

# Low Level 파일입출력

## System Call

- 리눅스 커널에 있는 함수를 사용하기 위한 API
- printf, scanf는 System Call로 만들어졌다

> System Call을 줄여서 시스콜(Syscall)이라고 한다

## Low Level 파일처리 API

- fopen은 Syscall 중 하나인 `open()`로 커널에게 부탁을 한다
- 커널은 모든 장치들을 관리한다

### fopen()

- Syscall을 포함한 Wrapper함수
- High Level API

### open()

- fopen이 사용하는 syscall
- Low Level API

### read()

- fscanf가 사용하는 syscall

### write()

- fprintf가 사용하는 syscall

### close()

- fclose가 사용하는 syscall

## 리눅스에서 파일의 의미

- 리눅스는 모든 장치들을 파일로 관리한다
- 장치파일은 fopen을 쓰면 안되고, Low Level API를 써야만한다


## vi에서 man 확인

- vim에 API 이름을 적는다
- `[page 숫자]`, `shift + k`
  1. Linux Shell Command
  2. System Call
  3. Linux Library
- 필요한 Header File과 함수 Interface를 확인할 수 있다


## 파일 디스크립터

- 한 프로그램이 파일에 접근하려고 할 때, 부여되는 정수

fd = open("파일", O_RDONLY, 0);

fd =
- 0, 1, 2 : 이미 할당됨
- -1 : 파일 없음
  - 시스템이 바쁠경우 안열릴 수도 있으니 에러처리는 필수로 필요하다
- 3부터 할당된다


## open() System Call Argument

`int open([path], [flag:필수옵션 | 추가옵션], [mode])`

### flag

- 필수 옵션
  - O_RDONLY : 읽기
  - O_WRONLY : 쓰기
  - O_RDWR : 읽기 쓰기
- 추가 옵션
  - O_CREAT : 없으면 새로 생성
  - O_APPEND : 덧붙이기
  - O_TRUNC : 파일 내용 제거 후 사용