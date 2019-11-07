import os

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QGridLayout, QLabel, QListWidget, QPushButton

from src.common.constants import BUTTON_STYLE


class ProjectSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("arial", 11))
        self.setWindowTitle("BEAT")
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        layout = QGridLayout()

        icon = QLabel()
        beat = QLabel("\nBEAT\n")
        beat.setAlignment(Qt.AlignCenter)
        icon.setPixmap(QtGui.QPixmap(f"res{os.sep}icons{os.sep}beatSmall.png"))
        self.deleteProject = QPushButton("Delete")
        self.openProject = QPushButton("Open")
        self.addProject = QPushButton("Create New Project")
        addIcon = QtGui.QIcon()
        addIcon.addPixmap(QtGui.QPixmap(f"res{os.sep}icons{os.sep}add.png"))
        self.addProject.setIcon(addIcon)
        self.addProject.setStyleSheet(BUTTON_STYLE)


        self.projectsList = QListWidget()

        layout.addWidget(icon, 0, 2, 1, 1)
        layout.addWidget(beat , 1, 2)
        layout.addWidget(self.addProject, 2, 0, 1, 5)
        layout.addWidget(QLabel('\nExisting Projects'), 3, 2)
        layout.addWidget(self.projectsList, 4, 0, 1, 5)
        layout.addWidget(self.deleteProject, 5, 0, 1, 1)
        layout.addWidget(self.openProject, 5, 4, 1, 1)


        self.setLayout(layout)

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(500)
        qtRectangle.setHeight(500)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)