import sys, qdarktheme, os, sqlite3
from sys import argv, executable
global language
global theme
global q
global w
global e
global a
global s
global d
global f
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QRadioButton, QButtonGroup, \
    QLabel, QLineEdit, QSlider, QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.Qt import Qt
from PIL import Image

template = ""


class Keyboard(QMainWindow):
    def __init__(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f

        super().__init__()
        self.f = True

        for i in range(2):
            try:
                settings_file = open('settings.txt', mode='r+', encoding="utf8")

                try:
                    settings = settings_file.readlines()

                    language = settings[0][2:].strip('\n')
                    theme = settings[1][2:].strip('\n')
                    q = settings[2][2:].strip('\n')
                    w = settings[3][2:].strip('\n')
                    e = settings[4][2:].strip('\n')
                    a = settings[5][2:].strip('\n')
                    s = settings[6][2:].strip('\n')
                    d = settings[7][2:].strip('\n')
                    f = settings[8][2:].strip('\n')

                except IndexError:
                    settings_file.write('l=english\n')
                    settings_file.write('t=auto')
                    settings_file.write(f'q=')
                    settings_file.write(f'w=')
                    settings_file.write(f'e=')
                    settings_file.write(f'a=')
                    settings_file.write(f's=')
                    settings_file.write(f'd=')
                    settings_file.write(f'f=0')
                    settings_file.close()
                    settings_file = open('settings.txt', mode='r+', encoding="utf8")

                    settings = settings_file.readlines()

                    language = settings[0][2:].strip('\n')
                    theme = settings[1][2:].strip('\n')
                    q = ''
                    w = ''
                    e = ''
                    a = ''
                    s = ''
                    d = ''
                    f = '0'

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

            self.a = open('sql.db', 'a', encoding="utf8")
            self.a.close()

            # Устанавливаем соединение с базой данных
            connection = sqlite3.connect('sql.db')
            cursor = connection.cursor()

            # Выбираем всех пользователей
            cursor.execute("""CREATE TABLE IF NOT EXISTS sqlsound(
               button TEXT,
               namefile TEXT);""")

            if f == '0':
                f = '1'
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("Q", q))
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("W", w))
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("E", e))
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("A", a))
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("S", s))
                cursor.execute('INSERT INTO sqlsound (button, namefile) VALUES (?, ?)', ("D", d))

                connection.commit()
                connection.close()


