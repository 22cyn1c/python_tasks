import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSlider
from PyQt5.QtGui import QPainter, QPen, QColor


class GoodMoodRising(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.color = QColor(255, 0, 0)
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle('Четвёртая программа')

        self.slider = QSlider(Qt.Vertical, self)
        self.slider.move(970, 40)
        self.slider.setValue(50)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.onValueChanged)
        self.slider.resize(20, 500)
        self.draw = True

    def onValueChanged(self, value):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter(self)
            qp.begin(self)
            pen, size = QPen(self.color), self.slider.value()
            qp.setPen(pen)
            qp.drawEllipse(0, 0, size * 10, size * 10)
            qp.drawEllipse(2 * size, 2 * size, 2 * size, 2 * size)
            qp.drawEllipse(6 * size, 2 * size, 2 * size, 2 * size)
            qp.drawArc(2 * size, 6 * size, 6 * size, 2 * size, -480, -1920)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GoodMoodRising()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
