from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QLabel, QFrame, \
    QSizePolicy

from src.common.tab_layout import TabLayout


class DocumentationTab(TabLayout):
    def __init__(self):
        super().__init__("Points of Interest View", "Detailed Points of Interest View")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        documentationList = QListWidget()

        documentationList.addItem("BEAT Documentation")
        documentationList.addItem("Plugin Structure")

        layout.addLayout(self.searchBuilder())
        layout.addWidget(documentationList)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        content = QLabel("# BEAT\n## To clone \n * TODO: determine IDE & Language")

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
