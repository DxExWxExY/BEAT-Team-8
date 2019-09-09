from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtWidgets import *

from common.tab_layout import TabLayout


class ProjectTab(TabLayout):
    def __init__(self):
        # your constructor must make the following calls
        super().__init__("Project View", "Detailed Project View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        projectList = QListWidget()
        addProjectButton = QPushButton('New Project')

        projectList.addItem("Project 1")
        projectList.addItem("Project 2")
        projectList.addItem("Project 3")
        projectList.addItem("Project 4")

        layout.addLayout(self.searchBuilder())
        layout.addWidget(projectList)
        layout.addWidget(addProjectButton)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        projctName = QLineEdit()
        projctDescription = QTextEdit()
        binPath = QLineEdit()
        binProperties = QTextEdit()
        browsePath = QPushButton('Browse')
        spacer = QSpacerItem(100, 100, )

        layout.addWidget(QLabel("Project Name"), 0, 0)
        layout.addWidget(QLabel('Project Description'), 1, 0)
        layout.addWidget(QLabel('Binary File Path'), 3, 0)
        layout.addWidget(QLabel('Binary File Properties'), 4, 0)

        layout.addWidget(projctName, 0, 1)
        layout.addWidget(projctDescription, 1, 1, 2, 1)
        layout.addWidget(binPath, 3, 1)
        layout.addWidget(binProperties, 4, 1, 2, 1)

        layout.addWidget(browsePath, 3, 2)
        layout.addWidget(spacer)

        layout.setContentsMargins(100, 0, 100, 0)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Projects")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4 , 1, 2)

        return layout