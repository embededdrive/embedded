# 환경변수

- 쉘에 저장되는 변수
- 사용자, Process, 리눅스 자체 등 다 같이 사용하는 변수

## 환경변수 전체 읽기

``` Bash
$ printenv
```

## 환경변수 임시 추가

``` Bash
$ export [변수명]=[값]
```

## `.bashrc`파일

- bash 쉘이 시작되자마자 자동으로 시작되는 bash 스크립트 파일
- ~/.bashrc 파일에 환경변수를 추가하는 코드를 추가하면 새로운 터미널에 환경변수가 적용된다
