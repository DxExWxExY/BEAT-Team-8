from src.items.plugin_item import PluginItem
from src.storage.xml_parser import XMLParser


class PluginManagementModel:
    def __init__(self):
        self.parser = XMLParser()
        self.__pluginList = self.parser.getEntries("plugin")
        print(self.__pluginList)

    def getPluginList(self):
        return self.__pluginList

    def getSelectedPlugin(self, key):
        return self.__pluginList[key]

    def addPlugin(self):
        self.__pluginList.append(PluginItem())

    def savePlugin(self, key, data):
        self.__pluginList[key] = data

    def deletePlugin(self, i):
        self.__pluginList.pop(i)
