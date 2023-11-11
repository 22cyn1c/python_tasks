import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QPlainTextEdit


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle('Четвёртая программа')

        self.new_button = QPushButton('Новый файл', self)
        self.new_button.resize(120, 30)
        self.new_button.move(20, 100)
        self.new_button.clicked.connect(self.new_file)

        self.save_button = QPushButton('Сохранить файл', self)
        self.save_button.resize(120, 30)
        self.save_button.move(20, 150)
        self.save_button.clicked.connect(self.save_file)

        self.open_button = QPushButton('Открыть файл', self)
        self.open_button.resize(120, 30)
        self.open_button.move(20, 200)
        self.open_button.clicked.connect(self.open_file)

        self.filename_edit = QLineEdit(self)
        self.filename_edit.move(20, 50)
        self.filename_edit.resize(120, 30)

        self.text_edit = QPlainTextEdit(self)
        self.text_edit.move(150, 50)
        self.text_edit.resize(200, 200)

    def new_file(self):
        self.text_edit.clear()
        self.filename_edit.clear()

    def save_file(self):
        if len(self.filename_edit.text()):
            with open(self.filename_edit.text(), 'w') as fp:
                fp.write(self.text_edit.toPlainText())

    def open_file(self):
        try:
            with open(self.filename_edit.text(), 'r', encoding='UTF-8')as fp:
                sp = fp.read()
                self.text_edit.setPlainText(sp)
        except FileNotFoundError:
            return


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Notebook()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
