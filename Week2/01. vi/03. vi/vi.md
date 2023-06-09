# vi 에디터

40년전 만들어진 editor

- 40년 전 당시, 키보드에 방항키가 없어 H, J, K, L를 방향키 대용으로 사용함

## vi의 종류

### vi

- 리눅스 에디터의 전통
- 임베디드 리눅스에서 주로 사용

### vim

- VI iMpromve
- VScode의 원조
- 플러그인 설치 가능하도록한 vi의 업그레이드 판

### neovim

- 소스코드를 처음부터 재 작성한 vi
- CLI 기반 새로운 에디터
- vim과 기능이 거의 같음

---

## 우부투 설치시 초기 상태

- vim이 설치되어 있음
- Small ver. 으로 설치되어 `방향키` 기능이 빠져있음

---

## vim 설치

``` Bash

$ sudo apt install vim -y

```

## vim 모드

## Command 모드

- vi를 처음 시작 할 때 모드
- 다른 모드에서 `ESC`키를 누르면 Command 모드로 돌아온다

### 명령어

`:` : Command Line 활성화

- 저장
`:wq!`

w : 저장  
q : 종료  
! : 강제

- 찾기
`:/[찾을단어]`  
`n` : 다음 검색  
`N` : 이전 검색

- 찾아 바꾸기
`:%s/[찾을단어]/[바꿀단어]/g`
`g`
- global
- 파일 전체의 단어를 바꾸는 옵션

- 번호 붙이기  
`:set nu`

- 번호 삭제  
`:set nonu`


### 단축키

`gg` : 맨 윗줄로 이동  
`G` : 맨 아랫줄로 이동  
`dd` : 한 줄 잘라내기  
`[줄 개수]dd` : 여러 줄 잘라내기
`yy` : 한 줄 복사  
`p` : 커서 뒤쪽에 붙여넣기  
`P` : 커서 앞쪽에 붙여넣기  
`u` : 실행 취소  
`Ctrl + r` : 다시 실행  

## Edit 모드

Command 모드에서 `i` 또는 `a` 키를 누른다

`a` : 커서 뒤쪽에 입력
`i` : 커서 앞쪽에 입력

## Visual 모드

1. Command 모드에서 커서를 복사할 영역의 처음 위치로 이동시킨다
2. `v`키를 누른다
3. 방향키를 통해서 영역을 지정한다
  - `y`키를 누르면 복사한다
  - `d`키를 누르면 잘라낸다
4. 자동으로 Command 모드로 돌아간다

> Shift + v 키를 사용하면 줄 단위로 영역이 지정된다


## 환경설정

`:set ts=4` : 탭 사이즈를 4칸으로 설정  
`:set sw=4` : 괄호를 열고 엔터를 쳤을시 기본 탭 사이즈를 4칸으로 설정  
`:set ls=2` : status bar를 2번 타입으로 설정한다, 파일 이름이 하단에 표시된다
`:set nu` : 번호 붙이기
`:set nonu` : 번호 붙이기 삭제

> vi를 껏다 켜면 setting 한 값이 모두 삭제된다
> home 디렉토리에 `.vimrc` 파일을 하나 만들면 디폴트로 설정이 된다