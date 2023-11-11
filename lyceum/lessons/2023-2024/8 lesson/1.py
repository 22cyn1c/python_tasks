import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="red">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>50</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>R</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="green">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>120</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>G</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="blue">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>190</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>B</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="all">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>500</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>ALL</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">channelButtons</string>
    </attribute>
   </widget>
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>60</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Изображение</string>
    </property>
   </widget>
   <widget class="QPushButton" name="left">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>500</y>
      <width>201</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Против часовой стрелки</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">rotateButtons</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="right">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>500</y>
      <width>211</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>По часовой стрелке</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">rotateButtons</string>
    </attribute>
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
 <buttongroups>
  <buttongroup name="channelButtons"/>
  <buttongroup name="rotateButtons"/>
 </buttongroups>
</ui>
"""


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 700)
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.jpeg);;Все файлы (*)')[0]
        self.angle = 0
        self.orig_im = QImage(self.fname)
        self.curr_image = self.orig_im.copy()
        self.image.resize(500, 500)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)
        self.red.clicked.connect(self.changeRed)
        self.blue.clicked.connect(self.changeBlue)
        self.green.clicked.connect(self.changeGreen)
        self.all.clicked.connect(self.changeAll)
        self.right.clicked.connect(self.rotateRight)
        self.left.clicked.connect(self.rotateLeft)

    def changeRed(self):
        # print('red')
        self.curr_image = self.orig_im.copy()
        for y in range(self.curr_image.size().height()):
            for x in range(self.curr_image.size().width()):
                r, g, b, a = self.curr_image.pixelColor(x, y).getRgb()
                self.curr_image.setPixelColor(QPoint(x, y), QColor(r, 0, 0))
        tmp = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(tmp)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def changeBlue(self):
        self.curr_image = self.orig_im.copy()
        for y in range(self.curr_image.size().height()):
            for x in range(self.curr_image.size().width()):
                r, g, b, a = self.curr_image.pixelColor(x, y).getRgb()
                self.curr_image.setPixelColor(QPoint(x, y), QColor(0, 0, b))
        tmp = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(tmp)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def changeGreen(self):
        self.curr_image = self.orig_im.copy()
        for y in range(self.curr_image.size().height()):
            for x in range(self.curr_image.size().width()):
                r, g, b, a = self.curr_image.pixelColor(x, y).getRgb()
                self.curr_image.setPixelColor(QPoint(x, y), QColor(0, g, 0))
        tmp = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(tmp)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def changeAll(self):
        self.curr_image = self.orig_im.copy()
        for y in range(self.curr_image.size().height()):
            for x in range(self.curr_image.size().width()):
                r, g, b, a = self.curr_image.pixelColor(x, y).getRgb()
                self.curr_image.setPixelColor(QPoint(x, y), QColor(r, g, b))
        tmp = QTransform().rotate(self.angle)
        self.curr_image = self.curr_image.transformed(tmp)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def rotateLeft(self):
        # print('right', self.c)
        # self.curr_image = self.original_image.copy()
        self.angle -= 90
        self.angle %= 360
        self.curr_image = self.curr_image.transformed(QTransform().rotate(-90))
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)
        # self.c += 1

    def rotateRight(self):
        self.angle += 90
        self.angle %= 360
        self.curr_image = self.curr_image.transformed(QTransform().rotate(+90))
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec_())
