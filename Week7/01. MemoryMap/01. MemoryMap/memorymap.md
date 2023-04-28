# MemoryMap

## Raspberry PI의 메모리 맵 종류

1. Legacy Master view of Address Map
   - 공식 Document의 기준 주소
2. Full 35bit Address Map
   - Rpi LPAE 기능으로 사용하는 주소체계
3. ARM view of the Address Map
   - 가상 메모리 주소

## LPAE (Large Physical Address Extention)

- 32bit system 에서는 4GB 까지의 메모리 사용가능하다
  - 1Byte × 0xFFFF_FFFF = 4GB
  - 4GB 이상을 사용하려면 64bit system을 사용해야 한다
- 32bit 가상 메모리 주소를 40bit 물리적 메모리 주소로 변환
  - swap 메모리 영역을 활용한다
  - 1Btye × 0xFF_FFFF_FFFF = 1TB
  - 최대 1TB의 주소공간에 엑세스 가능하다
- Cortex-A7, Cortex-A12, Cortex-A15 프로세서에서 지원

- 라즈베리파이에서는 35bit의 물리적 메모리 주소로 변환한다

> 라즈베리파이에서 LPAE 지원 확인
> ``` shell
> $ cat /proc/cpuinfo
> ```

## GPIO 핀에 연결된 H/W 제어

- Main Peripherals의 주소에 코드를 작성해야 한다
  - 프로세서는 32bit인 반면 Main Peripherals의 주소에는 16진수 한자리가 더있다

### GPIO base address

- Legacy Masterview of Address Map
  - 공식 Document의 기준주소
  - 공식 Document에서 Legacy Masterview of Address Map 상의 주소를 알 수 있다
  - Main Peripheral 의 주소
    - `0x7C00_0000`
  - GPIO base address 의 주소
    - `0x7E20_0000`

> Legacy 메모리 맵에서 Main Peripheral 으로부터 GPIO base address 까지의 offset이 `0x0220_0000`임을 알 수 있다

- ARM view of the Address Map
  - 공식 Document에서 ARM view of the Address Map 상의 주소를 알 수 있다
  - Main Peripheral
    - `0xFC00_0000`

> 공식 Document에서 Arm 메모리 맵에서 GPIO base address는 기술되어 있지 않다
> 하지만 **Main Peripheral과의 Offset이 `0x0220_0000`이므로 GPIO base address를 계산할 수 있다**
> - GPIO base address
>   - `0xFE20_0000`




# 18번 핀 LED코드

## 핀 출력 설정

- GPFSEL1 레지스터 (offset 0x04)
- 18번 핀 (26:24번 비트)를 001로 설정

## SET (HIGH / 3.3V) 할 경우

- GPSET0 레지스터 (offset 0x1C)
- 18번 핀 (18번 비트)를 1로 설정

## CLEAR (LOW / 0V) 할 경우

- GPCLR0 레지스터 (offset 0x28)
- 18번 핀 (18번 비트)

# 2번 핀 Switch코드

## 핀 입력 설정

- GPFSEL0 레지스터 (offset 0x00)
- 2번 핀 (8:6번 비트)를 000로 설정

## 핀 상태 확인

- GPLEV0 레지스터 (offset 0x34)
- 2번 핀 (2번 비트)

## 풀업 설정

- GPIO_PUP_PDN_CNTRL_REG0 레지스터 (offset 0xe4)
- 2번 핀 (05:04번 비트)
  - 00
    - 풀업 / 풀다운 저항 x
  - 01
    - 풀업 저항
  - 02
    - 풀다운 저항