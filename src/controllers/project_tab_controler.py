from PyQt5.QtWidgets import QFileDialog

from src.items.project_item import ProjectItem
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
