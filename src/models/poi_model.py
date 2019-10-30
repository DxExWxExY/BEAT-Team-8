from src.storage.xml_parser import XMLParser


class POIModel:
    def __init__(self):
        self.parser = XMLParser()
        self.__pluginList = self.parser.getEntries("plugin")

    def getPoiDefinitionsList(self):
        pass

    def getPluginPois(self, key):
        return self.__pluginList[key].pois

    def addPoiDefinition(self):
        pass

    def getPluginList(self):
        return self.__pluginList

    def __saveDefinitions(self):
        pass

    def getPluginFilters(self, key):
        return self.__pluginList[key].types