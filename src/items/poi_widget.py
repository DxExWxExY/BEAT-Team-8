import os

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QCheckBox, QLabel, QSizePolicy


class PoIWidget(QWidget):
    def __init__(self, poi):
        super().__init__()

        self.poi = poi
        layout = QGridLayout()

        self.check = QCheckBox('BP')
        name = QLabel(self.poi['name'])
        self.comment = QLabel()

        name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name.setAlignment(Qt.AlignLeft)

        self.updateCommentState()

        layout.addWidget(self.check, 0, 0)
        layout.addWidget(name, 0, 1)
        layout.addWidget(self.comment, 0, 2)
        layout.setAlignment(name, Qt.AlignLeft)

        self.setLayout(layout)

    def updateCommentState(self):
        if 'comment' in self.poi.keys():
            self.comment.setPixmap(QtGui.QPixmap(f"res{os.sep}icons{os.sep}comment.png"))
        else:
            self.comment.setPixmap(QtGui.QPixmap())
