# Interrupt

## Interrupt (인터럽트)

- 동작 중이던 프로세서가 수행 중인 작업을 멈추고 다른 장치 또는 소프트웨어의 요청에 응답하는 메커니즘
- 인터럽트 발생 시 함수가 호출되며, 함수의 작업을 마무리 하면 다시 돌아와서 작업을 시작한다

## 커널 인터럽트

- `<linux/interrupt.h>` 헤더 필요
- `request_irq([num], [handler], [flag], [name], [dev_id])`
  - num
    - 인터럽트 번호
  - handler
    - ISR (인터럽트 콜백 함수)
    - irqreturn_t 타입으로 선언
  - flag
    - 인터럽트 발생 시점
    - IRQF_TRIGGER_RISING
    - IRQF_TRIGGER_FALLING
    - IRQF_TRIGGER_HIGH
    - IRQF_TRIGGER_LOW
  - name
    - Interrupt 처리를 담당하는 장치 이름
    - debugging시 사용
  - dev_id
    - ISR 로 넘길 수 있는 인자 값
    - ISR이 접근해야 하는 데이터나 자료구조의 포인터
    - 여러 개의 디바이스 드라이버가 같은 인터럽트 라인을 공유할 경우, 구분하는 용도