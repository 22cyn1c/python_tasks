import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>468</width>
    <height>215</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>81</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя файла</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>60</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Максимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>100</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Минимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>140</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Среднее значение</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="filenameEdit">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>20</y>
      <width>181</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="maxEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>60</y>
      <width>251</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="minEdit">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>100</y>
      <width>271</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="avgEdit">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>140</y>
      <width>271</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0,00</string>
    </property>
   </widget>
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>10</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Рассчитать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>468</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        # uic.loadUi('stata.ui', self)  # Загружаем дизайн
        self.filenameEdit.setText("input.txt")
        self.button.clicked.connect(self.run)

    def write(self, mx, mn, avg):
        self.minEdit.setText(str(mn))
        self.maxEdit.setText(str(mx))
        self.avgEdit.setText(f'{avg:.2f}')

    def run(self):
        fle = self.filenameEdit.text()
        try:
            fp = open(fle, mode="rb")
            sp = fp.read().strip()
            if len(sp):
                try:
                    x = [int(t) for t in sp.split()]
                    self.write(max(x), min(x), round(sum(x) / len(x), 2))
                    with open("out.txt", "w", encoding="UTF-8") as fp:
                        fp.write(f"Максимальное значение = {self.maxEdit.text()}\n")
                        fp.write(f"Минимальное значение = {self.minEdit.text()}\n")
                        fp.write(f"Среднее значение = {self.avgEdit.text()}\n")
                    self.statusbar.showMessage("")
                except ValueError:
                    self.write(0, 0, 0)
                    self.statusbar.showMessage("Файл содержит некорректные данные")

            else:
                self.write(0, 0, 0)
                self.statusbar.showMessage("Указанный файл пуст")
            fp.close()

        except FileNotFoundError:
            self.write(0, 0, 0)
            self.statusbar.showMessage("Указанный файл не существует")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec_())