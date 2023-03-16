# 리눅스 환경 설정

## 터미널

### Video Terminal

- 모니터 + 키보드로 되어있는 콘솔 (H/W) 장치에서 어떤 S/W 적인 판단을 하지 않고, 입력시 내부로 쏴주고, 결과를 눈으로 보여주기만 하는 통신의 말단, 종착역 역할

### Therminal emulator (Term)

- Video Terminal을 가상으로 만든 것.
- GUI OS 내부에 있는 term을 Terminal Window이라고 한다.



## 터미널 단축키

- ### 화면 전체 키우기 : `F11`

- ### 새 터미널 열기 : `Ctrl + Alt + T`

- ### 새 탭 열기 : `Ctrl + Shift + T`

- ### 탭 닫기 : `Ctrl + Shift + W`

## vi 사용법

``` Bash
$ sudo apt install vim
$ sudo vi /[경로]/[파일명]
```

### 명령어 창 열기

`:` 콜론 (shift + ;) 입력

### 저장

`:wq!`

w : 저장  
q : 나가기  
! : 강제

## ubuntu update 서버 변경

`sudo vi /etc/apt/sources.list`

`%s/kr.archive.ubuntu.com/mirror.kakao.com/g`

## 패키지 업데이트

`sudo apt update`

`sudo apt upgrade`

`sudo autoremove`


## 언어 설정


# 리눅스 터미널 명령어

## 재부팅

``` Bash
$ sudo reboot
$ sudo shutdown -r now
```

### 프로그램을 설치하여 재부팅이 필요한 경우 reboot 명령어를 사용해야 한다

## 종료

``` Bash
$ sudo shutdown -h now
```

### 현재 디렉토리 확인

``` Bash
$ pwd
```

> 리눅스 CLI 환경에서는 폴더가 아닌 "디렉토리"라는 명칭을 사용한다

### 화면 지우기

``` Bash
$ clear
```

## 파일 목록 보기

``` Bash
$ ls -al
```

a : 숨김 파일까지 보기
l : 상세 리스트 형태로 보기

축약
``` Bash
$ ll
```

> `ll`은 임베디드 리눅스에서 지원하지 않는 경우가 많다

## 디렉토리 이동하기

### 상위 디렉토리로 이동하기

``` Bash
$ cd ..
```

### 해당 디렉토리로 이동하기

``` Bash
$ cd [디렉토리 이름]
```

### 홈 디렉토리로 이동하기

``` Bash
$ cd ~
```

### 루트 디렉토리로 이동하기

``` Bash
$ cd /
```

### 이전 디렉토리로 되돌아가기

``` Bash
$ cd -
```

### 복사 & 붙여넣기

- 복사 : `Ctrl + Insert`
- 붙여넣기 : `Shift + Insert`

### 화면 출력 정지 & 시작

- 정지 : `Ctrl + S`
- 시작 : `Ctrl + Q`


## 파일 위치 찾기

``` Bash
$ which [파일 명]
```

## 파일 정보 조회

``` Bash
$ file /[경로]/[파일명]
```

정확하게 어떤 파일인지 알고 싶을 때 사용한다

> 리눅스 시스템에서는 파일 확장자로 파일을 구분짓지 않는다

## 파일 관리 명령어

### 파일 생성

``` Bash
$ touch [파일명]
```
- 새로운 빈 파일을 생성한다
- 이미 있는 파일이라면, 변경된 시간을 현재 시간으로 업데이트 한다.

### 파일 삭제

``` Bash
$ rm [파일명]
```

### 디렉토리 생성

``` Bash
$ mkdir [디렉토리명]
```

p : 디렉토리 하위 메뉴까지 모두 한꺼번에 생성

``` Bash
$ mkdir -p ./[디렉토리명]/[하위 디렉토리명]
```

### 디렉토리 삭제

``` Bash
$ rmdir ./[디렉토리명]
```

> 디렉토리 안에 파일이 있으면 삭제가 되지 않는다

``` Bash
$ rm -r ./[경로]
```

\* : 현재 디렉토리에서 전체 삭제

### 파일 이동

``` Bash
$ mv [파일] [옮길 곳]
```

### 파일 이름변경

``` Bash
$ mv [파일] [파일이름]
```

---

# 리눅스 파일 시스템

## 파일 시스템

### 파일을 관리하는 방법


## 윈도우와 리눅스의 디렉토리 차이

### 윈도우 파일시스템은 `C:\`와 같은 드라이브에서 파일 관리가 시작된다.  
### 리눅스 파일 시스템은 `/`에서 파일 관리가 시작된다. 이를 `Root` 라고 한다.

1. 루트 디렉토리
   - 리눅스
     - `/`
   - 윈도우
     - `C:\`
2. 프로그램 디렉토리
   - 리눅스
     - `/bin`
   - 윈도우
     - `C:\Program Files`
3. 시스템 디렉토리
   - 리눅스
     - `/sbin`
   - 윈도우
     - `C:\Windows\System`
4. 사용자 디렉토리
    - 리눅스
      - `/home`
    - 윈도우
      - `C:\Users`

# GNOME 꾸미기

### Tweak 설치

``` bash
sudo apt install gnome-tweak-tool
```

### 확장도구 설치

[파이어 폭스 확장](https:// addons.mozilla.org / firefox /addon/gnome shell integration/)


...


