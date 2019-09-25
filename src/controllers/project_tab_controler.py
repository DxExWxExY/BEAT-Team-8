from PyQt5.QtWidgets import QFileDialog

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
        # TODO: Retrieve object from parser
        self.items = self.__parser.getItems()
        for item in self.items:
            self.tab.projectList.addItem(item.name)
        pass

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser(self.tab.binPath))
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.addProjectButton.clicked.connect(lambda: self.__addProject())
        self.tab.projectList.itemSelectionChanged.connect(lambda: self.__updateUI())

    def __updateUI(self):
        i = self.tab.projectList.indexFromItem(self.tab.projectList.currentItem()).row()
        self.tab.projectName.setText(self.items[i].name)
        self.tab.projectDescription.setText(self.items[i].description)

    def __fileBrowser(self, textBox):
        callback = QFileDialog.getOpenFileName()
        if callback:
            textBox.setText(str(callback[0]))

    def __searchForItem(self):
        print("Search triggered")
        pass

    def __addProject(self):
        print("add pressed")
        pass