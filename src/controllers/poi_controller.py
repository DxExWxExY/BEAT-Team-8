from src.models.poi_model import POIModel
from src.views.tabs.points_of_intersets_tab import PointsOfInterestTab


class POITabController:
    def __init__(self):
        self.tab = PointsOfInterestTab()
        self.model = POIModel()
        self.__addEventHandlers()
        self.__populateDropdowns()

    def __addEventHandlers(self):
        self.tab.existingPluginsDropdown.currentIndexChanged.connect(lambda: self.__selectPlugin())
        self.tab.typeDropdown.currentIndexChanged.connect(lambda: self.__selectType())

    def __populateDropdowns(self):
        items = ["Select Plugin"] + [key for key in self.model.getPluginList().keys()]
        self.tab.existingPluginsDropdown.addItems(items)

    def __searchPoi(self):
        pass

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