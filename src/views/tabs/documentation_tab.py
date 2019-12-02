from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QLabel, QFrame, \
    QSizePolicy, QTextEdit


class DocumentationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("arial", 11))
        self.setWindowTitle("Help")
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        layout = QGridLayout()
        layout.addLayout(self.leftPanelBuilder(), 0, 0, 1, 5)
        layout.addLayout(self.rightPanelBuilder(), 0, 5, 1, 10)
        self.setLayout(layout)

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.documentationList = QListWidget()
        layout.addLayout(self.searchBuilder())
        layout.addWidget(self.documentationList)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        self.content = QTextEdit()

        self.content.setFrameShape(QFrame.Panel)
        self.content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.content, 0, 0)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Documentation")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(900)
        qtRectangle.setHeight(700)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)
