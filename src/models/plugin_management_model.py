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

    def addPlugin(self, path):
        item = self.__buildItem(path)
        self.__pluginList[item.name] = item

    def savePlugin(self, item, oldName):
        del self.__pluginList[oldName]
        self.__pluginList[item.name] = item
        self.__parser.updateEntry("plugin", item)

    def deletePlugin(self, i):
        self.__pluginList.pop(i)

    def __buildItem(self, path):
        # TODO: Parse from xml
        return PluginItem()

    def update(self):
        self.__pluginList = self.__parser.getEntries("plugin")
