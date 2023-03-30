# typedef

## typedef

- 기존 타입을, 원하는 이름으로 정의하는 방법
- 타입명이 마음에 들지 않을 때 사용된다

``` C
#include <stdio.h>

typedef long long ll;

int main() {
	ll a = 1234567898765432123;

	printf("%lld", a);

	return 0;
}
```

# 구조체

- 기본 타입들을 모아 새로운 타입을 만드는 문법

> C 에서는 구조체 내부에 함수를 생성할 수 없다

``` C
struct Day {
    int year;
    int month;
    int date;
};
```

## 구조체 변수 생성

- 구조체 타입을 만들자마자 구조체 변수를 만들 수 있다

``` C
struct Day {
    int year;
    int month;
    int date;
} yesterday, today, tomorrow;
```

- `struct [구조체 이름] [구조체 변수]`으로 구조체 변수를 생성할 수 있다

``` C
struct Day {
    int year;
    int month;
    int date;
};

struct Day yesterday, today, tomorrow;
```

> C 에서는 `[구조체 이름]`으로 새 구조체 변수를 생성할 수 없다  
> C++ 에서는 `struct`를 안붙여도 가능하다

## typedef

- `typedef`을 사용하면 구조체 이름으로 새 구조체 변수를 생성할 수 있다

``` C
typedef struct _Day_ {
    int year;
    int month;
    int date;
} Day;

Day yesterday, today, tomorrow;
```

## 구조체 변수 초기화

- 구조체 변수를 생성할 때는 초기화가 가능하다
- 구조체 변수를 생성한 이후 초기화는 불가능하다

![구조체 변수 초기화](구조체%20변수%20초기화.png)

> C++ 에서는 구조체 변수를 생성한 이후 초기화가 가능하다

## 구조체 안에 있는 구조체

- 구조체 내부에 구조체를 만들 수 있다

``` C
typedef struct _Node_ {
    int a;

    struct {
        int y;
        int x;
    }b;

    int c;
} Node;
```

## 구조체 변수 선택적 초기화

- 리눅스 Device Driver 개발시 자주 사용된다

``` C
Node v = {
        .a = 10,
        .b = {
            .y = -1,
        },
};
```

> C++ 에서는 사용할 수 없다
> 끝에 세미콜론 `;` 이 아닌 콤마 `,` 를 써야함에 유의한다