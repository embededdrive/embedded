


``` C
#include <linux/module.h>

MODULE_LICENSE("GPL");

static int hi_init(void){
	printk(KERN_INFO "OK HIFAKER!!!\n");
	return 0;
}

static void hi_exit(void)
{
	printk(KERN_INFO "BYEBYE\n\n");
}

module_init(hi_init);
module_exit(hi_exit);
```

``` Makefile
KERNEL_HEADERS=/lib/modules/$(shell uname -r)/build

obj-m := hi.o

go :
    make -C $(KERNEL_HEADERS) M=$(PWD) modules

clean:
    make -C $(KERNEL_HEADERS) M=$(PWD) clean
```

## 디바이스 드라이버의 필요성

- Application 개발 시 Device File에다가 System Call API만 쓰면, 장치 제어가 된다
- 만약 H/W 가 바뀌면, Kernel을 다시 Build 할 필요가 없다

## 디바이스 드라이버의 장접

- App / Driver 역할 분담
- Application 개발자
  - H/W를 제어할 수 있는 API 사용 방법 익히기
  - API가 건내 준 Data 처리
  - API를 이용하여 H/W 제어
  - Log 남기기
  - Network / UI 작업

- Device Driver 개발자
  - H/W 제어 API 제작
  - H/W 불량 분석
  - Latency 측정


## 커널 헤더 위치

- `/usr/src/`

## 작동중인 커널 확인

- `uname -r`

## 장치 파일 생성

``` shell
$ sudo mknod /dev/nobrand c 100 0
```

- 컴퓨터 재부팅시 사라진다


## 읽기 쓰기 권한 부여

``` shell
$ sudo chmod 666 /dev/nobrand
$ ls -al /dev/nobrand
```

## 커널로그

``` shell
$ dmesg -w
```

# code.zip

## build

``` shell
$ make
```

- Makefile을 확인하면 driver와 app 명령을 실행
- driver 명령
  - /lib/moudles/$(shell uname -r)/build 디렉토리에서 빌드
  - 커널을 통해서 드라이버 파일을 빌드
  - gcc를 사용하지 않는다
- app 명령
  - gcc를 통해 app을 빌드


## 디바이스 드라이버 장착

``` Shell
$ sudo insmod nobrand.ko
```

- `*.ko` 파일
  - 디바이스 드라이버

- insmod 시
  - `module_init(nobrand_init);`
  - `/dev/nobrand` 파일과 `nobrand.ko` 파일을 연결해준다
- rmmod 시
  - `module_exit(nobrand_exit);`
  - `/dev/nobrand` 파일과 `nobrand.ko` 파일의 연결을 다시 해제한다

## 앱 실행

``` shell
$ ./app
```

- open() 시
  - `nobrand_open()`
- close() 시
  - `nobrand_release()`

## 디바이스 드라이버 제거

``` shell
$ sudo rmmod nobrand
```

## build 잔여파일 삭제

``` shell
$ make clean
```