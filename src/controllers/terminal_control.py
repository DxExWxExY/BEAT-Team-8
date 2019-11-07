from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *

class TerminalControl(QPlainTextEdit):
    def __init__(self):
        self.setPlainText("$ ")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.handleCommand()

    def handleCommand(self):
        print(self.toPlainText())

