from datetime import datetime
import io
import sys

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
    <width>910</width>
    <height>565</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Минипланировщик</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QCalendarWidget" name="calendarWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>40</y>
      <width>451</width>
      <height>361</height>
     </rect>
    </property>
   </widget>
   <widget class="QTimeEdit" name="timeEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>451</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>430</y>
      <width>451</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addEventBtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>470</y>
      <width>451</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить событие</string>
    </property>
   </widget>
   <widget class="QListWidget" name="eventList">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>10</y>
      <width>431</width>
      <height>521</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>910</width>
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


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.addEventBtn.clicked.connect(self.run)
        self.setWindowTitle("Минипланировщик")
        self.events = []

    def run(self):
        tme = datetime(self.calendarWidget.selectedDate().year(),
                       self.calendarWidget.selectedDate().month(),
                       self.calendarWidget.selectedDate().day(), self.timeEdit.time().hour(),
                       self.timeEdit.time().minute())
        txt = self.lineEdit.text()
        self.events.append((txt, tme))
        self.events = sorted(self.events, key=lambda x: x[1])
        self.eventList.clear()
        # print(self.events[0][0])
        self.eventList.addItems([f'{event[1]} - {event[0]}' for event in self.events])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec_())
