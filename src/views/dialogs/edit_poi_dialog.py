from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit


class EditPoiDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        self.setWindowTitle('Edit Points of Interest')
        self.setFont(QFont("arial", 11))
        layout = QVBoxLayout()
        self.poiList = QListWidget()
        self.addPoiButton = QPushButton('Add New Point of Interest')

        # self.poiList.itemSelectionChanged.connect(self.useSelectedItem)

        layout.addLayout(self.searchBuilder())
        layout.addWidget(self.poiList)
        layout.addWidget(self.addPoiButton)

        self.setLayout(layout)

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Points of Interest")

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(500)
        qtRectangle.setHeight(800)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)
