import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout


class EditPoi(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Analysis Result View'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 400
        self.__initUI()

    def __initUI(self):
        layout = QGridLayout()
