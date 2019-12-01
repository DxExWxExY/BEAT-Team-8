from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QLabel, QFrame, \
    QSizePolicy

from src.common.tab_layout import TabLayout


class DocumentationTab(TabLayout):
    def __init__(self):
        super().__init__("Documentation", "Detaileds ")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.documentationList = QListWidget()
        layout.addLayout(self.searchBuilder())
        layout.addWidget(self.documentationList)

        # documentationList.addItem("BEAT Documentation")
        # documentationList.addItem("Plugin Structure")


        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        content = QLabel()

        content.setFrameShape(QFrame.Panel)
        content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(content, 0, 0)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Documentation")

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout
