from src.items.plugin_item import PluginItem
from src.storage.xml_parser import XMLParser


class PluginManagementModel:
    def __init__(self):
        self.parser = XMLParser()
        self.__pluginList = self.parser.getEntries("plugin")

    def getPluginList(self):
        return self.__pluginList

    def getSelectedPlugin(self, i):
        return self.__pluginList[i]

    def addPlugin(self):
        self.__pluginList.append(PluginItem())

    def savePlugin(self, i, data):
        # TODO: serialize all objects in lists with parser
        self.__pluginList[i] = data
        pass

    def deletePlugin(self, i):
        self.__pluginList.pop(i)
