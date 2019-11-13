from src.storage.entries_parser import EntriesParser


class POIModel:
    def __init__(self):
        self.parser = EntriesParser()
        self.__pluginList = self.parser.getEntries("plugin")

    def getPoiDefinitionsList(self):
        pass

    def getPluginPois(self, key):
        return self.__pluginList[key].pois

    def addPoiDefinition(self, key, poi):
        self.__pluginList[key].pois += [poi]
        self.parser.updateEntry("plugin", self.__pluginList[key])

    def getPluginList(self):
        return self.__pluginList

    def __saveDefinitions(self):
        pass

    def getPluginFilters(self, key):
        return self.__pluginList[key].types

    def update(self):
        self.__pluginList = self.parser.getEntries("plugin")