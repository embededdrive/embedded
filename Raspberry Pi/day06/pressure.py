from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    press = sense.get_pressure()
    
    print("Pressure : %s" % press)
    sleep(1)