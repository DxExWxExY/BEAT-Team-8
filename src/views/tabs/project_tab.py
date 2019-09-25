from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QPushButton, QGridLayout, QLineEdit, QTextEdit, QLabel, \
    QTableWidget, QTableWidgetItem

from src.common.tab_layout import TabLayout


class ProjectTab(TabLayout):
    def __init__(self):
        super().__init__("Project View", "Detailed Project View")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.projectList = QListWidget()
        self.addProjectButton = QPushButton('New Project')

        layout.addLayout(self.searchBuilder())
        layout.addWidget(self.projectList)
        layout.addWidget(self.addProjectButton)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        self.projctName = QLineEdit()
        self.projctDescription = QTextEdit()
        self.binPath = QLineEdit()
        self.browsePath = QPushButton('Browse')
        self.deleteButton = QPushButton('Delete')
        self.saveButton = QPushButton('Save')

        layout.addWidget(QLabel("Project Name"), 0, 0)
        layout.addWidget(QLabel('Project Description'), 1, 0)
        layout.addWidget(QLabel('Binary File Path'), 3, 0)
        layout.addWidget(QLabel('Binary File Properties'), 4, 0)

        layout.addWidget(self.projctName, 0, 1)
        layout.addWidget(self.projctDescription, 1, 1, 2, 1)
        layout.addWidget(self.binPath, 3, 1)
        layout.addWidget(self.tableBuilder(), 4, 1)

        layout.addWidget(self.deleteButton, 5, 0)
        layout.addWidget(self.saveButton, 5, 2)
        layout.addWidget(self.browsePath, 3, 2)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Projects")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

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
