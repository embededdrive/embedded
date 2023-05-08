# 인터럽트

## 인터럽트 (Interrupt)

- 프로그램 실행 중 CPU의 현재 처리 순서를 중단하고, 정해진 일련의 동작을 수행하도록 하는 것

## 아키텍쳐

- ARM 아키텍쳐에 인터럽트가 포함되어 있다
- ARM 아키텍쳐를 쓰는 경우 인터럽트 구성은 동일하다

## IRQ (Interrupt ReQuest)

- 어느 한 순간에 한 개의 활성화된 장치에 대해서만 할당된다

## ISR (Interrupt Service Routine)

- 실질적인 인터럽트 처리 작업 수행
- 우선순위가 더 높은 인터럽트 발생시 재귀적으로 인터럽트를 처리한다

## Event Table

- 등록된 이벤트 목록을 바로 호출

## 벡터 테이블

- 인터럽트 실행 함수가 배열 형태로 존재한다

## 인터럽트 처리 과정

1. 인터럽트 요청
   - 특정 이벤트가 발생
   - Periperal 에서 들어오는 전기적인 신호
2. 프로그램 실행 중단
   - 현재 실행 중인 루틴을 잠시 멈춘다
3. 상태 보관
   - 현재 프로그램의 상태를 레지스터에 저장한다
4. 인터럽트 판별
   - 벡터 테이블에서 참조 실행할 ISR 주소값을 얻는다
5. ISR 실행
   - 인터럽트 요청에 맞는 실질적인 인터럽트 처리
6. 상태 복구
   - 저장해둔 복귀주소 로드
   - 이전에 실행 된 루틴으로 복원

## Interrupt 구분

### Nested Interrupt

- 현재 실행중인 인터럽트 보다 우선수누이가 높은 인터럽트가 발생하면, 현재 실행중인 인터럽트를 멈추고, 우선순위가 높은 인터럽트를 먼저 처리하는 것
- 우선순위에 따라서 인터럽트를 처리하는 것

### Vectored Interrupt

- interrupt가 호출되었을 때 Vector Table에 있는 인터럽트에 대응되는 ISR 주소를 바로 호출한다
- 인터럽트 처리 속도가 빠르다

### NVIC (Nested Vectored Interrupt Controller)

- Nested Interrupt + Vectored Interrupt
- 우선순위에 따라서 여러개의 인터럽트를 처리한다
- 주소를 바로 호출한다
- 속도가 빠르다
- ARM 아키텍쳐에 적용된 Interrupt

# NVIC

## ARM (Advanced RISC Machine)

> RISC (Reduced Instruction Set Computer)

- RISC 기반의 CPU 아키텍쳐 판매
- 아키텍쳐만 판매하고 하드웨어는 칩 제조사들이 제작한다
  - 특정 요구사항에 맞춰 제작 (임베디드)
  - 소형, 고성능, 저전력, 저발열, 에너지 효율성
  - Vendor들은 특정 목적에 맞춰 아키텍쳐만 가져다 쓴다

## ARM - NVIC

- ARM은 CPU 로직만 라이센싱해서 판매
- 이 로직안에 NVIC라는 인터럽트 컨트롤러 존재
- ARM Cortex-M을 사용하는 벤더들은 NVIC를 사용한다

> STM32-F103RB도 ARM 아키텍쳐의 NVIC를 사용하게 된다

## ARM - NVIC의 실행흐름

1. 외부 신호를 받아 인터럽트 발생시키는 장치로 입력
2. 신호 요청을 NVIC로 전달
3. NVIC에서는 CPU에 IRQs로 부터 받은 요청에 맞는 코드 실행을 요청
4. CPU 실행 요청에 맞는 코드 ISR 실행

# Button Interrupt


# 개발

## 펌웨어 vs OS

- 앱 설치
- 보안
- 멀티 프로세싱

### 펌웨어

- 장치 제어시 메모리 접근

### OS

- App --시스템콜--> DeviceDriver ----> 장치제어
- App --[HAL]--> DeviceDriver ----> 장치제어
- App 개발자 입장에서 메모리 맵을 몰라도 개발이 가능해진다

## HAL (Hardware Abstraction Layer)

- 메모리 맵을 보지 않고 개발 가능
- 다양한 MCU를 통합하여 개발 가능
- 각 회사마다 개발한다

## CMSIS

- ARM사의 HAL을 통합시키려는 시도

## IDE

- IAR
- ARM DS-5