class Settings(QWidget):
    rlTabChanged = QtCore.pyqtSignal()
    elTabChanged = QtCore.pyqtSignal()

    def __init__(self):
        global language
        global theme

        super().__init__()

        self.theme_change = QLabel(self)
        self.theme_change.move(20, 20)
        self.theme_change.resize(50, 15)

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
        self.russian.move(150, 50)
        self.russian.resize(75, 30)
        self.russian.toggled.connect(self.change_russian)
        self.russian.setAutoExclusive(True)

        self.english = QRadioButton(self)
        self.english.setText('English')
        self.english.move(150, 80)
        self.english.resize(75, 30)
        self.english.toggled.connect(self.change_english)
        self.english.setAutoExclusive(True)

        self.change_language = QPushButton(self)
        if language == 'english':
            self.change_language.setText('Change language')
        else:
            self.change_language.setText('Смена языка')
        self.change_language.move(150, 115)
        self.change_language.resize(105, 25)
        self.change_language.clicked.connect(self.restart1)

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
        global q
        global w
        global e
        global a
        global s
        global d
        global f

        qdarktheme.setup_theme("light")
        theme = 'light'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

    def dark(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f

        qdarktheme.setup_theme("dark")
        theme = 'dark'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

    def synchronization(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f

        qdarktheme.setup_theme("auto")
        theme = 'auto'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

    def change_russian(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f

        self.dark_theme.setText('Тёмная тема')
        self.light_theme.setText('Светлая тема')
        self.sync_with_desktop.setText('Тема системы')
        self.language_change.setText('Язык')
        self.theme_change.setText('Тема')
        self.change_language.setText('Смена языка')
        language = 'russian'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

    def change_english(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        self.dark_theme.setText('Dark theme')
        self.light_theme.setText('Light theme')
        self.sync_with_desktop.setText('System theme')
        self.language_change.setText('Language')
        self.theme_change.setText('Theme')
        self.change_language.setText('Change language')
        # self.nameTabChanged.emit('Sound keyboard')
        language = 'english'
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

    def restart1(self):
        os.execl(executable, os.path.abspath(__file__), *argv)


class QKeyDialog(QDialog):

    def __init__(self, parent):
        global q
        super().__init__(parent)
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(q, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        q = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class WKeyDialog(QDialog):
    def __init__(self, parent):
        global w
        super().__init__(parent)
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(w, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        w = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class EKeyDialog(QDialog):
    def __init__(self, parent):
        global e
        super().__init__(parent)
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(e, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        e = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class AKeyDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        global a
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(a, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        a = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class SKeyDialog(QDialog):
    def __init__(self, parent):
        global s
        super().__init__(parent)
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(s, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        s = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class DKeyDialog(QDialog):
    def __init__(self, parent):
        global d
        super().__init__(parent)
        global language
        self.setFixedSize(225, 50)
        if language == 'english':
            self.label_nameofsound = QLabel('Sound file', self)
        else:
            self.label_nameofsound = QLabel('Файл звука', self)
        self.label_nameofsound.move(5, 15)
        self.line_nameofsound = QLineEdit(d, self)
        self.line_nameofsound.move(75, 12)
        self.line_nameofsound.resize(100, 25)
        self.button_nameofsound = QPushButton('OK', self)
        self.button_nameofsound.move(180, 12)
        self.button_nameofsound.resize(35, 25)
        self.button_nameofsound.clicked.connect(self.edited)
        self.button_nameofsound.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        d = self.line_nameofsound.text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')


class DataBase(QDialog):
    def __init__(self, parent):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        super().__init__(parent)
        self.setFixedSize(222, 240)
        if language == 'english':
            self.button_table = QPushButton('Save data', self)
        else:
            self.button_table = QPushButton('Сохранить данные', self)
        self.button_table.move(10, 210)
        self.button_table.resize(200, 25)
        self.table_sounds = QTableWidget(self)
        self.table_sounds.setFixedSize(250, 205)
        self.table_sounds.setColumnCount(2)
        self.table_sounds.setRowCount(6)
        if language == 'english':
            self.table_sounds.setHorizontalHeaderLabels(["Key", "Sound file"])
        else:
            self.table_sounds.setHorizontalHeaderLabels(["Клавиша", "Файл звука"])
        self.table_sounds.setItem(0, 0, QTableWidgetItem("Q"))
        self.table_sounds.setItem(1, 0, QTableWidgetItem("W"))
        self.table_sounds.setItem(2, 0, QTableWidgetItem("E"))
        self.table_sounds.setItem(3, 0, QTableWidgetItem("A"))
        self.table_sounds.setItem(4, 0, QTableWidgetItem("S"))
        self.table_sounds.setItem(5, 0, QTableWidgetItem("D"))
        self.table_sounds.item(0, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.item(1, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.item(2, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.item(3, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.item(4, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.item(5, 0).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table_sounds.setItem(0, 1, QTableWidgetItem(q))
        self.table_sounds.setItem(1, 1, QTableWidgetItem(w))
        self.table_sounds.setItem(2, 1, QTableWidgetItem(e))
        self.table_sounds.setItem(3, 1, QTableWidgetItem(a))
        self.table_sounds.setItem(4, 1, QTableWidgetItem(s))
        self.table_sounds.setItem(5, 1, QTableWidgetItem(d))

        self.button_table.clicked.connect(self.edited)
        self.button_table.clicked.connect(self.close)

    def edited(self):
        global language
        global theme
        global q
        global w
        global e
        global a
        global s
        global d
        global f
        q = self.table_sounds.item(0, 1).text()
        w = self.table_sounds.item(1, 1).text()
        e = self.table_sounds.item(2, 1).text()
        a = self.table_sounds.item(3, 1).text()
        s = self.table_sounds.item(4, 1).text()
        d = self.table_sounds.item(5, 1).text()
        clean = open('settings.txt', 'w+')
        clean.seek(0)
        clean.close()
        with open('settings.txt', mode='r+', encoding="utf8") as settings_file:
            settings_file.flush()
            settings_file.write(f'l={language}\n')
            settings_file.write(f't={theme}\n')
            settings_file.write(f'q={q}\n')
            settings_file.write(f'w={w}\n')
            settings_file.write(f'e={e}\n')
            settings_file.write(f'a={a}\n')
            settings_file.write(f's={s}\n')
            settings_file.write(f'd={d}\n')
            settings_file.write(f'f={f}')

        connection = sqlite3.connect('sql.db')
        cursor = connection.cursor()

        # Выбираем всех пользователей
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (q, 'Q'))
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (w, 'W'))
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (e, 'E'))
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (a, 'A'))
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (s, 'S'))
        cursor.execute('UPDATE sqlsound SET namefile = ? WHERE button = ?', (d, 'D'))

        connection.commit()
        connection.close()


class SoundKeyboard(QWidget):
    def __init__(self):
        global language
        global theme

        super().__init__()

        if language == 'english':
            self.label_panel = QLabel(self)
            self.label_panel.move(20, 25)
            self.label_panel.setText('Soundbar')
        else:
            self.label_panel = QLabel(self)
            self.label_panel.move(20, 25)
            self.label_panel.setText('Звуковая панель')

        self.panel_button1 = QPushButton(self)
        self.panel_button1.move(20, 60)
        self.panel_button1.resize(35, 35)
        self.panel_button1.setText("Q")
        self.panel_button1.setFont(QFont('Calibri', 14))
        self.panel_button1.clicked.connect(self.buttonconnectQ)

        self.panel_button2 = QPushButton(self)
        self.panel_button2.move(60, 60)
        self.panel_button2.resize(35, 35)
        self.panel_button2.setText('W')
        self.panel_button2.setFont(QFont('Calibri', 14))
        self.panel_button2.clicked.connect(self.buttonconnectW)

        self.panel_button3 = QPushButton(self)
        self.panel_button3.move(100, 60)
        self.panel_button3.resize(35, 35)
        self.panel_button3.setText("E")
        self.panel_button3.setFont(QFont('Calibri', 14))
        self.panel_button3.clicked.connect(self.buttonconnectE)

        self.panel_button4 = QPushButton(self)
        self.panel_button4.move(40, 100)
        self.panel_button4.resize(35, 35)
        self.panel_button4.setText("A")
        self.panel_button4.setFont(QFont('Calibri', 14))
        self.panel_button4.clicked.connect(self.buttonconnectA)

        self.panel_button5 = QPushButton(self)
        self.panel_button5.move(80, 100)
        self.panel_button5.resize(35, 35)
        self.panel_button5.setText("S")
        self.panel_button5.setFont(QFont('Calibri', 14))
        self.panel_button5.clicked.connect(self.buttonconnectS)

        self.panel_button6 = QPushButton(self)
        self.panel_button6.move(120, 100)
        self.panel_button6.resize(35, 35)
        self.panel_button6.setText("D")
        self.panel_button6.setFont(QFont('Calibri', 14))
        self.panel_button6.clicked.connect(self.buttonconnectD)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.move(180, 50)
        self.volume_slider.setValue(100)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.valueChanged.connect(self.volume_changed)

        if language == 'english':
            self.label_volume = QLabel('Volume', self)
            self.label_volume.move(175, 25)
        else:
            self.label_volume = QLabel('Громкость', self)
            self.label_volume.move(175, 25)

        if language == 'english':
            self.label_database = QLabel('Database', self)
            self.label_database.move(175, 80)
        else:
            self.label_database = QLabel('База данных', self)
            self.label_database.move(175, 80)

        if language == 'english':
            self.database_button = QPushButton(self)
            self.database_button.move(175, 100)
            self.database_button.resize(100, 35)
            self.database_button.setText("Database")
            self.database_button.clicked.connect(self.databasebuttonconnect)
        else:
            self.database_button = QPushButton(self)
            self.database_button.move(175, 100)
            self.database_button.resize(100, 35)
            self.database_button.setText("База данных")
            self.database_button.clicked.connect(self.databasebuttonconnect)

        self.playerq = QMediaPlayer(self)
        self.playere = QMediaPlayer(self)
        self.playerw = QMediaPlayer(self)
        self.playera = QMediaPlayer(self)
        self.players = QMediaPlayer(self)
        self.playerd = QMediaPlayer(self)

        self.label_im = QLabel(self)
        self.label_im.move(235, 20)
        self.pm = QPixmap('im4.png')
        self.label_im.setPixmap(self.pm)

    def buttonconnectQ(self):
        self.keywidgetq = QKeyDialog(self)
        self.keywidgetq.show()

    def buttonconnectW(self):
        self.keywidgetw = WKeyDialog(self)
        self.keywidgetw.show()

    def buttonconnectE(self):
        self.keywidgete = EKeyDialog(self)
        self.keywidgete.show()

    def buttonconnectA(self):
        self.keywidgeta = AKeyDialog(self)
        self.keywidgeta.show()

    def buttonconnectS(self):
        self.keywidgets = SKeyDialog(self)
        self.keywidgets.show()

    def buttonconnectD(self):
        self.keywidgetd = DKeyDialog(self)
        self.keywidgetd.show()

    def databasebuttonconnect(self):
        self.dbbutton = DataBase(self)
        self.dbbutton.show()

    def volume_changed(self, value):
        if value >= 66:
            self.pm = QPixmap('im4.png')
            self.label_im.setPixmap(self.pm)
        elif 33 <= value < 66:
            self.pm = QPixmap('im3.png')
            self.label_im.setPixmap(self.pm)
        elif 0 < value < 33:
            self.pm = QPixmap('im2.png')
            self.label_im.setPixmap(self.pm)
        else:
            self.pm = QPixmap('im1.png')
            self.label_im.setPixmap(self.pm)

        self.playerq.setVolume(value)
        self.playere.setVolume(value)
        self.playera.setVolume(value)
        self.playerw.setVolume(value)
        self.players.setVolume(value)
        self.playerd.setVolume(value)

    def keyPressEvent(self, ev):
        global q
        global w
        global e
        global a
        global s
        global d
        if ev.key() == Qt.Key_Q:
            ffp = os.path.join(os.getcwd(), q)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.playerq.setMedia(content)
            self.playerq.play()
        if ev.key() == Qt.Key_W:
            ffp = os.path.join(os.getcwd(), w)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.playerw.setMedia(content)
            self.playerw.play()
        if ev.key() == Qt.Key_E:
            ffp = os.path.join(os.getcwd(), e)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.playere.setMedia(content)
            self.playere.play()
        if ev.key() == Qt.Key_A:
            ffp = os.path.join(os.getcwd(), a)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.playera.setMedia(content)
            self.playera.play()
        if ev.key() == Qt.Key_S:
            ffp = os.path.join(os.getcwd(), s)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.players.setMedia(content)
            self.players.play()
        if ev.key() == Qt.Key_D:
            ffp = os.path.join(os.getcwd(), d)
            url = QUrl.fromLocalFile(ffp)
            content = QMediaContent(url)
            self.playerd.setMedia(content)
            self.playerd.play()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Keyboard()
    sys.excepthook = except_hook
    sys.exit(app.exec())