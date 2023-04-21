import RPi.GPIO as GPIO
import time

buz = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buz,GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(buz,262)
pwm.start(50.0)
time.sleep(1)

pwm.stop()
GPIO.cleanup()