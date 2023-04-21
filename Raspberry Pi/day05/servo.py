from gpiozero import AngularServo
from time import sleep

servo = AngularServo(21, min_angle=0, max_angle=90)

servo.angle=90

while True:
    pass