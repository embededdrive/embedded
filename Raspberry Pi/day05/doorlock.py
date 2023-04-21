from gpiozero import AngularServo, Button, LED
from time import sleep

gled = LED(23)
yled = LED(24)
rled = LED(25)

btn1 = Button(19)
btn2 = Button(20)

servo = AngularServo(21, min_angle=0, max_angle=90)

pwd = [0, 1, 0, 1]
btnin = [0, 0, 0, 0]

servo.angle = 0

idx = -1

def btn1pressed():
    global idx
    if idx != -1:
        btnin[idx] = 0
        idx += 1
        yled.on()
        sleep(0.5)
        yled.off()

def btn2pressed():
    global idx
    if idx != -1:
        btnin[idx] = 1
        idx += 1
        yled.on()
        sleep(0.5)
        yled.off()

btn1.when_pressed = btn1pressed
btn2.when_pressed = btn2pressed

while True:
    idx = 0
    while idx < 4:
        pass
    idx = -1

    issame = True

    for i in range(4):
        if pwd[i] != btnin[i]:
            issame = False

    if issame:
        gled.on()
        servo.angle = 90
        sleep(1)
        gled.off()
        servo.angle = 0
    else:
        rled.on()
        sleep(1)
        rled.off()