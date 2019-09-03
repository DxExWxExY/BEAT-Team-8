from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit

from common.tab_layout import TabLayout


class ProjectTab(TabLayout):
    def __init__(self):
        # your constructor must make the following calls
        super().__init__("Project View", "Detailed Project View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        # Build layout for the left panel, and add widgets to it.
        # the class will add it to the parent layout for displaying
        layout = QVBoxLayout()

        search = QLineEdit()
        search.setPlaceholderText("Search Projects")
        search.returnPressed.connect(lambda: print("Enter Detected"))

        layout.addWidget(search)
        layout.addWidget(QPushButton('a'))
        layout.addWidget(QPushButton('a'))
        layout.addWidget(QPushButton('a'))
        return layout

    def rightPanelBuilder(self):
        # Build layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel('My Other Label'))
        layout.addWidget(QPushButton('a'))
        layout.addWidget(QPushButton('a'))
        layout.addWidget(QPushButton('a'))
        return layout