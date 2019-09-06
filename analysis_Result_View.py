import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
                             QPushButton, QGridLayout, QSplitter)
from PyQt5.QtCore import Qt

class AnalysisResult(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Analysis Result View'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 400
        self.initUI()

    def initUI(self):
        searchBox = QLineEdit()
        searchButton = QPushButton('Search')

        newButton = QPushButton('New')

        analysis_res_area = QLabel('Analysis Result Area')
        name = QLabel('Name')
        description = QLabel('Description')

        nameEdit = QLineEdit()
        descriptionEdit = QTextEdit()

        saveButton = QPushButton('Save')
        deleteButton = QPushButton('Delete')

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(searchBox, 1, 2)
        grid.addWidget(searchButton, 1, 3)
        grid.addWidget(newButton, 2, 3)
        grid.addWidget(analysis_res_area, 3, 2)
        grid.addWidget(name, 4, 0)
        grid.addWidget(nameEdit, 4, 2, 1, 3)
        grid.addWidget(description, 5, 0)
        grid.addWidget(descriptionEdit, 5, 2, 8, 3)
        grid.addWidget(deleteButton, 15, 2, 1, 1)
        grid.addWidget(saveButton, 15, 3, 1, 1)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(grid)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    analysisResWin = AnalysisResult()
    sys.exit(app.exec_())
