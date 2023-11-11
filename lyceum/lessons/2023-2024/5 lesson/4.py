import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem


template = '''<?xml version="1.0" encoding="UTF-8"?>
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
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>40</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>80</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Телефон</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactName">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>40</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactNumber">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>70</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addContactBtn">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>50</y>
      <width>81</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QListWidget" name="contactList">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>110</y>
      <width>256</width>
      <height>192</height>
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
'''


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        # uic.loadUi('flag.ui', self)  # Загружаем дизайн

        self.setFixedSize(350, 350)
        self.addContactBtn.clicked.connect(self.spis)

    def spis(self):
        b = str(self.contactName.text()) + ' ' + str(self.contactNumber.text())
        a = QListWidgetItem(b)
        self.contactList.addItem(a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec_())