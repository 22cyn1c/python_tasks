import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QTextBrowser


class Suffle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Четвёртая программа')

        self.button = QPushButton('Загрузить строки', self)
        self.button.resize(150, 30)
        self.button.move(30, 15)
        self.button.clicked.connect(self.run)

        self.text_field = QTextBrowser(self)
        self.text_field.resize(280, 300)
        self.text_field.move(10, 60)

    def run(self):
        with open('lines.txt', encoding='utf-8') as fp:
            sp = fp.readlines()
            txt = ''.join(sp[1::2]) + ''.join(sp[::2])
            self.text_field.setPlainText(txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suffle()
    ex.show()
    sys.exit(app.exec_())
