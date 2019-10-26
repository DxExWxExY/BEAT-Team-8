from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QPushButton, QGridLayout, QLineEdit, QTextEdit, QLabel, \
    QTableWidget, QTableWidgetItem

from src.common.tab_layout import TabLayout


class ProjectTab(TabLayout):
    def __init__(self):
        super().__init__("Project View", "Detailed Project View")
        super().addContentToLeftPanel(self.__leftPanelBuilder())
        super().addContentToRightPanel(self.__rightPanelBuilder())
        super().build()

    def __leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.projectList = QListWidget()
        self.addProjectButton = QPushButton('Add New Project')

        layout.addLayout(self.__searchBuilder())
        layout.addWidget(self.projectList)
        layout.addWidget(self.addProjectButton)

        return layout

    def __rightPanelBuilder(self):
        layout = QGridLayout()

        self.projectName = QLineEdit()
        self.projectDescription = QTextEdit()
        self.binPath = QLineEdit()
        self.browsePath = QPushButton('Browse')
        self.deleteButton = QPushButton('Delete')
        self.saveButton = QPushButton('Save')

        layout.addWidget(QLabel("Project Name"), 0, 0)
        layout.addWidget(QLabel('Project Description'), 1, 0)
        layout.addWidget(QLabel('Binary File Path'), 3, 0)
        layout.addWidget(QLabel('Binary File Properties'), 4, 0)

        layout.addWidget(self.projectName, 0, 1, 1, 9)
        layout.addWidget(self.projectDescription, 1, 1, 2, 9)
        layout.addWidget(self.binPath, 3, 1, 1, 8)
        layout.addWidget(self.__tableBuilder(), 4, 1, 1, 9)

        layout.addWidget(self.deleteButton, 5, 8)
        layout.addWidget(self.saveButton, 5, 9)
        layout.addWidget(self.browsePath, 3, 9)

        return layout

    def __searchBuilder(self):
        layout = QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Projects")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout

    def __tableBuilder(self):
        self.table = QTableWidget()
        self.table.setRowCount(13)
        self.table.setColumnCount(2)

        self.table.setItem(0, 0, QTableWidgetItem('OS'))
        self.table.setItem(1, 0, QTableWidgetItem('Binary Type'))
        self.table.setItem(2, 0, QTableWidgetItem('Machine'))
        self.table.setItem(3, 0, QTableWidgetItem('Class'))
        self.table.setItem(4, 0, QTableWidgetItem('Bits'))
        self.table.setItem(5, 0, QTableWidgetItem('Language'))
        self.table.setItem(6, 0, QTableWidgetItem('Canary'))
        self.table.setItem(7, 0, QTableWidgetItem('Crypto'))
        self.table.setItem(8, 0, QTableWidgetItem('Nx'))
        self.table.setItem(9, 0, QTableWidgetItem('Pic'))
        self.table.setItem(10, 0, QTableWidgetItem('Relocs'))
        self.table.setItem(11, 0, QTableWidgetItem('Relro'))
        self.table.setItem(12, 0, QTableWidgetItem('Stripped'))

        self.table.setHorizontalHeaderLabels(['Name', 'Value'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        return self.table

    def setProjectList(self, list):
        pass

    def setUIElementsText(self, item):
        pass
