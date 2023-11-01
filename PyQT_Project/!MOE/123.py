import sys
from functools import partial
from PyQt5 import QtCore, QtWidgets


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QtWidgets.QAction('&Exit', self)
        exitAct.triggered.connect(QtWidgets.qApp.quit)
        newAct = QtWidgets.QAction('&New Tab', self)
        newAct.triggered.connect(self.newTab)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)
        self.tabbed = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabbed)

        self.show()

    def newTab(self):
        tab = TabbedFrame()
        ix = self.tabbed.addTab(tab, "")
        tab.nameTabChanged.connect(partial(self.tabbed.setTabText, ix))
        tab.updateTab()


class TabbedFrame(QtWidgets.QWidget):
    nameTabChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(TabbedFrame, self).__init__(parent)

        updateButton = QtWidgets.QPushButton("Update")
        updateButton.clicked.connect(self.updateTab)
        self.nameLineEdit = QtWidgets.QLineEdit("New Tab")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Tab Name"))
        layout.addWidget(self.nameLineEdit)
        layout.addWidget(updateButton)
        layout.addStretch()

    def updateTab(self):
        new_name = self.nameLineEdit.text()
        self.nameTabChanged.emit(new_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())