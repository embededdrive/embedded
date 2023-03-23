# 리눅스에서 사용되는 압축 방법

## tar (Tape ARchiver)

- 여러 개의 파일을 하나의 파일로 묶거나 풀 때 사용하는 명령어  

J : 
z : gzip 압축 알고리즘  
c : 압축  
x : 압축풀기  
v : 진행상황 표시  
f : 파일명 지정  

## 한 파일로 모으고, `*.tar.xz`로 압축하기

``` Bash
$ tar -Jcvf ab_xz.tar a.txt b.txt
```

## ./test에 압축해제

``` Bash
$ tar -Jxvf ab_xz.tar -C ./test
```