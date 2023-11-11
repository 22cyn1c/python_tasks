import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QLCDNumber


class MiniCalcularor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 115)
        self.setWindowTitle('Фокус со словами')

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.resize(self.calculate_button.sizeHint())
        self.calculate_button.move(130, 53)
        self.calculate_button.clicked.connect(self.hello)
        self.calculate_button.resize(50, 20)

        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(10, 10)
        self.label = QLabel(self)
        self.label.setText("Второе число(целое):")
        self.label.move(10, 60)
        self.label = QLabel(self)
        self.label.setText("Сумма:")
        self.label.move(225, 15)
        self.label = QLabel(self)
        self.label.setText("Разность:")
        self.label.move(210, 40)
        self.label = QLabel(self)
        self.label.setText("Произведение:")
        self.label.move(183, 65)
        self.label = QLabel(self)
        self.label.setText("Частное:")
        self.label.move(215, 90)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(260, 10)
        self.result_sub = QLCDNumber(self)
        self.result_sub.move(260, 35)
        self.result_mul = QLCDNumber(self)
        self.result_mul.move(260, 60)
        self.result_div = QLCDNumber(self)
        self.result_div.move(260, 85)

        self.number_1 = QLineEdit(self)
        self.number_1.move(10, 30)

        self.number_2 = QLineEdit(self)
        self.number_2.move(10, 80)

    def hello(self):
        txt = self.number_1.text()
        txt1 = self.number_2.text()
        self.result_sum.display(int(txt) + int(txt1))
        self.result_mul.display(int(txt) * int(txt1))
        self.result_sub.display(int(txt) - int(txt1))
        if txt1 == '0':
            self.result_div.display('Error')
        else:
            self.result_div.display(round(int(txt) / int(txt1), 3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalcularor()
    ex.show()
    sys.exit(app.exec())