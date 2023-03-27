# 쉘 스크립트 작성

## 변수 생성

변수 만들기

``` Bash
[변수이름]=[값]
```

- 모든 값들은 문자열로 취급한다

![변수 생성](변수%20생성.png)

> `=` 기호 주변으로 띄워쓰기시 에러가 발생한다

## Shell Script에서 Argument 변수 사용하기

``` Bash
#!/bin/bash

echo $1
echo $2
echo $3
```

![Argument 변수 사용하기](Argument%20변수%20사용.png)


