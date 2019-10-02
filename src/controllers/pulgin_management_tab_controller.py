from PyQt5.QtWidgets import QFileDialog

from src.items.plugin_item import PluginItem
from src.models.plugin_management_model import PluginManagementModel
from src.views.tabs.plugin_management_tab import PluginManagementTab


class PluginManagementTabController:
    def __init__(self):
        self.tab = PluginManagementTab()
        self.model = PluginManagementModel()
        self.__addEventHandlers()
        self.__populateLists()
        self.__populateDropdowns()

    def __addEventHandlers(self):
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPlugin())
        self.tab.browseStructurePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.browseDataPath.clicked.connect(lambda: self.__fileBrowser(isData=True))
        self.tab.deletePlugin.clicked.connect(lambda: self.__deletePlugin())
        self.tab.savePlugin.clicked.connect(lambda: self.__savePlugin())

    def __populateLists(self):
        self.items = self.model.getPluginList()
        for item in self.items:
            self.tab.pluginList.addItem(item.name)
        self.tab.poiList.addItems(self.model.getPoiList())

    def __populateDropdowns(self):
        self.tab.outputField.addItems(self.model.getOutputFieldItems())

    def __savePlugin(self):
        pass

    def __deletePlugin(self):
        pass

    def __searchForPlugin(self):
        print("At least you entered something \\(\'\'/)/")

    def __addProject(self):
        # TODO: Move logic to model
        self.items.append(PluginItem(len(self.items)))
        self.tab.projectList.addItem(self.items[-1].name)

    def __fileBrowser(self, isData=False):
        callback = QFileDialog.getOpenFileName()
        if callback:
            if isData:
                self.tab.dataSetPath.setText(str(callback[0]))
            else:
                self.tab.pluginStructurePath.setText(str(callback[0]))
