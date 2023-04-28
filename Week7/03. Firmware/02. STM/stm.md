# STM

## 실습 보드 정보

- 보드 이름
  - Nucleo
- 보드 모델명
  - Nucleo-F103RB
- ST사의 CPU칩셋 이름
  - STM32F103RB
- CPU 아키텍쳐
  - ARM Cortex-M3

## IDE (개발환경)

- STM CubeIDE
  - ARM GNU GCC를 사용하는 Eclipse기반 무료 IDE
- [개발도구 다운로드 사이트](https://st.com)

## CubeIDE

- 임베디드에서 매우 어려운 보드 초기세팅을 대신해준다
- GUI를 통해서 시작코드를 생성할 수 있다

## ST-Link 디버깅장비

- Trace를 위해 별도의 디버깅 장비가 필요하다
- ex) ST-Link/V2, J-link, Trace32

> Nucleo에는 ST-Link/V2가 포함되어있다!

# Clock 설정

## Digital 신호

- 특정 전압을 걸면 `1`로 인식 (High)
- 0V 전압을 걸면 `0`으로 인식 (Low)
- 과거에는 5V를 많이 사용했지만 현재는 3.3V가 주로 사용된다
- Rising Edge
  - 클럭 신호가 Low에서 High으로 갈 때
- Falling Edge
  - 클럭 신호가 High에서 Low로 갈 때

## 클럭

- 서로 신호를 맞추어 동작되기 위해 사용
- 박자를 맞추어, 여러 장치들이 동시에 동작되기 위한 것
- CPU도 동기 클럭 신호에 맞추어 Fetch / Decode / Excute로 동작한다

## Clock Generator (클럭 발생기)

- 주기적인 클럭 발생장치를 Oscillator (발진기)라고 한다
- MCU 내부에도 Oscillator가 있다
- 필요시 외부에 추가로 Oscillator를 달아준다

### 내장 Oscillator가 있어도 외장 Oscillator를 사용하는 이유

- 내장 Oscillator
  - 온도 등 노이즈 영향으로 클럭이 정확하지 않다
  - Timer가 정확하지 않다
- 외장 Oscillator
  - MCU 내부 Oscillator 보다 빠른 속도의 클럭을 발진할 수 있다

## 프리스케일러

- 연결된 장치에 다른 클럭을 전달해야할 경우 사용한다

# 개발 초기 설정

## PIN 설정

- 각 Pin 마다 어떤 역할을 수행할지 설정이 필요하다
- 사용할 Pin에 대해 MCU 내부 레지스터 설정
  - GPIO Input
  - GPIO Output
  - SPI / I2C 통신
  - UART 통신
- DataSheet를 참고하여 레지스터 설정을 해주어야 한다

> CubeIDE가 반자동으로 해준다

## startup.s 작성

- Assembly로 작성
- 초기 클럭 설정
- 메모리 초기화
- C언어가 구동되기 위한 구동 준비
- C언어로 작성된 Firmware의 Main 함수 호출

> CubeIDE가 반자동으로 해준다

## CubeIDE

- CubeIDE를 사용하면 손쉽게 설정이 가능하다
- 임베디드 초기 소스코드를 대신 작성해준다
- 고 수준의 HW / Firmware 지식이 없어도, GUI로 초기 세팅이 가능하다