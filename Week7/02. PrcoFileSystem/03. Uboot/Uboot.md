# 임베디드의 부팅

## PC계열과 ARM 부트로더의 차이

- x64_86
  - 0단계 : ROM 코드
  - 1단계 : BIOS or UEFI
  - 2단계 : Bootloader (GRUB)
  - Linux Kernel 실행
- ARM
  - 0, 1단계 : 칩셋 사 제공
  - 2 단계 : Bootloader (U-boot)
  - Linux Kernel 실행

## U-boot 동작 전까지

- BL0와 BL1은 칩셋사에서 Code Release한다

### BL0

- CPU 내부에 iROM과 iRAM 존재
- iROM에 있는 BL0 코드를 iRAM에 복사 후 코드를 수행
- SDRAM 설정, PMIC, UART Init, NAND 초기화
- OM (Operating Mode, DIP Switch) 확인
- NAND에 있는 BL1을 DRAM에 올리고 제어권을 넘긴다

### BL1

- NAND 앞 부분에 저장되어 있다
- BL0는 iROM에서 읽어 iRAM에서 동작했지만, BL1은 NAND에서 읽어 iRAM에서 동작시킨다
- Clock, MMU 등 초기화
- U-boot 코드를 SDRAM에 복사 후 제어권을 넘긴다

## 라즈베리파이의 부팅

- ROM의 부트로더
  - Recovery.bin이 있는지 확인 후 복구 진행
  - bootcode.bin 호출
- bootcode.bin
  - config.txt를 읽음
  - start.elf를 호출 (GPU 활성화)
- start.elf
  - ARM Core 활성화
  - kernel.img 호출


...


# U-Boot 설치하기

## U-Boot (Universal Boot Loader)

- 임베디드 리눅스 개발에 가장 많이 쓰이는 Open Bootloader
- USB, TCP/IP, Flash 제어가 가능하다

## 라즈베리파이의 부트로더

- U-Boot 이 아닌 전용 부트로더가 존재한다
- 부트로더가 변경이 불가능하도록 설계되었다

# 라즈베리파이로 U-Boot 동작시켜보기

## 