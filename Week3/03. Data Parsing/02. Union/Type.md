# union

## union

- struct와 문법이 비슷하다
- union은 멤버끼리 값을 공유한다

``` C
typedef union _Book_ {
    int author;
    int writer;
} Book;

Book newBook = {0};

newBook.author = 1;

printf("%d", newBook.writer);
```

## union을 쓰는 이유

- 같은 메모리 주소를 사용한다
- 다른 데이터 타입을 사용하면 해당 타입에 맞게 들어간다
- 바이트 단위의 파싱을 편리하게 할 수 있다

``` C
#include <stdio.h>
#include <stdint.h>

typedef union _Memory_ {
	uint32_t _4byte;
	uint8_t _1byte[4];
} Memory;

int main() {

	Memory data;

	data._4byte = 0x1234ABCD;

	return 0;
}
```

![바이트 단위 파싱](바이트%20단위%20파싱.png)