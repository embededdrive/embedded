from gpiozero import PWMLED
from gpiozero import LED
from gpiozero import Button
from time import sleep

led = LED(2)

R = PWMLED(14)
G = PWMLED(15)
B = PWMLED(18)

btn1 = Button(16)
btn2 = Button(20)
btn3 = Button(21)

rval = 1
gval = 1
bval = 1

def btn1pressed():
    global rval
    print("btn1")
    rval += 0.1
    if rval > 1:
        rval = 0
    sleep(0.1)

def btn2pressed():
    global gval
    print("btn2")
    gval += 0.1
    if gval > 1:
        gval = 0
    sleep(0.1)

def btn3pressed():
    global bval
    print("btn3")
    bval += 0.1
    if bval > 1:
        bval = 0
    sleep(0.1)

btn1.when_pressed = btn1pressed
btn2.when_pressed = btn2pressed
btn3.when_pressed = btn3pressed

while True:
    R.value = rval
    G.value = gval
    B.value = bval