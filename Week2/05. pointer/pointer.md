# 임베디드 C언어

## App (Application)

### 운영체제 안에서 동작하는 프로그램

## 임베디드에서 사용되는 운영체제

1. 리눅스
2. RTOS
3. 자체적으로 작은 운영체제 개발 (Firmware 라고 부름)

# Application Level 개발

1. 리눅스
   - 리눅스 App
2. RTOS
   - RTOS 운영체제 App

## GUI 개발

- 윈도우에서 GUI App
  - C#
  - C++
- 리눅스에서 GUI App
  - C++ (Qt, GTK 라이브러리 사용)

## Test Scenario 개발

- 검증 S/W 개발
  - C 언어로 주로 개발

# Middleware Level 개발

## Middleware 개발

- 운영체제의 신호를 App이 가져갈 수 있는 API
- App Level에서 운영체제에게 신호를 전달하는 API

- Android 개발
  - Java
  - C
  - C++
- RTOS 개발
  - C

# Low Level 개발

## Firmware 개발

- H/W를 제어하는, 작은 운영체제를 직접 개발
- 주언어
  - C
  - Assembly

## Device Driver 개발

- 커널 내부에서 동작되는 프로그램
- H/W를 제어
- 주언어
  - C