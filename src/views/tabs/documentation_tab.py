from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QLabel, QFrame, \
    QSizePolicy, QTextEdit

from src.common.tab_layout import TabLayout


class DocumentationTab(TabLayout):
    def __init__(self):
        super().__init__("Documentation","")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

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
