import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 50)
        self.setWindowTitle('Пятая программа')

        self.add_button = QPushButton('+', self)
        self.add_button.resize(25, 25)
        self.add_button.move(75, 10)
        self.add_button.clicked.connect(self.add_button1)

        self.substract_button = QPushButton('-', self)
        self.substract_button.resize(25, 25)
        self.substract_button.move(100, 10)
        self.substract_button.clicked.connect(self.substract_button1)

        self.multiply_button = QPushButton('*', self)
        self.multiply_button.resize(25, 25)
        self.multiply_button.move(125, 10)
        self.multiply_button.clicked.connect(self.multiply_button1)

        self.first_value = QLineEdit(self)
        self.first_value.resize(70, 25)
        self.first_value.move(5, 10)
        self.first_value.setText('0')

        self.second_value = QLineEdit(self)
        self.second_value.resize(70, 25)
        self.second_value.move(150, 10)
        self.second_value.setText('0')

        self.name_label = QLabel(self)
        self.name_label.setText("=")
        self.name_label.move(220, 15)

        self.result = QLineEdit(self)
        self.result.resize(70, 25)
        self.result.move(230, 10)
        self.result.setEnabled(False)
        self.result.setText('0')

    def add_button1(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def substract_button1(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def multiply_button1(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())