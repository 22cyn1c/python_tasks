import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRectF


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>900</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>30</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Показать</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>30</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>side</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>60</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>coeff</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>90</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>n</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>30</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>300</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>60</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0.9</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_3">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>90</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>5</string>
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


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.c = 0
        desinger = io.StringIO(template)
        uic.loadUi(desinger, self)
        # uic.loadUi('square.ui', self)
        self.color = QColor(255, 0, 0)
        self.flag = False
        self.btn.clicked.connect(self.run)

    def run(self):
        self.side = int(self.lineEdit.text())
        self.koef = float(self.lineEdit_2.text())
        self.cnt = int(self.lineEdit_3.text())
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_square(qp)
            # Завершаем рисование
            qp.end()

    def draw_square(self, qp):
        qp.setPen(self.color)
        side, x, y = self.side, 50, 130
        for _ in range(self.cnt):
            qp.drawRect(QRectF(x, y, side, side))
            delta = (1 - self.koef) * side / 2
            side = self.koef * side
            x, y = x + delta, y + delta


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec_())
