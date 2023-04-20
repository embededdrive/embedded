# 임베디드 업체

## AP (Application Processor)

- 앱이 동작하는 고성능 CPU

## SoC (System On Chip)

- 내부에 다양한 기능이 있는 칩
- 임베디드 리눅스 개발
- 부품들이 원할하게 동작할 수 있도록 디바이스 드라이버를 개발
- 자체적으로 하드웨어 제작
- 하드웨어가 동작하는 소프트웨어 개발

> 리눅스 소스코드, 드라이버 코드, 샘플코드를 제작
> ex) 라즈베리파이의 칩

### SoC 업체

- 삼성 S Lsi
- 브로드컴

## BSP (Board Support Package)

- 임베디드계의 SI 업체
- SoC 부품회사들의 부품을 가져와 보드에 장착해서 제대로 동작할 수 있는 시스템을 구축하는 업무


1. 보드 회로도 제작
2. SoC 부착
3. 중국에 회로도 보냄
4. 테스트 샘플보드 수령
5. 테스트
6. 주문

> SI업체 : 시스템 통합업무를 담당하는 업체
> SoC 업체에서 제작한 리눅스 소스코드, 드라이버 코드, 샘플코드를 통해 H/W, S/W 샘플을 제작한다
> ex) 라즈베리파이 보드, 최종 커널 코드

### BSP 업체

- 삼성 SDS
- 현대 오토에버
- LG CNS
- 한화시스템 ICT

# Device Driver

## Device Driver (디바이스 드라이버)

- 프로그램이 H/W를 제어하기 위한 S/W
- H/W 개발 업체들이 장치 개발 후 장치가 보내는 신호를 PC가 받아서 처리할 수 있게 해주는 App과 app으로 전달해주는 디바이스 드라이버를 개발
- S/W 인터페이스를 통해 Application 이 H/W Spec을 이해하지 않아도 된다

## Firmware에서 임베디드 개발

- HW 메모리 맵 Address에 직접 값 Access 가능
- Application이 직접 제어한다

### Memory mapped I/O

- 메모리 맵에 GPIO 핀을 매핑하고, GPIO 핀에 H/W 장치를 연결하여 해당 메모리 주소에 신호를 줘소 동작시키는 방법

> 만약 H/W 장치를 교체해야 한다면 모든 Firmware의 H/W관련 코드를 수정하여, 모두 다시 Firmware 다운로드 후 실행해야 한다

## 중간 Layer

- Kernel은 공통적으로 쓰는 API를 제공
- Kernel 소스코드만 새로운 H/W가 동작되도록 수정하여 다시 Build하면, 다른 Firmware들은 수정할 필요가 없다
- App과 H/W 사이에 계층을 두었다
  - App은 커널의 API를 통해 H/W 접근이 가능하다
  - H/W에 대한 지식이 없어도, 커널 API를 통해 H/W를 제어하는 Application 제작가능

> 새로운 H/W 추가를 위해 소스코드 수정시 커널만 재 빌드하면 된다

### Device Driver Module (디바이스 드라이버 모듈)

- 커널에 들어가는 코드 덩어리 `*.ko`
- 디바이스 드라이버를 커널 모듈 형식으로 제작한다
- 커널 모듈만 동작 중인 커널에 적재 / 해제 하는 방식으로 테스트 할 수 있다

1. Device Files에게 API를 던진다
2. Device Driver만 재 Build하여 커널에 넣고 뺀다

- `insmod` 명령어
  - Kernel에 Device Driver Module을 넣는다
  - Kernel이 해당 모듈을 관리하기 시작한다
- `rmmod` 명령어
  - 필요없는 모듈을 제거한다
  - 메모리상 모두 Remove 한다