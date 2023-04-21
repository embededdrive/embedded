from sense_hat import SenseHat

sense = SenseHat()

X = [50, 50, 50]
O = [255, 215, 0]

alpha = [
    X, X, X, O, O, X, X, X,
    X, X, O, X, X, O, X, O,
    X, O, X, X, X, O, O, X,
    O, X, X, X, X, X, O, X,
    O, X, X, X, X, X, O, X,
    O, X, X, X, X, O, O, X,
    X, O, X, X, O, X, O, X,
    X, X, O, O, X, X, X, O,
]

sense.set_pixels(alpha)