from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        designer_file = QFile("ui/form.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        loader.registerCustomWidget(MplWidget)
        self.ui = loader.load(designer_file, self)
        data = []
        f = open("0mtp20210821.txt", 'r')
        for line in f:
            data.append([str(x) for x in line.split()])
        for i in range(288):
            self.ui.listWidget.addItem(data[i + 1][1])
        f.close()
        designer_file.close()

        self.ui.pushButton.clicked.connect(self.update_graph)

        self.setWindowTitle("Вертикальный метеорологический температурный профиль")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

    def update_graph(self):
        data = []
        height = []
        temperature = []
        f = open("0mtp20210821.txt", 'r')
        for line in f:
            data.append([str(x) for x in line.split()])
        for i in range(21):
            height.append([float(data[0][i + 2].replace(',', '.'))])
        for i in range(288):
            if data[i + 1][1] == self.ui.listWidget.currentItem().text():
                for j in range(21):
                    temperature.append([float(data[i + 1][j + 2].replace(',', '.'))])
        self.ui.widget.canvas.axes.clear()
        self.ui.widget.canvas.axes.plot(temperature, height)
        self.ui.widget.canvas.axes.set_title(self.ui.listWidget.currentItem().text())
        self.ui.widget.canvas.draw()


app = QApplication([])
window = MainWidget()
window.show()
app.exec_()
