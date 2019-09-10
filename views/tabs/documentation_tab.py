from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QTextEdit, QLabel

from common.tab_layout import TabLayout


class DocumentationTab(TabLayout):
    def __init__(self):
        super().__init__("Points of Interest View", "Detailed Points of Interest View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        documentationList = QListWidget()
        addProjectButton = QPushButton('New Project')

        documentationList.addItem("BEAT Documentation")
        documentationList.addItem("Plugin Structure")

        layout.addLayout(self.searchBuilder())
        layout.addWidget(documentationList)
        layout.addWidget(addProjectButton)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        content = QLabel()


        layout.addWidget(content, 0, 0)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Projects")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout
