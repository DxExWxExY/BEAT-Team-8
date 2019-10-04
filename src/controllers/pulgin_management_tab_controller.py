from PyQt5.QtWidgets import QFileDialog

from src.models.plugin_management_model import PluginManagementModel
from src.views.tabs.plugin_management_tab import PluginManagementTab


class PluginManagementTabController:
    def __init__(self):
        self.tab = PluginManagementTab()
        self.model = PluginManagementModel()
        self.__addEventHandlers()
        self.__populateProjectList()

    def __addEventHandlers(self):
        self.tab.addPlugin.clicked.connect(lambda: self.__addPlugin())
        self.tab.pluginList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPlugin())
        self.tab.browseStructurePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.browseDataPath.clicked.connect(lambda: self.__fileBrowser(isData=True))
        self.tab.deletePlugin.clicked.connect(lambda: self.__deletePlugin())
        self.tab.savePlugin.clicked.connect(lambda: self.__savePlugin())

    def __populateProjectList(self):
        for item in self.model.getPluginList():
            self.tab.pluginList.addItem(item.name)

    def __updateUI(self):
        self.tab.poiList.clear()
        selectedItem = self.model.getSelectedPlugin(self.__currentItem())
        self.tab.pluginStructurePath.setText(selectedItem.structurePath)
        self.tab.dataSetPath.setText(selectedItem.dataSetPath)
        self.tab.pluginName.setText(selectedItem.name)
        self.tab.pluginDescription.setText(selectedItem.description)
        self.tab.outputField.addItems(selectedItem.outputFields)
        self.tab.poiList.addItems(selectedItem.pois)

    def __savePlugin(self):
        current = self.model.getSelectedPlugin(self.__currentItem())
        current.name = self.tab.pluginName.text()
        current.description = self.tab.pluginDescription.toPlainText()
        current.structurePath = self.tab.pluginStructurePath.text()
        current.dataSetPath = self.tab.dataSetPath.text()
        self.tab.pluginList.clear()
        self.__populateProjectList()

    def __deletePlugin(self):
        self.model.deletePlugin(self.__currentItem())
        self.tab.pluginList.clear()
        self.__populateProjectList()

    def __currentItem(self):
        return self.tab.pluginList.indexFromItem(self.tab.pluginList.currentItem()).row()

    def __searchForPlugin(self):
        print("At least you entered something \\(\'\'/)/")

    def __addPlugin(self):
        self.model.addPlugin()
        self.tab.pluginList.clear()
        self.__populateProjectList()

    def __fileBrowser(self, isData=False):
        callback = QFileDialog.getOpenFileName()
        if callback:
            if isData:
                self.tab.dataSetPath.setText(str(callback[0]))
            else:
                self.tab.pluginStructurePath.setText(str(callback[0]))
