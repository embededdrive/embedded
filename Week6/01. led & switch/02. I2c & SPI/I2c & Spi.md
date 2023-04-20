# I2C

## 핀

- SDA (Serial Data)
- SCL (Serial clock)

> SDA / SCL 핀이 존재하면 I2C 통신을 하는 센서이다

## 장점

- 핀 2개로 다량의 장치를 연결하여 각각 제어할 수 있다
- Master(Main)
- Slave(Sub)

## BMP280

- 정밀한 대기압센서
- 온도 측정 가능

## Slave 주소

- Slave 들은 자기만의 주소 값을 가진다

# SPI

## 특징

- I2C와 같이 Master / Slave 통신을 한다
- 주로 고속이 필요한 장치에서 사용
- ex) SD카드 어댑터 모듈, LCD 디스플레이

## 장점

- Master가 Slave에게 데이터를 전송하면서 동시에 데이터를 받을 수 있다
- 속도가 빠르다

## 단점

- 핀이 많이 필요하다

|I2C|SPI|
|:---:|:---:|
|2개 (SCL, SDA)|4개 (CS, SCK, MOSI, MISO)|

## 핀

- CS
  - slave 선택
- SCK
  - 클럭
- MOSI (Master Out Slave In)
- MISO (Master In Slave Out)