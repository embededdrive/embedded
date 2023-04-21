from signal import pause
from gpiozero import RotaryEncoder, Button, PWMLED

rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)
rotor.steps = -180
rot_btn = Button(12)

G = PWMLED(23)
Y = PWMLED(24)
R = PWMLED(25)

def change_hue():
    print(rotor.steps)

def say_hello():
    R.off()
    G.off()
    Y.off()

rotor.when_rotated = change_hue
rot_btn.when_pressed = say_hello

while True:
    if rotor.steps < -60:
        R.value = (rotor.steps + 180) / 120
    elif rotor.steps < 60:
        G.value = (rotor.steps + 60) / 120
    else:
        Y.value = (rotor.steps - 60) / 120

