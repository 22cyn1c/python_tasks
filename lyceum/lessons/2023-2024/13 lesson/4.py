import sys
from random import randrange

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('Координаты')

        self.setMouseTracking(True)

        self.button = QPushButton('❤', self)
        self.button.move(100, 100)
        self.button.resize(40, 40)

        self.cx = 100
        self.cy = 100

    def mouseMoveEvent(self, event):
        if self.cx + self.cy - 40 <= event.x() + event.y() <= self.cx + self.cy + 40:
            y = randrange(1, 460)
            x = randrange(1, 460)
            self.cx = x
            self.cy = y
            self.button.move(self.cx, self.cy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())