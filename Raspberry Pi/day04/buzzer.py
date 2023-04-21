from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

c1 = 261.62
c1s = 277.18
d1 = 293.66
d1s = 311.12
e1 = 329.62
f1 = 349.22
f1s = 369.99
g1 = 391.99
g1s = 415.30
a1 = 440.00
a1s = 466.16
b1 = 493.88
c2 = 523.25
c2s = 554.36
d2 = 587.32
d2s = 622.25
e2 = 659.25
f2 = 698.45
f2s = 739.98
g2 = 783.99
g2s = 830.60
a2 = 880.00

b = TonalBuzzer(17)

def playbuzz(lev, time):
    b.play(lev)
    sleep(time * 0.5)
    b.stop()


playbuzz(c1, 1.5)
playbuzz(c1, 0.5)
playbuzz(f1, 0.5)
playbuzz(a1, 1.5)
playbuzz(d2, 1)
playbuzz(c2, 0.5)
playbuzz(c2, 1)
playbuzz(a1s, 0.5)
playbuzz(a1, 2)

playbuzz(c1, 1.5)
playbuzz(c1, 0.5)
playbuzz(f1, 0.5)
playbuzz(a1, 1.5)
playbuzz(c2, 1)
playbuzz(a1s, 0.5)
playbuzz(a1s, 1)
playbuzz(a1, 0.5)
playbuzz(g1, 2)