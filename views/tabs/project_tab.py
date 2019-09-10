from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QPushButton, QGridLayout, QLineEdit, QTextEdit, QLabel, \
    QTableWidget, QTableWidgetItem
from common.tab_layout import TabLayout


class ProjectTab(TabLayout):
    def __init__(self):
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
        browsePath = QPushButton('Browse')
        deleteButton = QPushButton('Delete')
        saveButton = QPushButton('Save')

        layout.addWidget(QLabel("Project Name"), 0, 0)
        layout.addWidget(QLabel('Project Description'), 1, 0)
        layout.addWidget(QLabel('Binary File Path'), 3, 0)
        layout.addWidget(QLabel('Binary File Properties'), 4, 0)

        layout.addWidget(projctName, 0, 1)
        layout.addWidget(projctDescription, 1, 1, 2, 1)
        layout.addWidget(binPath, 3, 1)
        layout.addWidget(self.tableBuilder(), 4, 1)

        layout.addWidget(deleteButton, 5, 0)
        layout.addWidget(saveButton, 5, 2)
        layout.addWidget(browsePath, 3, 2)

        layout.setContentsMargins(100, 0, 100, 0)

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

    def tableBuilder(self):
        table = QTableWidget()
        table.setRowCount(13)
        table.setColumnCount(2)

        table.setItem(0, 0, QTableWidgetItem('OS'))
        table.setItem(1, 0, QTableWidgetItem('Binary Type'))
        table.setItem(2, 0, QTableWidgetItem('Machine'))
        table.setItem(3, 0, QTableWidgetItem('Class'))
        table.setItem(4, 0, QTableWidgetItem('Bits'))
        table.setItem(5, 0, QTableWidgetItem('Language'))
        table.setItem(6, 0, QTableWidgetItem('Canary'))
        table.setItem(7, 0, QTableWidgetItem('Crypto'))
        table.setItem(8, 0, QTableWidgetItem('Nx'))
        table.setItem(9, 0, QTableWidgetItem('Pic'))
        table.setItem(10, 0, QTableWidgetItem('Relocs'))
        table.setItem(11, 0, QTableWidgetItem('Relro'))
        table.setItem(12, 0, QTableWidgetItem('Stripped'))

        table.setHorizontalHeaderLabels(['Name', 'Value'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)

        return table
