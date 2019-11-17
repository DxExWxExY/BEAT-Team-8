from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTableWidgetItem

from src.common.constants import BUTTON_STYLE
from src.views.dialogs.project_details_dialog import ProjectDetails


class ProjectWidget(QWidget):
    def __init__(self, project):
        super().__init__()

        self.project = project

        layout = QGridLayout()

        self.name = QLabel()
        self.info = QPushButton("Details")

        self.info.setStyleSheet(BUTTON_STYLE)
        
        self.info.clicked.connect(lambda: self.__showDetails())

        layout.addWidget(self.name, 0, 0)
        layout.addWidget(self.info, 0, 1)

        self.setLayout(layout)

    def __showDetails(self):
        self.details = ProjectDetails(self.project.name)
        self.details.table.setItem(0, 1, QTableWidgetItem(self.project.binaryProperties['os']))
        self.details.table.setItem(1, 1, QTableWidgetItem(self.project.binaryProperties['arch']))
        self.details.table.setItem(2, 1, QTableWidgetItem(self.project.binaryProperties['machine']))
        self.details.table.setItem(3, 1, QTableWidgetItem(self.project.binaryProperties['class']))
        self.details.table.setItem(4, 1, QTableWidgetItem(self.project.binaryProperties['bits']))
        self.details.table.setItem(5, 1, QTableWidgetItem(self.project.binaryProperties['lang']))
        self.details.table.setItem(6, 1, QTableWidgetItem(self.project.binaryProperties['canary']))
        self.details.table.setItem(7, 1, QTableWidgetItem(self.project.binaryProperties['crypto']))
        self.details.table.setItem(8, 1, QTableWidgetItem(self.project.binaryProperties['nx']))
        self.details.table.setItem(9, 1, QTableWidgetItem(self.project.binaryProperties['pic']))
        self.details.table.setItem(10, 1, QTableWidgetItem(self.project.binaryProperties['relocs']))
        self.details.table.setItem(11, 1, QTableWidgetItem(self.project.binaryProperties['relro']))
        self.details.table.setItem(12, 1, QTableWidgetItem(self.project.binaryProperties['stripped']))
        self.details.exec()