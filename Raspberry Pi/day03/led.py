from gpiozero import LED
from gpiozero import Button
from signal import pause
from time import sleep

a = LED(15)
b = LED(14)
c = LED(12)
d = LED(22)
e = LED(23)
f = LED(17)
g = LED(18)
DP = LED(13)

lst = [g, f, a, b, e, d, c, DP]
num = [[a, b, c, d, e, f], #0
       [b, c], #1
       [a, b, g, e, d], #2
       [a, b, g, c, d], #3
       [f, g, b, c], #4
       [a, f, g, c, d], #5
       [a, f, g, e, c, d], #6
       [f, a, b, c], #7 
       [a, b, c, d, e, f, g], #8
       [a, b, c, d, g, f]] #9


def segment(number):
    for i in lst:
        i.off()
    for i in lst:
        if i in num[number]:
            i.on()
        else:
            i.off()

pressed = 0
dir = 0
n = 0

def btnpressed():
    global pressed
    pressed = 1

btn = Button(2)

btn.when_pressed = btnpressed

led = LED(3)

led.off()

while(True):

    segment(n)
    if n == 0 or n == 9:
        sleep(0.4)
    sleep(0.1)

    if pressed == 1 and n == 7:
        for _ in range(3):
            led.on()
            for i in lst:
                i.on()
            sleep(0.5)
            led.off()
            for i in lst:
                i.off()
            sleep(0.5)
        
        pressed = 0

    if dir == 0:
        if n < 9:
            n += 1
        else:
            n = 8
            dir = 1
    elif dir == 1:
        if n > 0:
            n -= 1
        else:
            n = 1
            dir = 0
        
    sleep(0.1)