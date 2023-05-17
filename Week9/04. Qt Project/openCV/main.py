from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from test import Ui_MainWindow
import cv2
import numpy

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.img = cv2.imread('burger.png')
        self.img = self.processingImage(self.img)
        self.printImage(self.img, self.pic)

    def processingImage(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = numpy.ones((3,3))
        img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        return img

    def printImage(self, imgBGR, pic):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))

app = QApplication()
win = MyApp()
win.show()
app.exec_()