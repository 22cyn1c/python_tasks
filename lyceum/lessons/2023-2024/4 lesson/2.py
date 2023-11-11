import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 70)
        self.setWindowTitle('Фокус со словами')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(165, 30)
        self.trick_button.clicked.connect(self.hello)
        self.trick_button.resize(25, 25)

        self.label = QLabel(self)
        self.label.setText("Выражение:")
        self.label.move(20, 10)
        self.label = QLabel(self)
        self.label.setText("Результат:")
        self.label.move(220, 10)

        self.first_value = QLineEdit(self)
        self.first_value.move(10, 30)

        self.second_value = QLineEdit(self)
        self.second_value.move(210, 30)

    def hello(self):
        txt = self.first_value.text()
        self.second_value.setText(str(eval(txt)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())