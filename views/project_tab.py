from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit, QListView, QListWidget, QGridLayout

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



        projectList = QListWidget()
        projectList.addItem("Project 1")
        projectList.addItem("Project 2")
        projectList.addItem("Project 3")
        projectList.addItem("Project 4")

        layout.addLayout(self.searchBuilder())
        layout.addWidget(projectList)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        projctName = QLineEdit()
        projctDescription = QLineEdit()
        binPath = QLineEdit()
        binProperties = QLineEdit()

        browsePath = QPushButton('Browse')

        layout.addWidget(QLabel("Project Name"), 0, 0, 1, 1)
        layout.addWidget(QLabel('Project Description'), 1, 0, 1, 1)
        layout.addWidget(QLabel('Binary File Path'), 2, 0, 1, 1)
        layout.addWidget(QLabel('Binary File Properties'), 3, 0, 1, 1)

        layout.addWidget(projctName, 0, 1)
        layout.addWidget(projctDescription, 1, 1, 1)
        layout.addWidget(binPath, 5, 1, 1, 2)
        layout.addWidget(binProperties, 3, 1)

        layout.addWidget(browsePath, 6, 3, 1, 2)

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