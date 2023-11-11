import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


# from ui_01 import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.number = ''
        self.buffer = ''
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        # self.pushButton.clicked.connect(self.run)
        self.btn1.clicked.connect(self.run)
        self.btn2.clicked.connect(self.run)
        self.btn3.clicked.connect(self.run)
        self.btn4.clicked.connect(self.run)
        self.btn5.clicked.connect(self.run)
        self.btn6.clicked.connect(self.run)
        self.btn7.clicked.connect(self.run)
        self.btn8.clicked.connect(self.run)
        self.btn9.clicked.connect(self.run)
        self.btn0.clicked.connect(self.run)
        self.btn_plus.clicked.connect(self.run)
        self.btn_eq.clicked.connect(self.run)
        self.btn_div.clicked.connect(self.run)
        self.btn_dot.clicked.connect(self.run)
        self.btn_minus.clicked.connect(self.run)
        self.btn_mult.clicked.connect(self.run)
        self.btn_pow.clicked.connect(self.run)
        self.btn_sqrt.clicked.connect(self.run)
        self.btn_fact.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.run)

    def run(self):
        ch = self.sender().text()
        if ch.isdigit() or ch == '.' and len(self.buffer):
            if ch == '.' and '.' in self.buffer:
                return
            self.buffer += ch
            self.table.display(self.buffer)
        elif ch in ['!', '√']:
            if ch == '!':
                nm = int(float(str(eval(self.number + self.buffer))))
                if nm >= 0:
                    rs = 1
                    for k in range(1, nm + 1):
                        rs *= k
                    self.buffer = str(rs)
                    self.number = str(rs)
                    self.table.display(self.buffer[:5])
                else:
                    self.table.display('Error')
            elif ch == '√':
                nm = float(str(eval(self.number + self.buffer)))
                if nm >= 0:
                    self.buffer = str(round(nm ** 0.5, 1))
                    self.number = self.buffer
                    self.table.display(self.buffer[:5])
                else:
                    self.table.display('Error')
            self.buffer = ''
        elif ch in '+/-*^':
            if ch == '^':
                ch = '**'
            rs = str(eval(self.number + self.buffer))
            self.table.display(rs[:5])
            self.number = str(rs) + ch
            self.buffer = ''
        elif ch == '=':
            if not (len(self.buffer) == 0 or self.buffer == '0' and self.number[-1] == '/'):
                self.number = str(round(eval(self.number + self.buffer), 1))
                self.buffer = ''
                self.table.display(self.number[:5])
            else:
                self.table.display('Error')
        elif ch == 'С':
            self.number = ''
            self.buffer = ''
            self.table.display('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())