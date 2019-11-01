from PyQt5.QtWidgets import QInputDialog, QLineEdit

from src.models.poi_model import POIModel
from src.views.tabs.points_of_intersets_tab import PointsOfInterestTab


# noinspection PyCallByClass
class POITabController:
    def __init__(self):
        self.tab = PointsOfInterestTab()
        self.model = POIModel()
        self.__addEventHandlers()
        self.__populateDropdowns()

    def __addEventHandlers(self):
        self.tab.existingPluginsDropdown.currentIndexChanged.connect(lambda: self.__selectPlugin())
        self.tab.typeDropdown.currentIndexChanged.connect(lambda: self.__selectType())
        self.tab.addPoiButton.clicked.connect(lambda: self.__addPoiToPlugin())

    def __populateDropdowns(self):
        items = ["Select Plugin"] + [key for key in self.model.getPluginList().keys()]
        self.tab.existingPluginsDropdown.addItems(items)

    def __searchPoi(self):
        pass

    def __populateList(self):
        selected = self.tab.existingPluginsDropdown.currentText()
        self.tab.poiList.clear()
        self.tab.poiList.addItems(self.model.getPluginPois(selected))

    def __selectPlugin(self):
        selected = self.tab.existingPluginsDropdown.currentText()
        if selected in "Select Plugin":
            self.tab.typeDropdown.clear()
            self.tab.poiList.clear()
            self.tab.typeDropdown.setEnabled(False)
            self.tab.addPoiButton.setEnabled(False)
            self.tab.content.clear()
        else:
            self.tab.addPoiButton.setEnabled(True)
            self.tab.typeDropdown.setEnabled(True)
            self.tab.poiList.clear()
            self.tab.typeDropdown.clear()
            self.tab.typeDropdown.addItems(self.model.getPluginFilters(selected))
            self.tab.poiList.addItems(self.model.getPluginPois(selected))

    def __selectType(self):
        # TODO: filter by type
        pass

    def __addPoiToPlugin(self):
        text, okPressed = QInputDialog.getText(self.tab, "New PoI", "New Point of Interest", QLineEdit.Normal)
        if okPressed and text != '':
            which = self.tab.existingPluginsDropdown.currentText()
            self.model.addPoiDefinition(which, text)
            self.__populateList()

    def update(self):
        self.model.update()
