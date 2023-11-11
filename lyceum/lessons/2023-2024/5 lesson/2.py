import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>273</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QRadioButton" name="radioButton">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>50</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Синий</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_1</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_2">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>80</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Красный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_1</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_3">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>110</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Зелёный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_1</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_4">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>50</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Синий</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_2</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_5">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>80</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Красный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_2</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_6">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>110</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Зелёный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_2</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_7">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>110</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Синий</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_3</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_8">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>50</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Красный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_3</string>
    </attribute>
   </widget>
   <widget class="QRadioButton" name="radioButton_9">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>80</y>
      <width>82</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Зелёный</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">color_group_3</string>
    </attribute>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>170</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Ура</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>30</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Цвет №1</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>30</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Цвет №2</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>30</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Цвет №3</string>
    </property>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>590</x>
      <y>180</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
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
 <buttongroups>
  <buttongroup name="color_group_1"/>
  <buttongroup name="color_group_2"/>
  <buttongroup name="color_group_3"/>
 </buttongroups>
</ui>
'''


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        # uic.loadUi('flag.ui', self)  # Загружаем дизайн

        self.setFixedSize(800, 300)
        self.make_flag.clicked.connect(self.run)
        self.color_group_1.buttonClicked.connect(self.set_color)
        self.color_group_2.buttonClicked.connect(self.set_color)
        self.color_group_3.buttonClicked.connect(self.set_color)
        self.data = {self.color_group_1: "Синий", self.color_group_2: "Синий",
                     self.color_group_3: "Синий"}
        self.result.resize(200, 30)
        self.setWindowTitle("Текстовый флаг")
        self.make_flag.setText("Сделать флаг")

    def set_color(self, btn):
        self.data[self.sender()] = btn.text()

    def run(self):
        a, b, c = [self.data[key] for key in self.data]
        self.result.setText(f'Цвета: {a}, {b} и {c}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())