from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from src.models.project_model import ProjectModel
from src.views.tabs.project_tab import ProjectTab


class ProjectTabController:
    def __init__(self):
        self.tab = ProjectTab()
        self.model = ProjectModel()
        self.__addEventHandlers()
        self.__populateProjectList()

    def __populateProjectList(self):
        for item in self.model.getProjectList():
            self.tab.projectList.addItem(item.name)

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.addProjectButton.clicked.connect(lambda: self.__addProject())
        self.tab.projectList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.saveButton.clicked.connect(lambda: self.__saveProject())
        self.tab.deleteButton.clicked.connect(lambda: self.__deleteProject())

    def __updateUI(self):
        selectedItem = self.model.getSelectedProject(self.__getCurrentItem())
        self.tab.projectName.setText(selectedItem.name)
        self.tab.projectDescription.setText(selectedItem.description)
        self.tab.binPath.setText(selectedItem.binaryPath)
        self.tab.table.setItem(0, 1, QTableWidgetItem(selectedItem.binaryProperties['os']))
        self.tab.table.setItem(1, 1, QTableWidgetItem(selectedItem.binaryProperties['arch']))
        self.tab.table.setItem(2, 1, QTableWidgetItem(selectedItem.binaryProperties['']))
        self.tab.table.setItem(3, 1, QTableWidgetItem("Win PE"))
        self.tab.table.setItem(4, 1, QTableWidgetItem(selectedItem.binaryProperties['bits']))
        self.tab.table.setItem(5, 1, QTableWidgetItem("Language"))
        self.tab.table.setItem(6, 1, QTableWidgetItem(selectedItem.binaryProperties['canary']))
        self.tab.table.setItem(7, 1, QTableWidgetItem(selectedItem.binaryProperties['crypto']))
        self.tab.table.setItem(8, 1, QTableWidgetItem(selectedItem.binaryProperties['nx']))
        self.tab.table.setItem(9, 1, QTableWidgetItem(selectedItem.binaryProperties['pic']))
        self.tab.table.setItem(10, 1, QTableWidgetItem(selectedItem.binaryProperties['relocs']))
        self.tab.table.setItem(11, 1, QTableWidgetItem("Relor"))
        self.tab.table.setItem(12, 1, QTableWidgetItem(selectedItem.binaryProperties['stripped']))

    def __fileBrowser(self):
        callback = QFileDialog.getOpenFileName()
        if callback:
            self.tab.binPath.setText(str(callback[0]))

    def __searchForItem(self):
        print("Search triggered")

    def __getCurrentItem(self):
        i = self.tab.projectList.indexFromItem(self.tab.projectList.currentItem()).row()
        return i

    def __saveProject(self):
        selectedItem = self.model.getSelectedProject(self.__getCurrentItem())
        selectedItem.name = self.tab.projectName.text()
        selectedItem.description = self.tab.projectDescription.toPlainText()
        selectedItem.binaryPath = self.tab.binPath.text()
        
        self.tab.projectList.clear()
        self.__populateProjectList()

    def __deleteProject(self):
        self.model.deleteProject(self.__getCurrentItem())
        self.tab.projectList.clear()
        self.__populateProjectList()

    def __addProject(self):
        self.model.addProject()
        self.tab.projectList.clear()
        self.__populateProjectList()
