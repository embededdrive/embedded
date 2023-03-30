# Preprocessor

## Preprocessor

- 실행 파일이 나오기 까지를 컴파일 과정 이라고 한다
- 컴파일을 하기 전 전처리 과정을 거친다


|preprocessor|compiler|assembler|linker|
|:---:|:---:|:---:|:---:|
|전처리기|컴파일러|어셈블러|링커|
|*.i | *.s | *.o|*.exe|


# Preprocessor 환경구축

## Visual Studio에서 전처리기 파일 확인

- 솔루션 탐색기 > 프로젝트 > 속성 > C/C++ > 전처리기
  - 파일로 전처리 : 예
  - 전처리 줄 번호 표시 안함 : 예
- Ctrl + F7을 통해 컴파일하면 빌드 되지 않은 `*.i` 파일이 생성된 것을 프로젝트 폴더에서 확인 가능하다

# 조건부 컴파일

## 전처리기 지시문

- *.c 파일을 읽어 전처리를 한 후, i 파일로 만든다
- `전처리기 지시문`들을 처리한다

``` C
#include
#define
#ifdef
#ifndef
#undef
#if
#elif
#else
#endif
#error
#pragma
```

### include

- 파일 그대로 복사 붙여넣기
- 해당 파일 내용을 그대로 가져온다

``` C
#include <stdio.h>
```

### define

- 매크로를 정의한다

``` C
#define KOR
#define USA
```

### ifdef

- 매크로가 정의되어 있으면 전처리 과정에 포함한다

``` C
#define KOR

#ifdef KOR
안녕
#endif
```

### ifndef

- 매크로가 정의되어 있지 않으면 전처리 과정에 포함한다

``` C
#define KOR

#ifdef KOR
안녕
#endif

#ifndef USA
HI
#endif
```

### undef

- 정의된 매크로를 해제한다

``` C
#define KOR

#undef KOR

#ifdef KOR
안녕
#endif

#ifndef USA
HI
#endif
```

### if / elif / else

- 조건문에 따라 전처리 과정에 포함한다

``` C
#define age 25

#if age < 20
20세 미만
#elif age < 40
40세 미만
#else
40세 이상
#endif
```

### if defined

- ifdef과 동일하게 사용가능하다
- defined를 쓰면 &&, ||, ==, !=, >, < 등 연산기호를 사용할 수 있다

``` C
#define USED
#define STATUS 'A'

#if defined USED && STATUS == 'A'
민트급
#elif defined USED && STATUS == 'B'
중고
#else
미사용
#endif
```

### error

- stderr에 에러 메세지를 출력한다
- 전처리 중 `#error` 문을 만나면 전처리 단계가 중단된다

``` C
#define DEBUG

#ifdef DEBUG
#error 디버그 모드
#endif
```

### define 활용

HW 초기화 코드
- 특정 장치의 초기화 코드를 작성
- make에 따라 define이 달라짐
- HW 초기화 코드를 Define에 따라 넣고 안 넣을 수 있다
  - error로 컴파일을 중단시킬 수 있다

``` C
#define x86

#ifndef x64
#error 64비트 장치에서만 실행할 수 있습니다.
#endif

int main() {

	return 0;
}
```

# 컴파일러 Header Guard

- 전처리기에서 같은 함수를 가져오면 컴파일시 에러가 발생한다
- 이를 방지하기 위해 Header Guard를 사용한다
- 중복 include와 상호 include로 인한 컴파일 에러를 방지할 수 있다

## pragma once

- 임베디드에서 컴파일러가 지원은 하지만 회사에서 잘 안쓴다

``` C
#pragma once
```

## 수동 Header Guard

- gcc 표준
- define / ifndef를 사용
- pragma once와 동일한 기능

``` C
#ifndef __KFC__
#define __KFC__

void abc() {
  int a = 10;
}

#endif
```

# C 파일과 Header 차이

- 전처리기
  - `*.c` 파일과 `*.h` 파일을 똑같이 처리한다
  - `*.c` 파일과 `*.h` 파일은 모두 include 가능하다
- 컴파일러
  - `*.h` 파일은 컴파일하지 않는다
