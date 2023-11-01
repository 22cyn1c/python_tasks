import sys
import qdarktheme
import datetime as dt
import time

global language
global theme

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QRadioButton, QButtonGroup, \
    QLabel, QLineEdit
from PyQt5 import QtGui

template = ""


class Clock(QMainWindow):
    def __init__(self):
        global language
        global theme

        super().__init__()
        for i in range(2):
            try:
                settings_file = open('settings.txt', mode='r+', encoding="utf8")

                try:
                    settings = settings_file.readlines()

                    language = settings[0][2:].strip('\n')
                    theme = settings[1][2:].strip('\n')

                except IndexError:
                    settings_file.write('l=english\n')
                    settings_file.write('t=auto')
                    settings_file.close()
                    settings_file = open('settings.txt', mode='r+', encoding="utf8")

                    settings = settings_file.readlines()

                    language = settings[0][2:].strip('\n')
                    theme = settings[1][2:].strip('\n')

            except FileNotFoundError:
                tmp = open('settings.txt', mode='w+', encoding="utf8")
                tmp.close()
                continue

            self.tabs = QTabWidget()
            self.tabs.showMaximized()

            if language == 'english':

                self.tabs.addTab(Settings(), 'Settings')
                self.tabs.addTab(Timer(), 'Timer')

            else:

                self.tabs.addTab(Settings(), 'Настройки')
                self.tabs.addTab(Timer(), 'Таймер')

            qdarktheme.enable_hi_dpi()


class Settings(QWidget):
    def __init__(self):
        global language
        global theme

        super().__init__()

        self.dark_theme = QRadioButton(self)
        self.dark_theme.move(90, 90)
        self.dark_theme.resize(150, 150)

        self.light_theme = QRadioButton(self)
        self.light_theme.move(600, 600)
        self.light_theme.resize(150, 150)

        self.sync_with_desktop = QRadioButton(self)
        self.sync_with_desktop.move(300, 300)
        self.sync_with_desktop.resize(150, 150)

        if language == 'english':
            self.dark_theme.setText('Dark theme')
            self.light_theme.setText('Light theme')
            self.sync_with_desktop.setText('Synchronization with computer')

        else:
            self.dark_theme.setText('Тёмная тема')
            self.light_theme.setText('Светлая тема')
            self.sync_with_desktop.setText('Синхронизация с компьютером (по умолчанию)')

        self.dark_theme.toggled.connect(self.dark)
        self.light_theme.toggled.connect(self.light)
        self.sync_with_desktop.toggled.connect(self.sync)

        self.theme_group = QButtonGroup()
        self.theme_group.addButton(self.dark_theme)
        self.theme_group.addButton(self.light_theme)
        self.theme_group.addButton(self.sync_with_desktop)

        if theme == 'auto':
            self.sync_with_desktop.toggle()

        elif theme == 'dark':
            self.dark_theme.toggle()

        else:
            self.light_theme.toggle()

        self.russian = QRadioButton(self)
        self.russian.setText('Русский')
        self.russian.move(300, 700)
        self.russian.resize(150, 150)
        self.russian.toggled.connect(self.change_russian)
        self.russian.setAutoExclusive(True)

        self.english = QRadioButton(self)
        self.english.setText('English')
        self.english.move(500, 700)
        self.english.resize(150, 150)
        self.english.toggled.connect(self.change_english)
        self.english.setAutoExclusive(True)

        self.language_group = QButtonGroup()
        self.language_group.addButton(self.english)
        self.language_group.addButton(self.russian)

        if language == 'english':
            self.english.toggle()
        elif language == 'russian':
            self.russian.toggle()

    def light(self):
        global language
        global theme

        qdarktheme.setup_theme("light")
        theme = 'light'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')

    def dark(self):
        global language
        global theme

        qdarktheme.setup_theme("dark")
        theme = 'dark'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')

    def sync(self):
        global language
        global theme

        qdarktheme.setup_theme("auto")
        theme = 'auto'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')

    def change_russian(self):
        global language
        global theme

        self.dark_theme.setText('Тёмная тема')
        self.light_theme.setText('Светлая тема')
        self.sync_with_desktop.setText('Синхронизация с компьютером (по умолчанию)')
        language = 'russian'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')

    def change_english(self):
        global language
        global theme

        self.dark_theme.setText('Dark theme')
        self.light_theme.setText('Light theme')
        self.sync_with_desktop.setText('Synchronization with computer')
        language = 'english'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.timer_display = QLabel('0:0:0', self)

        font = QtGui.QFont("'Arial'", 20)
        self.timer_display.setFont(font)
        self.move(40, 300)
        self.resize(100, 100)

        self.start_button = QPushButton('>', self)
        self.start_button.clicked.connect(self.start_timer)
        self.start_button.move(40, 500)
        self.start_button.resize(100, 50)

        self.lap_button = QPushButton('!', self)
        self.lap_button.clicked.connect(self.lap_result)
        self.lap_button.move(40, 200)
        self.lap_button.resize(100, 50)

        self.timer_hours = QLineEdit(self)
        self.timer_hours.move(60, 100)
        self.timer_hours.resize(20, 20)

        self.timer_seconds = QLineEdit(self)
        self.timer_seconds.move(180, 100)
        self.timer_seconds.resize(20, 20)

        self.timer_seconds = QLineEdit(self)
        self.timer_seconds.move(230, 100)
        self.timer_seconds.resize(20, 20)

    def start_timer(self):
        pass

    def lap_result(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Clock()
    sys.excepthook = except_hook
    sys.exit(app.exec())
