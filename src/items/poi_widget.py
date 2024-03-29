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
        self.comment = QLabel()
        self.name = QLabel(self.poi['name'])

        self.name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.name.setAlignment(Qt.AlignLeft)

        self.updateCommentState()

        if self.poi['type'] not in 'Function':
            self.check.setEnabled(False)

        layout.addWidget(self.check, 0, 0)
        layout.addWidget(self.name, 0, 1)
        layout.addWidget(self.comment, 0, 2)
        layout.setAlignment(self.name, Qt.AlignLeft)

        self.setLayout(layout)

    def updateCommentState(self):
        if 'comment' in self.poi.keys():
            self.comment.setPixmap(QtGui.QPixmap(f"res{os.sep}icons{os.sep}comment.png"))
        else:
            self.comment.setPixmap(QtGui.QPixmap())
