from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QFrame, \
    QSizePolicy, QTextEdit, QDialog, QDesktopWidget


class DocumentationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("arial", 11))
        self.setWindowTitle("Help")
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        layout = QGridLayout()
        layout.addLayout(self.leftPanelBuilder(), 0, 0, 1, 2)
        layout.addLayout(self.rightPanelBuilder(), 0, 2, 1, 13)
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
        qtRectangle.setHeight(800)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)

    def keyPressEvent(self, event):
        if not event.key() == Qt.Key_Escape:
            super(DocumentationDialog, self).keyPressEvent(event)
