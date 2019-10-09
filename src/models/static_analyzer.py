import r2pipe

class StaticAnalyzer:
    def __init__(self):
        pass

    def getBinaryProperties(self, path):
        properties = dict()
        # TODO: Process json into dictionary
        # if fail add key with the none value
        json = self.__executej("IIj")
        properties['os'] = json[0]['os']
        # repeat
        return properties

    def __execute(self, command):
        # Execute
        pass

    def __executej(self, command):
        # Execute
        return [] #Json data

    def getPois(self, plugin, type):
        json = self.__executej("")
        results = []
        filter = plugin.listFilter(type)
        for e in json:
            if e in filter:
                results.append(e)
        return results