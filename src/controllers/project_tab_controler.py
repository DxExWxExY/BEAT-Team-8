from PyQt5.QtWidgets import QFileDialog

from src.models.project_item import ProjectItem
from src.models.project_xml_parser import ProjectSchemaParser
from src.views.tabs.project_tab import ProjectTab


class ProjectTabController:
    def __init__(self):
        self.tab = ProjectTab()
        # self.model = ProjectModel()
        self.__parser = ProjectSchemaParser()
        self.__addEventHandlers()
        self.__populateList()

    def __populateList(self):
        # TODO: Move this logic to model
        self.items = self.__parser.getItems()
        for item in self.items:
            self.tab.projectList.addItem(item.name)
        pass

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.addProjectButton.clicked.connect(lambda: self.__addProject())
        self.tab.projectList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.saveButton.clicked.connect(lambda: self.__saveProject())

    def __updateUI(self):
        self.tab.projectList.update()
        selectedItem = self.__getSelectedItem()
        self.tab.projectName.setText(selectedItem.name)
        self.tab.projectDescription.setText(selectedItem.description)
        self.tab.binPath.setText(selectedItem.binaryPath)

    def __fileBrowser(self):
        callback = QFileDialog.getOpenFileName()
        if callback:
            self.tab.binPath.setText(str(callback[0]))

    def __searchForItem(self):
        print("Search triggered")
        pass

    def __getSelectedItem(self):
        i = self.tab.projectList.indexFromItem(self.tab.projectList.currentItem()).row()
        return self.items[i]

    def __saveProject(self):
        selectedItem = self.__getSelectedItem()
        selectedItem.name = self.tab.projectName.text()
        selectedItem.description = self.tab.projectDescription.toPlainText()
        selectedItem.binaryPath = self.tab.binPath.text()
        self.tab.projectList.repaint()


    def __addProject(self):
        # TODO: Move logic to model
        self.items.append(ProjectItem(0))
        self.tab.projectList.addItem(self.items[-1].name)
        pass