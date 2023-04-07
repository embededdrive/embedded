# RTOS (Real Time OS)

## RTOS 개념

- 실시간 시스템에 적합한 운영체제
  - 임베디드 시스템에서 자주 사용
- 요즘은 리눅스 기반의 RTOS가 사용된다
  - IoT 기술의 발달로 장치들이 정교화 되고 스마트 해짐
  - 많은 레퍼런스로 개발 용이, 유지 보수 용이

## RTOS vs 리눅스

- 설계부터 다르다
  - RTOS는 Real Time을 위한 OS로 정해진 타임 라인을 정확히 지키기 위해 설계됨
- 모든 OS는 preemptive 한 작업 수행을 보장한다
- ***RTOS는 시스템 콜에 대한 Preemptive가 있다***

## RTOS 업계 순위

- VxWorks [Wind River]
- Window Embedded Compact (구 Windows CE) [Microsoft]
- QNX [Blackberry]
  - 전장분야에서 주로 사용
- 국산 NEOS [한컴 MDS]
  - 방산분야에서 주로 사용

# time_t 와 tm

## time() 시스템콜

- `time_t time(time_t *tloc);`
  - 1970년 1월 1일 0시 0분 0초부터 현재까지의 시간을 초 단위로 반환

``` C
#include <stdio.h>
#include <time.h>

int main() {
	time_t current_time = time(NULL);

	printf("%ld\n", current_time);

	return 0;
}
```

- `time_t type`
  - 64비트 unsigned 정수형 숫자
  - 시간 표현 data type


``` C
time_t BBQ;
time(&BBQ);  // BBQ 안에 시간이 들어간다
```

## 구조체 tm

- C 표준 라이브러리에서 제공하는 시간과 날짜를 나타내기 위한 구조체
- `localtime()`을 이용해서 구조체에 시간 정보를 담을 수 있다

|멤버|범위|
|:---:|:---:|
|tm_sec|0-61|
|tm_min|0-59|
|tm_hour|0-23|
|tm_mday|1-31|
|tm_mon|0-11|
|tm_year|1900 이후|
|tm_wday|0-6|

``` C
#include <stdio.h>
#include <time.h>

int main() {

	while(1)
	{

		time_t current_time = time(NULL);

		struct tm *tmm = localtime(&current_time);

		printf("%d/%d/%d\n", tmm->tm_year, tmm->tm_mon, tmm->tm_mday);
		
		// 2023/4/5 WED
		// 22:33:48
	}

	return 0;
}
```

# clock_t

## clock()

- 현재 프로세스가 시작되고, 얼마나 시간이 흘렀는지 CPU 클럭 수치 값
``` C
#include <stdio.h>
#include <time.h>

int main()
{
  clock_t a = clock();

	printf("%ld\n", a);

	return 0;
}
```

## clock 함수

- `CLOCKS_PER_SEC` 매크로
  - 1초당 시스템 clock이 올라가는 정도를 나타낸다

``` C
#include <stdio.h>
#include <time.h>

int main()
{
	printf("%ld\n", CLOCKS_PER_SEC);

	return 0;
}
```

# gettimeofday()

- syscall
- us 단위로 time 보다 정밀한 현재 시간을 얻을 수 있다
- `sys/time.h` 라이브러리를 통해 사용

## gettimeofday 시스템 콜

- timeval과 timezone 2개의 구조체가 존재한다

### timeval

- time_t tv_sec
  - s 단위
- suseconds_t tv_usec
  - us 단위

``` C
#include <stdio.h>
#include <sys/time.h>

int main()
{
	struct timeval time;

	gettimeofday(&time, NULL);

	printf("%ld\n", time.tv_sec);
	printf("%ld\n", time.tv_usec);

	return 0;
}
```

### timezone

- int tz_minuteswest
- int tz_dsttime
- 잘 사용하지 않는다 


# WDT (Watchdog Timer)

- 임베디드 시스템에서 오작동을 막기 위한 타이머
  - 타이머가 끝나면 시스템 리셋 or 중지 / 메모리 덤프 / 코어 덤프 동작이 이뤄진다
  - 평소에는 지속적으로 갱신이 필요하다
  - 동작 중 무한루프가 돌거나 응답이 없을 때 WDT가 Timeout이 된다
    - 임베디드의 안전장치
    - 디버깅에 좋음

## alarm API

- alarm (초)
  - 특정 시간 후 SIGALRM Signal이 발생한다
  - alarm을 다시 울리면 갱신된다