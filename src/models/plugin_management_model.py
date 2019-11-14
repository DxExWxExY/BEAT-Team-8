from src.items.plugin_item import PluginItem
from src.storage.entries_parser import EntriesParser


class PluginManagementModel:
    def __init__(self):
        self.__parser = EntriesParser()
        self.__pluginList = self.__parser.getEntries("plugin")

    def getPluginList(self):
        return self.__pluginList

    def getSelectedPlugin(self, key):
        return self.__pluginList[key]

    def savePlugin(self, item, oldName):
        del self.__pluginList[oldName]
        self.__pluginList[item.name] = item
        self.__parser.updateEntry("plugin", item)

    def deletePlugin(self, i):
        self.__parser.deleteEntry("plugin", self.__pluginList[i])
        del self.__pluginList[i]

    def update(self):
        self.__pluginList = self.__parser.getEntries("plugin")

    def createPlugin(self, path):
        if self.__parser.validatePluginSchema(path):
            self.__parser.getPluginFromXml(path)
            self.update()

    def getPoi(self, plugin, poiName):
        return self.__pluginList[plugin].pois[poiName]

    def addPoiDefinition(self, key, poi, data):
        self.__pluginList[key].pois[poi] = data
        self.__parser.updateEntry("plugin", self.__pluginList[key])
        self.update()

    def deletePoi(self, plugin, poiName):
        del self.__pluginList[plugin].pois[poiName]
        self.__parser.updateEntry("plugin", self.__pluginList[plugin])
        self.update()

    def updatePoiDefinition(self, plugin):
        self.__parser.updateEntry("plugin", self.__pluginList[plugin])