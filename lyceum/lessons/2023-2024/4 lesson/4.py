import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QCheckBox
from PyQt5.QtCore import Qt


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 130)
        self.setWindowTitle('Шестая программа')

        self.edit1 = QLineEdit(self)
        self.edit1.move(90, 10)

        self.edit2 = QLineEdit(self)
        self.edit2.move(90, 40)

        self.edit3 = QLineEdit(self)
        self.edit3.move(90, 70)

        self.edit4 = QLineEdit(self)
        self.edit4.move(90, 100)

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.move(20, 11)
        self.checkbox1.toggle()
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(self.hide1)

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.move(20, 41)
        self.checkbox2.toggle()
        self.checkbox2.setChecked(True)
        self.checkbox2.stateChanged.connect(self.hide2)

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.move(20, 71)
        self.checkbox3.toggle()
        self.checkbox3.setChecked(True)
        self.checkbox3.stateChanged.connect(self.hide3)

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.move(20, 101)
        self.checkbox4.toggle()
        self.checkbox4.setChecked(True)
        self.checkbox4.stateChanged.connect(self.hide4)

    def hide1(self, checkbox1):
        if checkbox1 == Qt.Checked:
            self.edit1.setVisible(True)
        else:
            self.edit1.setVisible(False)

    def hide2(self, checkbox2):
        if checkbox2 == Qt.Checked:
            self.edit2.setVisible(True)
        else:
            self.edit2.setVisible(False)

    def hide3(self, checkbox3):
        if checkbox3 == Qt.Checked:
            self.edit3.setVisible(True)
        else:
            self.edit3.setVisible(False)

    def hide4(self, checkbox4):
        if checkbox4 == Qt.Checked:
            self.edit4.setVisible(True)
        else:
            self.edit4.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
