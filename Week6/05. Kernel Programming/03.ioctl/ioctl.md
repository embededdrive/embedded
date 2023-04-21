# ioctl

## ioctl (Input Output ConTroL)

- `<sys/ioctl.h>` 필요
- 하드웨어를 제어하기 위한 함수
- 예약된 동작 번호 지정

``` c
ioctl([파일디스크립터], cmd, arg)
```

- _IO([type], [num]) 명령 코드 중 하나
- type
  - 매직번호
  - 다른 디바이스 드라이버와 구별
- num
  - 명령번호

## ioctl의 역할

- H/W에 여러 옵션을 줘서 명령을 할 수 있다
  - app에서 cmd에 정수 값을 보낼 수 있다
  - driver에서 cmd 값에 따라 select 문 사용가능
  - cmd 값에 따른 코드 추가 가능
  - args에 포인터를 전달하여 app의 다량의 데이터를 driver로 전달 가능


## return값 활용

### `-EINVAL` (Invalid argument)

- switch 문에 `default:` 추가
- 범위를 벗어난 값을 인자로 받을 경우 `-EINVAL` 에러를 일으킨다
- 커널에 로그가 남지 않고 App에서 확인 가능하다

# ioctl argument

## Ioctl Argument 사용하기

- arg에 값을 담아 보낸다
  - User Space ➡ Kernel Space

### app 코드

``` C
ioctl(fd, _IO(0,3), 1234);
ioctl(fd, _IO(0,4), 9012);
ioctl(fd, _IO(0,5), 5678);
```

### Kernel 코드

``` C

```

> `%lu` (Unsigned Long)
> `%ul`이 아님에 주의한다

# Kernel Log

## 커널 로그 레벨

- printk()에 메시지의 중요도를 나타낼 수 있다
- 디버깅에 도움이 된다

|로그 레벨|DEFINE|의미|
|:---:|:---:|:---:|
|0|KERN_EMERG|시스템이 동작하지 않음|
|1|KERN_ALERT|즉시 출력 메시지|
|2|KERN_CRIT|치명적 에러 메시지|
|3|KERN_ERR|에러 메시지|
|4|KERN_WARNING|경고 메시지|
|5|KERN_NOTICE|정상 메시지|
|6|KERN_INFO|시스템 정보 메시지|
|7|KERN_DEBUG|디버깅 정보|

## 커널 디버깅

- 커널 코드의 실행을 분석, 버그를 찾는 과정
  - printk 디버깅
    - printk 함수를 이용해 커널 코드의 실행 중에 로그 출력
  - kgdb 디버깅
    - 원격 PC에서 gdb 클라이언트를 실행
    - 리모트 gdb 서버로 커널 디버깅
  - QEMU 디버깅
    - 가상 머신에서 QEMU를 사용
    - 커널 이미지르 ㄹ실행하여 디버깅

# copy_from / to_user

## Linux Layer

- User Space
  - 사용자 영역
  - 응용 프로그램이 실행되는 공간
  - 사용자와 상호작용
  - 시스템 콜로 Kernel Space 진업
- Kernel Space
  - 커널 영역
  - 시스템 콜 인터페이스를 통해 호출된 함수가 실행되는 공간
  - 운영체제의 핵심 기능 수행
  - User Space에서 요청한 동작 수행
  - device drive와 같은 하드웨어 관련 모듈도 동작
  - Subsystems
    - 커널의 모듈들
      - 메모리 관리
      - 프로세스 관리
      - 파일시스템
- Hardware



> 커널 코드에서는 string.h를 사용하지 못함
> linux/string.h 방식으로 사용가능