# 포인터 (Pointer)

## 포인터 기본

``` C
int x = 10;
int* p = &x;
```

- 포인터 p는 타입에 맞는 주소(&x)를 저장할 수 있다
- 이를 가리킨다라고 표현한다
- 이후로 `*p`는 x로 취급된다

## 포인터 배열

- 포인터를 담은 배열

``` C
int* p[3] = {NULL, NULL, NULL};
```

## 배열 포인터

- 배열을 가리키는 포인터

### \[타입\]* p

- 단위크기가 int의 크기(4Byte)와 같은 포인터
- `+=1` 연산을 하면 주소값이 int 의 크기 만큼 바뀐다

``` C
int vect[5] = { 1, 2, 3, 4, 5 };
int* p = vect;

printf("%p\n", p);
p += 1;
printf("%p\n", p);
```

![단위크기가 int의 크기와 같은 포인터](단위크기가%20int의%20크기(4Byte)와%20같은%20포인터.png)

> 배열의 경우 이름 자체가 주소값이다  
> `p = [배열명]` 라고해도 되고  
> `p = &[배열명]` 라고해도 상관없다
> ``` C
> int* p = vect;
> int* p = &vect;
> ```

### \[타입\](*p)\[\[배열크기\]\]

- 단위크기가 배열의 크기와 같은 포인터
- `+= 1` 연산을 하면 주소값이 배열의 크기 만큼 바뀐다

``` C
int vect[5] = { 1, 2, 3, 4, 5 };
int(*p)[5];
p = &vect;

printf("%p\n", p);
p += 1;
printf("%p\n", p);
```

![단위크기가 배열의 크기와 같은 포인터](단위크기가%20배열의%20크기와%20같은%20포인터.png)

## 함수 포인터

### \[반환값 타입\](*p)([매개변수 타입]);

- 포인터 p는 함수의 주소(&run)를 저장할 수 있다
- 이를 가리킨다라고 표현한다
- 이후로 `*p`는 함수(run)로 취급된다

``` C
#include <stdio.h>

void run() {
	printf("함수실행!\n");
}

int add(int a, int b) {
	return a + b;
}

int main() {

	void(*p)();
	p = &run;

	(*p)();

	int(*q)(int, int);
	q = &add;

	int ret = (*q)(1, 2);
	printf("%d\n", ret);

	return 0;
}
```

## 함수 포인터 배열

### \[반환값 타입\](*p\[\[배열크기\]\])([매개변수 타입]);

- 배열에 각각 함수를 가리키고 호출할 수 있다

``` C
#include <stdio.h>

int sum(int a, int b) {
	return a + b;
}

int sub(int a, int b) {
	return a - b;
}

int mul(int a, int b) {
	return a * b;
}

int div(int a, int b) {
	return a / b;
}

int main() {
	
	int(*p[4])(int, int) = { &sum, &sub, &mul, &div };

	int ret;

	for (int i = 0; i < 4; i++)
	{
		ret = (*p[i])(10, 2);
		printf("%d\n", ret);
	}

	return 0;
}
```

![함수 포인터 배열](함수%20포인터%20배열.png)

# Main argument

## main()의 매개변수

### C언어의 main()는 실행 파일 옵션을 매개 변수로 받을 수 있다

- argc
  - main()에 전달되는 정보의 개수
- argv
  - main()에 전달되는 정보
  - 첫 번째 문자열은 실행 경로로 고정

``` C
#include <stdio.h>

int main(int argc, char* argv[]) {
	
	printf("argc = %d\n", argc);

	for (int i = 0; i < argc; i++)
	{
		printf("argv[%d] = %s\n", i, argv[i]);
	}
	
	return 0;
}
```