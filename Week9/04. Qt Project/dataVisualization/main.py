
from PySide2.QtWidgets import *
from main_ui import Ui_MainWindow
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class myapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.figure, self.graph1 = pyplot.subplots(1, 3, figsize=(9, 3), sharey=True)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.lay.addWidget(self.canvas)

    def chart1(self):
        data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
        names = list(data.keys())
        values = list(data.values())

        self.graph1[0].clear()
        self.graph1[1].clear()
        self.graph1[2].clear()
        self.graph1[0].bar(names, values)
        self.graph1[1].scatter(names, values)
        self.graph1[2].plot(names, values)
        self.figure.suptitle('PySide GOGO')
        self.canvas.draw()

    def chart2(self):
        data = {'apple': 10, 'orange': 40, 'lemon': 30, 'lime': 20}
        names = list(data.keys())
        values = list(data.values())

        self.graph1[0].clear()
        self.graph1[1].clear()
        self.graph1[2].clear()
        self.graph1[0].bar(names, values)
        self.graph1[1].scatter(names, values)
        self.graph1[2].plot(names, values)
        self.figure.suptitle('PySide GOGO')
        self.canvas.draw()

app = QApplication()
win = myapp()
win.show()
app.exec_()


'''
import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')
print(type(fig))
print(type(axs[0]))
plt.show()
'''