from PyQt5.QtWidgets import QFileDialog

from src.items.project_item import ProjectItem
from src.models.project_model import ProjectModel
from src.views.tabs.project_tab import ProjectTab


class ProjectTabController:
    def __init__(self):
        self.tab = ProjectTab()
        self.model = ProjectModel()
        self.__addEventHandlers()
        self.__populateList()

    def __populateList(self):
        self.items = self.model.getProjectList()
        for item in self.items:
            self.tab.projectList.addItem(item.name)

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.addProjectButton.clicked.connect(lambda: self.__addProject())
        self.tab.projectList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.saveButton.clicked.connect(lambda: self.__saveProject())

    def __updateUI(self):
        selectedItem = self.__getSelectedItem()
        self.tab.projectName.setText(selectedItem[0].name)
        self.tab.projectDescription.setText(selectedItem[0].description)
        self.tab.binPath.setText(selectedItem[0].binaryPath)

    def __fileBrowser(self):
        callback = QFileDialog.getOpenFileName()
        if callback:
            self.tab.binPath.setText(str(callback[0]))

    def __searchForItem(self):
        print("Search triggered")

    def __getSelectedItem(self):
        i = self.tab.projectList.indexFromItem(self.tab.projectList.currentItem()).row()
        return self.items[i], i

    def __saveProject(self):
        selectedItem, i = self.__getSelectedItem()
        selectedItem.name = self.tab.projectName.text()
        selectedItem.description = self.tab.projectDescription.toPlainText()
        selectedItem.binaryPath = self.tab.binPath.text()
        # TODO: Get Current Objects from list OR register new instance in DB
        self.model.sendStateData([])

    def __deleteProject(self):
        self.items.remove(self.__getSelectedItem()[1])
        self.tab.projectList.takeItem(self.__getSelectedItem()[0].name)
        self.tab.projectList.update()

    def __addProject(self):
        # TODO: Move logic to model
        self.items.append(ProjectItem(len(self.items)))
        self.tab.projectList.addItem(self.items[-1].name)
