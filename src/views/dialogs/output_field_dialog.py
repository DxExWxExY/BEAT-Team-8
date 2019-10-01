import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
                             QPushButton, QGridLayout)


class OutputField(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Output Field View'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 250
        self.initUI()

    def initUI(self):
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
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    outputFieldView = OutputField()
    sys.exit(app.exec_())
