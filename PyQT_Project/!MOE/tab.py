import sys
import qdarktheme
global language
global theme
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QRadioButton, QButtonGroup, \
    QLabel, QLineEdit
from PyQt5 import QtCore


template = ""


class Keyboard(QMainWindow):
    def __init__(self):
        global language
        global theme

        super().__init__()
        self.f = True

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
            self.tabs.setFixedSize(300, 200)
            self.tabs.showNormal()

            if language == 'english':
                self.tabs.addTab(SoundKeyboard(), 'Sound keyboard')
                self.tabs.addTab(Settings(), 'Settings')

            else:

                self.tabs.addTab(SoundKeyboard(), 'Звуковая клавиатура')
                self.tabs.addTab(Settings(), 'Настройки')

            qdarktheme.enable_hi_dpi()

class Settings(QWidget):
    rlTabChanged = QtCore.pyqtSignal()
    elTabChanged = QtCore.pyqtSignal()

    def __init__(self):
        global language
        global theme

        super().__init__()

        self.theme_change = QLabel(self)
        self.theme_change.move(20, 20)

        self.dark_theme = QRadioButton(self)
        self.dark_theme.move(20, 50)
        self.dark_theme.resize(100, 30)

        self.light_theme = QRadioButton(self)
        self.light_theme.move(20, 80)
        self.light_theme.resize(100, 30)

        self.sync_with_desktop = QRadioButton(self)
        self.sync_with_desktop.move(20, 110)
        self.sync_with_desktop.resize(100, 30)

        if language == 'english':
            self.dark_theme.setText('Dark theme')
            self.light_theme.setText('Light theme')
            self.sync_with_desktop.setText('System theme')
            self.theme_change.setText('Theme')

        else:
            self.dark_theme.setText('Тёмная тема')
            self.light_theme.setText('Светлая тема')
            self.sync_with_desktop.setText('Тема системы')
            self.theme_change.setText('Тема')

        self.dark_theme.toggled.connect(self.dark)
        self.light_theme.toggled.connect(self.light)
        self.sync_with_desktop.toggled.connect(self.synchronization)

        if theme == 'auto':
            self.sync_with_desktop.toggle()

        elif theme == 'dark':
            self.dark_theme.toggle()

        else:
            self.light_theme.toggle()

        self.language_change = QLabel(self)
        self.language_change.resize(55, 16)
        self.language_change.move(150, 20)
        self.russian = QRadioButton(self)
        self.russian.setText('Русский')
        self.russian.move(150, 60)
        self.russian.resize(75, 30)
        self.russian.toggled.connect(self.change_russian)
        self.russian.setAutoExclusive(True)

        self.english = QRadioButton(self)
        self.english.setText('English')
        self.english.move(150, 90)
        self.english.resize(75, 30)
        self.english.toggled.connect(self.change_english)
        self.english.setAutoExclusive(True)

        self.language_group = QButtonGroup()
        self.language_group.addButton(self.english)
        self.language_group.addButton(self.russian)

        if language == 'english':
            self.english.toggle()
            self.language_change.setText('Language')
        elif language == 'russian':
            self.russian.toggle()
            self.language_change.setText('Язык')

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

    def synchronization(self):
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
        self.sync_with_desktop.setText('Тема системы')
        self.language_change.setText('Язык')
        self.theme_change.setText('Тема')
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
        self.sync_with_desktop.setText('System theme')
        self.language_change.setText('Language')
        self.theme_change.setText('Theme')
        # self.nameTabChanged.emit('Sound keyboard')
        language = 'english'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}')


class SoundKeyboard(QWidget):
    pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Keyboard()
    sys.excepthook = except_hook
    sys.exit(app.exec())
