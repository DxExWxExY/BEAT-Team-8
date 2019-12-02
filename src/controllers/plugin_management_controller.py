from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from src.models.plugin_management_model import PluginManagementModel
from src.views.dialogs.add_poi_dialog import AddPoiDialog
from src.views.dialogs.plugin_management_dialog import PluginManagementDialog


class PluginManagementController:
    def __init__(self):
        self.dialog = PluginManagementDialog()
        self.model = PluginManagementModel()
        self.newPoiDialog = AddPoiDialog()
        self.__addEventHandlers()
        self.__populatePluginList()

    def __addEventHandlers(self):
        self.dialog.addPlugin.clicked.connect(lambda: self.__addPlugin())
        self.dialog.pluginList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.dialog.poiList.itemSelectionChanged.connect(lambda: self.__viewPoi())
        self.dialog.searchBox.returnPressed.connect(lambda: self.__searchForPlugin())
        self.dialog.searchButton.clicked.connect(lambda: self.__searchForPlugin())
        self.dialog.deletePlugin.clicked.connect(lambda: self.__deletePlugin())
        self.dialog.savePlugin.clicked.connect(lambda: self.__savePlugin())
        self.dialog.addPoi.clicked.connect(lambda: self.__addPoiToPlugin())
        self.newPoiDialog.saveNewPoi.clicked.connect(lambda: self.__saveNewPoi())
        self.newPoiDialog.cancelButton.clicked.connect(lambda: self.newPoiDialog.close())
        self.dialog.savePoi.clicked.connect(lambda: self.__updatePoi())
        self.dialog.deletePoi.clicked.connect(lambda: self.__deletePoiFromPlugin())

    def __populatePluginList(self):
        for key in self.model.getPluginList().keys():
            self.dialog.pluginList.addItem(key)

    def __updateUI(self):
        self.dialog.poiList.clear()
        self.dialog.outputField.clear()
        if self.dialog.pluginList.selectedItems():
            selectedItem = self.model.getSelectedPlugin(self.__currentPlugin())
            self.dialog.pluginName.setText(selectedItem.name)
            self.dialog.pluginDescription.setText(selectedItem.description)
            self.dialog.outputField.addItems(selectedItem.outputs)
            self.dialog.poiList.addItems(selectedItem.pois)

    def __savePlugin(self):
        selectedPlugin = self.model.getSelectedPlugin(self.__currentPlugin())
        if selectedPlugin is not None:
            oldName = selectedPlugin.name
            selectedPlugin.name = self.dialog.pluginName.text()
            selectedPlugin.description = self.dialog.pluginDescription.toPlainText()
            self.model.savePlugin(selectedPlugin, oldName)
            itemIndex = self.dialog.pluginList.findItems(oldName, QtCore.Qt.MatchExactly)
            i = self.dialog.pluginList.row(itemIndex[0])
            self.dialog.pluginList.takeItem(i)
            self.dialog.pluginList.clear()
            self.__populatePluginList()
            index = self.dialog.pluginList.count() - 1
            self.dialog.pluginList.setCurrentRow(index)
            self.__updateUI()

    def __deletePlugin(self):
        if not self.dialog.pluginList.selectedItems():
            return
        buttonReply = QMessageBox.question(self.dialog, 'Delete Plugin',
                                           "Are you sure you want to delete this plugin?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.model.deletePlugin(self.__currentPlugin())
            self.dialog.pluginList.clear()
            self.__populatePluginList()

    def __currentPlugin(self):
        return self.dialog.pluginList.currentItem().text()

    def __searchForPlugin(self):
        searchText = self.dialog.searchBox.text().lower()
        # When search is triggered with an empty string clear the list
        if searchText is "":
            self.dialog.pluginList.clear()
            self.__populatePluginList()
        else:
            # get all the items with substring of searched string
            searches = []
            for pluginName in self.model.getPluginList().keys():
                if searchText in pluginName.lower():
                    searches.append(pluginName)
            # add those items with substring into the list
            self.dialog.pluginList.clear()
            for s in searches:
                self.dialog.pluginList.addItem(s)

    def __addPlugin(self):
        path, response = QFileDialog.getOpenFileName(self.dialog, 'Select Plugin XML', filter='XML files (*.xml)')
        try:
            if response:
                self.model.createPlugin(path)
                self.dialog.pluginList.clear()
                self.__populatePluginList()
            self.dialog.pluginList.setCurrentRow(self.dialog.pluginList.count() - 1)
        except KeyError:
            pass

    def __viewPoi(self):
        if not self.dialog.poiList.selectedItems():
            return
        else:
            self.dialog.poiName.clear()
            self.dialog.poiType.clear()
            self.dialog.poiMapping.clear()
            selectedPoiName = self.dialog.poiList.currentItem().text()
            selectedPlugin = self.__currentPlugin()
            selectedPoi = self.model.getPoi(selectedPlugin, selectedPoiName)
            types = self.model.getSelectedPlugin(selectedPlugin).types
            self.dialog.poiName.setText(selectedPoi['name'])
            self.dialog.poiType.addItems(types[1:])
            self.dialog.poiMapping.setText(selectedPoi['map'])
            self.dialog.poiType.setCurrentIndex(types.index(selectedPoi['type']))

    def __saveNewPoi(self):
        plugin = self.dialog.pluginList.currentItem().text()
        poi = {}
        poi['name'] = self.newPoiDialog.newPoiName.text()
        poi['type'] = self.newPoiDialog.newPoiType.currentText()
        poi['map'] = self.newPoiDialog.newPoiMapping.text()
        self.model.addPoiDefinition(plugin, poi['name'], poi)
        self.__populatePoiList()
        self.newPoiDialog.close()

    def __updatePoi(self):
        plugin = self.dialog.pluginList.currentItem().text()
        poi = self.dialog.poiList.currentItem().text()
        selected = self.model.getPoi(plugin, poi)
        selected['name'] = self.dialog.poiName.text()
        selected['type'] = self.dialog.poiType.currentText()
        selected['map'] = self.dialog.poiMapping.text()
        self.model.updatePoiDefinition(plugin)

    def __addPoiToPlugin(self):
        if self.dialog.pluginList.selectedItems():
            self.newPoiDialog.newPoiType.clear()
            self.newPoiDialog.newPoiName.clear()
            self.newPoiDialog.newPoiMapping.clear()
            selectedPlugin = self.__currentPlugin()
            types = self.model.getSelectedPlugin(selectedPlugin).types
            self.newPoiDialog.newPoiType.addItems(types[1:])
            self.newPoiDialog.show()

    def __deletePoiFromPlugin(self):
        if self.dialog.pluginList.selectedItems() and self.dialog.poiList.selectedItems():
            selectedPoi = self.dialog.poiList.currentItem().text()
            selectedPlugin = self.dialog.pluginList.currentItem().text()
            self.model.deletePoi(selectedPlugin, selectedPoi)
            self.__populatePoiList()

    def __populatePoiList(self):
        self.dialog.poiList.clear()
        plugin = self.dialog.pluginList.currentItem().text()
        for poi in self.model.getSelectedPlugin(plugin).pois.keys():
            self.dialog.poiList.addItem(poi)

    def update(self):
        self.model.update()
