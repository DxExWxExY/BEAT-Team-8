class PluginParser:
    def __init__(self):
        self.pluginList = self.__pluginsFromDB()

    def getFilterAndPlugin(self, plugin):
        if plugin == 'pa':
            return plugin()

    def __pluginsFromDB(self):
        # DB query as objs
        return []

    def __deserializer(self):
        return object()
