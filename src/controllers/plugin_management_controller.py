from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QLineEdit

from src.models.plugin_management_model import PluginManagementModel
from src.views.dialogs.add_poi_dialog import AddPoiDialog
from src.views.tabs.plugin_management_tab import PluginManagementTab


class PluginManagementTabController:
    def __init__(self):
        self.tab = PluginManagementTab()
        self.model = PluginManagementModel()
        self.newPoiDialog = AddPoiDialog()
        self.__addEventHandlers()
        self.__populatePluginList()

    def __addEventHandlers(self):
        self.tab.addPlugin.clicked.connect(lambda: self.__addPlugin())
        self.tab.pluginList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.poiList.itemSelectionChanged.connect(lambda: self.__viewPoi())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPlugin())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForPlugin())
        self.tab.deletePlugin.clicked.connect(lambda: self.__deletePlugin())
        self.tab.savePlugin.clicked.connect(lambda: self.__savePlugin())
        self.tab.addPoi.clicked.connect(lambda: self.__addPoiToPlugin())
        self.newPoiDialog.saveNewPoi.clicked.connect(lambda: self.__saveNewPoi())
        self.newPoiDialog.cancelButton.clicked.connect(lambda: self.newPoiDialog.close())
        self.tab.savePoi.clicked.connect(lambda: self.__updatePoi())
        self.tab.deletePoi.clicked.connect(lambda: self.__deletePoiFromPlugin())

    def __populatePluginList(self):
        for key in self.model.getPluginList().keys():
            self.tab.pluginList.addItem(key)

    def __updateUI(self):
        self.tab.poiList.clear()
        self.tab.outputField.clear()
        if self.tab.pluginList.selectedItems():
            selectedItem = self.model.getSelectedPlugin(self.__currentPlugin())
            self.tab.pluginName.setText(selectedItem.name)
            self.tab.pluginDescription.setText(selectedItem.description)
            self.tab.outputField.addItems(selectedItem.outputs)
            self.tab.poiList.addItems(selectedItem.pois)

    def __savePlugin(self):
        selectedPlugin = self.model.getSelectedPlugin(self.__currentPlugin())
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
        if not self.tab.pluginList.selectedItems():
            return
        buttonReply = QMessageBox.question(self.tab, 'Delete Plugin',
                                           "Are you sure you want to delete this plugin?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.model.deletePlugin(self.__currentPlugin())
            self.tab.pluginList.clear()
            self.__populatePluginList()

    def __currentPlugin(self):
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
        path, response = QFileDialog.getOpenFileName(self.tab, 'Select Plugin XML', filter='XML files (*.xml)')
        try:
            if response:
                self.model.createPlugin(path)
                self.tab.pluginList.clear()
                self.__populatePluginList()
            self.tab.pluginList.setCurrentRow(self.tab.pluginList.count() - 1)
        except KeyError:
            pass

    def update(self):
        self.model.update()

    def __viewPoi(self):
        if not self.tab.poiList.selectedItems():
            return
        else:
            self.tab.poiName.clear()
            self.tab.poiType.clear()
            self.tab.poiMapping.clear()
            selectedPoiName = self.tab.poiList.currentItem().text()
            selectedPlugin = self.__currentPlugin()
            selectedPoi = self.model.getPoi(selectedPlugin, selectedPoiName)
            types = self.model.getSelectedPlugin(selectedPlugin).types
            self.tab.poiName.setText(selectedPoi['name'])
            self.tab.poiType.addItems(types[1:])
            self.tab.poiMapping.setText(selectedPoi['map'])
            self.tab.poiType.setCurrentIndex(types.index(selectedPoi['type']))

    def __saveNewPoi(self):
        plugin = self.tab.pluginList.currentItem().text()
        poi = {}
        poi['name'] = self.newPoiDialog.newPoiName.text()
        poi['type'] = self.newPoiDialog.newPoiType.currentText()
        poi['map'] = self.newPoiDialog.newPoiMapping.text()
        self.model.addPoiDefinition(plugin, poi['name'], poi)
        self.__populatePoiList()
        self.newPoiDialog.close()

    def __updatePoi(self):
        plugin = self.tab.pluginList.currentItem().text()
        poi = self.tab.poiList.currentItem().text()
        selected = self.model.getPoi(plugin, poi)
        selected['name'] = self.tab.poiName.text()
        selected['type'] = self.tab.poiType.currentText()
        selected['map'] = self.tab.poiMapping.text()
        self.model.updatePoiDefinition(plugin)

    def __addPoiToPlugin(self):
        if self.tab.pluginList.selectedItems():
            self.newPoiDialog.newPoiType.clear()
            self.newPoiDialog.newPoiName.clear()
            self.newPoiDialog.newPoiMapping.clear()
            selectedPlugin = self.__currentPlugin()
            types = self.model.getSelectedPlugin(selectedPlugin).types
            self.newPoiDialog.newPoiType.addItems(types[1:])
            self.newPoiDialog.show()

    def __deletePoiFromPlugin(self):
        if self.tab.pluginList.selectedItems() and self.tab.poiList.selectedItems():
            selectedPoi = self.tab.poiList.currentItem().text()
            selectedPlugin = self.tab.pluginList.currentItem().text()
            self.model.deletePoi(selectedPlugin, selectedPoi)
            self.__populatePoiList()

    def __populatePoiList(self):
        self.tab.poiList.clear()
        plugin = self.tab.pluginList.currentItem().text()
        for poi in self.model.getSelectedPlugin(plugin).pois.keys():
            self.tab.poiList.addItem(poi)
