from src.items.plugin_item import PluginItem


class PluginManagementModel:
    def __init__(self):
        # TODO: Add plugin parser instance
        self.__poiList = ["PoI a", "PoI b", "PoI c"]
        self.__pluginList = [PluginItem(i) for i in range(5)]
        self.__outputFields = ["Python File", "Other"]
        pass

    def getPoiList(self):
        return self.__poiList

    def getPluginList(self):
        return self.__pluginList

    def getOutputFieldItems(self):
        return self.__outputFields

    def getSelectedPlugin(self, i):
        return self.__pluginList[i]

    def addPlugin(self):
        self.__pluginList.append(PluginItem(len(self.__pluginList)))

    def savePlugin(self, i, data):
        # TODO: serialize all objects in lists with parser
        self.__pluginList[i] = data
        pass

    def deletePlugin(self, i):
        self.__pluginList.pop(i)
