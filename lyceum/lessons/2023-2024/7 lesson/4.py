import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import choice


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>120</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Случайная строка из файла</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="text_field">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>10</y>
      <width>571</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
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


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.button.clicked.connect(self.run)

    def run(self):
        fp = open('lines.txt', encoding='UTF-8')
        sp = fp.readlines()
        if sp:
            self.text_field.setText(choice(sp))
        fp.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec_())