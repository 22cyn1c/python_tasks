import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 50)
        self.setWindowTitle('Фокус со словами')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(165, 10)
        self.trick_button.clicked.connect(self.hello)
        self.trick_button.resize(25, 25)

        self.first_value = QLineEdit(self)
        self.first_value.move(10, 10)

        self.second_value = QLineEdit(self)
        self.second_value.move(210, 10)

    def hello(self):
        txt = self.trick_button.text()
        if txt == '->':
            self.second_value.setText(self.first_value.text())
            self.first_value.setText('')
            self.trick_button.setText('<-')
        else:
            if txt == '<-':
                self.first_value.setText(self.second_value.text())
                self.second_value.setText('')
                self.trick_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())