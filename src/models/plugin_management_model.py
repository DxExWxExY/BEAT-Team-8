from src.items.plugin_item import PluginItem


class PluginManagementModel:
    def __init__(self):
        # TODO: Add plugin parser instance
        pass

    def getPoiList(self):
        return ["PoI a", "PoI b", "PoI c"]

    def getPluginList(self):
        return [PluginItem(i) for i in range(5)]

    def getOutputFieldItems(self):
        return ["Python File", "Other"]