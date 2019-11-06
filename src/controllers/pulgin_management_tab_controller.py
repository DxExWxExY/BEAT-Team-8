from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit

from src.models.plugin_management_model import PluginManagementModel
from src.views.dialogs.edit_poi_dialog import EditPoiDialog
from src.views.tabs.plugin_management_tab import PluginManagementTab


class PluginManagementTabController:
    def __init__(self):
        self.tab = PluginManagementTab()
        self.model = PluginManagementModel()
        self.editPoiDialog = EditPoiDialog()
        self.__addEventHandlers()
        self.__populatePluginList()

    def __addEventHandlers(self):
        self.tab.addPlugin.clicked.connect(lambda: self.__addPlugin())
        self.tab.pluginList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPlugin())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForPlugin())
        self.tab.deletePlugin.clicked.connect(lambda: self.__deletePlugin())
        self.tab.savePlugin.clicked.connect(lambda: self.__savePlugin())
        self.tab.editPoi.clicked.connect(lambda: self.__editPoiDialog())
        self.editPoiDialog.addPoiButton.clicked.connect(lambda: self.__addPoiToPlugin())

    def __populatePluginList(self):
        for key in self.model.getPluginList().keys():
            self.tab.pluginList.addItem(key)

    def __updateUI(self):
        self.tab.poiList.clear()
        selectedItem = self.model.getSelectedPlugin(self.__currentItem())
        self.tab.pluginName.setText(selectedItem.name)
        self.tab.pluginDescription.setText(selectedItem.description)
        self.tab.outputField.addItems(selectedItem.outputFields)
        self.tab.poiList.addItems(selectedItem.pois)

    def __savePlugin(self):
        selectedPlugin = self.model.getSelectedPlugin(self.__currentItem())
        if selectedPlugin is not None:
            oldName = selectedPlugin.name
            selectedPlugin.name = self.tab.pluginName.text()
            selectedPlugin.description = self.tab.pluginDescription.toPlainText()
            self.model.savePlugin(selectedPlugin, oldName)
            itemIndex = self.tab.pluginList.findItems(oldName, QtCore.Qt.MatchExactly)
            i = self.tab.pluginList.row(itemIndex[0])
            self.tab.pluginList.takeItem(i)
            self.tab.pluginList.clear()
            self.__populatePluginList()
            index = self.tab.pluginList.count() -1
            self.tab.pluginList.setCurrentRow(index)
            self.__updateUI()

    def __deletePlugin(self):
        self.model.deletePlugin(self.__currentItem())
        self.tab.pluginList.clear()
        self.__populatePluginList()

    def __currentItem(self):
        return self.tab.pluginList.currentItem().text()

    def __searchForPlugin(self):
        searchText = self.tab.searchBox.text().lower()
        # When search is triggered with an empty string clear the list
        if searchText is "":
            self.tab.pluginList.clear()
            self.__populatePluginList()
        else:
            # get all the items with substring of searched string
            searches = []
            for pluginName in self.model.getPluginList().keys():
                if searchText in pluginName.lower():
                    searches.append(pluginName)
            # add those items with substring into the list
            self.tab.pluginList.clear()
            for s in searches:
                self.tab.pluginList.addItem(s)

    def __addPlugin(self):
        callback = QFileDialog.getOpenFileName()
        try:
            if callback:
                self.model.addPlugin(str(callback[0]))
                self.tab.pluginList.clear()
                self.__populatePluginList()
            self.tab.pluginList.setCurrentRow(self.tab.pluginList.count() - 1)
        except KeyError:
            # TODO: raise exception for file not being xml
            pass

    def __editPoiDialog(self):
        self.editPoiDialog.show()

    def __addPoiToPlugin(self):
        text, okPressed = QInputDialog.getText(self.tab, "New PoI", "New Point of Interest", QLineEdit.Normal)
        if okPressed and text != '':
            # which = self.tab.existingPluginsDropdown.currentText()
            # self.model.addPoiDefinition(which, text)
            # self.__populateList()
            pass

    def update(self):
        self.model.update()
