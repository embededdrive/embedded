# Decomposition

- 하나의 큰 작업을 분해해서 수행한뒤 결과를 합치는 것
- 작업을 병렬처리하여 작업시간을 단축한다

## Data Decomposition 처리방법

- 데이터 단위로 분해하여 Thread Programming
- 각 Thread 마다 같은 작업을 수행
- Core의 최고 효율을 낼 수 있다.

# 시스템 프로그래밍

## 시간

- 시스템 시간
- 시스템 클럭

## OS / firmware

- CPU가 동작하기 위해서 클럭을 맞춰서 동작하고 있다

## 시스템 시간

- 1970년 1월 1일 0시 0분 0초 부터 경과한 시간을 초 단위로 표현
- 시스템 클럭으로 유지됨
- &date

## UTC (Coordinated Universal Time)

- 국제 표준 시간
- 1972년 부터 시행
- UTC + offset으로 시간표시
- 한국 (KST) = UTC + 9

## RTC (Real Time Clock)

- 전원이 없어도, 시간을 계산한다
- 수은 건전지 사용

## 리눅스에서 관리하는 시간

### date 명령어

- `$ date`
- 부팅시 RTC 정보를 받아 리눅스에서 시간 정보를 관리한다
- 네트워크에 연결될 때, Time 서버에서 시간을 자동 Update 한다

### 인터넷 타임서버에서 시간 값 가져와 맞추기

``` Shell
$ sudo apt install rdate
$ sudo rdate time.bora.net
$ date
```

### hwclock 명령어

- `$ sudo hwclock`
- RTC HW 장치가 가지고 있는 시간 정보 값
- 리눅스에서는 date와 RTC가 맞지 않으면 한족으로 Sync를 맞춰주는 명령어를 써야함
- `-s` 옵션
  - 시스템 시간을 기준으로 RTC 시간을 변경
- `-w` 옵션
  - RTC 시간을 기준으로 시스템 시간을 변경

``` Shell
$ sudo hwclock -s
$ sudo hwclock -w
```

## 시스템 시간 vs 시스템 클럭

- 시스템 시간
  - 컴퓨터 시스템의 현재 시간
  - 로그 파일 기록
  - 예약된 작업 수행
  - 파일 수정 시간
- 시스템 클럭
  - H/W 장치
  - 운영체제에서 관리
  - CPU가 실행하는 명령어의 실행주기를 결정
  - 타이머 구현
  - 정해진 간격으로 작업 수행
  - 실시간 처리
  - CPU 성능 향상

> 시스템 시간과 시스템 클럭은 동기화 되어있다


[광주_6반_김도훈] ㅇㄹㅋㄹ