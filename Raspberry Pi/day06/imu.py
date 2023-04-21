from sense_hat import SenseHat

sense = SenseHat()

while True:
    acc = sense.get_compass_raw()
    print(f'[{acc["x"]:5.1f}] - ', end= ' ')
    print(f'[{acc["y"]:5.1f}] - ', end= ' ')
    print(f'[{acc["z"]:5.1f}]', end= ' ')
    print()