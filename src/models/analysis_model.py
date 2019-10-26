from src.analyzers.static_analyzer import StaticAnalyzer
from src.storage.xml_parser import XMLParser


class AnalysisModel:
    def __init__(self):
        self.parser = XMLParser()
        self.__staticAnalyzer = StaticAnalyzer()
        self.__poiList = dict()
        self.__message = ''


    def run_static(self, path):
        self.__staticAnalyzer.setPath(path)
        self.__poiList ["Function"] = self.__staticAnalyzer.R2findPOI("function")
        self.__poiList ["DLL"]= self.__staticAnalyzer.R2findPOI("dll")
        self.__poiList ["String"] = self.__staticAnalyzer.R2findPOI("strings")
        self.__message= "Static analysis complete."

    def getPoiList(self):
        return self.__poiList

    def getTerminalOutput(self):
        return self.__message

    def getPluginsList(self):
        return ["Select Plugin"] + self.parser.getEntries("plugin")

    def getFilterList(self, filter):
        if len(self.__poiList) is 0:
            return []

        if filter == "All":
            temp = []
            for key in self.__poiList.keys():
                temp += self.__poiList[key]
            return temp

        if filter not in "Variable Struct Packet Protocol":
            return self.__poiList[filter]
        else:
            return []



