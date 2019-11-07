import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
                             QPushButton, QGridLayout, QDesktopWidget)


class OutputField(QWidget):

    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__setWindowPosition()
        self.show()

    def __initUI(self):
        name = QLabel('Name')
        nameEdit = QLineEdit()
        nameEdit.setPlaceholderText('Name')

        description = QLabel('Description')
        descriptionEdit = QTextEdit()
        descriptionEdit.setPlaceholderText('Description')

        location = QLabel('Location')
        locationEdit = QLineEdit()
        locationEdit.setPlaceholderText('Location')

        browseButton = QPushButton('Browse')
        generateButton = QPushButton('Generate')

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(name, 0, 0)
        grid.addWidget(nameEdit, 0, 1, 1, 3)
        grid.addWidget(description, 1, 0)
        grid.addWidget(descriptionEdit, 1, 1, 1, 3)
        grid.addWidget(location, 2, 0)
        grid.addWidget(locationEdit, 2, 1, 1, 3)
        grid.addWidget(browseButton, 3, 3)
        grid.addWidget(generateButton, 4, 3)
        self.setWindowTitle('Output Field View')
        self.setLayout(grid)

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(300)
        qtRectangle.setHeight(250)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)
