import time
from threading import Lock, Thread

from fuzzywuzzy import process

from src.analyzers.dynamic_analyzer import DynamicAnalyzer
from src.analyzers.static_analyzer import StaticAnalyzer
from src.storage.entries_parser import EntriesParser


class AnalysisModel:
    def __init__(self):
        self.parser = EntriesParser()
        self.__staticAnalyzer = StaticAnalyzer()
        self.__dynamicAnalyzer = DynamicAnalyzer()
        self.__pluginList = self.parser.getEntries("plugin")
        self.__poiList = dict()
        self.__message = ''
        self.stopFlag = False
        self.uiLock = Lock()

    def run_static(self, project, plugin):
        self.__staticAnalyzer.setPath(project.binaryPath)
        self.__poiList["Function"] = self.__staticAnalyzer.findPois("function")
        self.__poiList["DLL"] = self.__staticAnalyzer.findPois("dll")
        self.__poiList["String"] = self.__staticAnalyzer.findPois("strings")
        self.__poiList["Variable"] = self.__staticAnalyzer.findPois("variable")
        project.results[plugin] = self.__poiList
        self.__staticAnalyzer.close()
        self.__lint(plugin)
        self.__message = "Static analysis complete."

    def getPoiList(self):
        return self.__poiList

    def getTerminalOutput(self):
        return self.__message

    def getPluginFilters(self, pluginName):
        return self.__pluginList[pluginName].types

    def getPluginsList(self):
        return ["Select Plugin"] + [key for key in self.__pluginList.keys()]

    def setFilterList(self, filter):
        if len(self.__poiList) is 0:
            return {}

        if filter == "All":
            temp = {}
            for key in self.__poiList.keys():
                temp.update(self.__poiList[key])
            return temp

        if filter not in "Struct Packet Protocol":
            return self.__poiList[filter]
        else:
            return {}

    def __lint(self, pluginName):
        plugin = self.__pluginList[pluginName]
        for key in self.__poiList.keys():
            lint = {}
            for ek in self.__poiList[key].keys():
                name = self.__poiList[key][ek]['name']
                if key == 'Variable':
                    lint[name] = self.__poiList[key][ek]
                    continue
                if process.extractOne(ek, list(plugin.pois.keys()))[1] > 80:
                    lint[name] = self.__poiList[key][ek]
            self.__poiList[key] = lint

    def update(self):
        self.__pluginList = self.parser.getEntries("plugin")

    def saveProject(self, project):
        self.parser.updateEntry("project", project)

    def findPoi(self, name):
        for key in self.__poiList.keys():
            if name in self.__poiList[key]:
                return self.__poiList[key][name]

    def setBreakpoints(self, path, pois, args):
        try:
            self.__dynamicAnalyzer.setPath(path, args)
            for poi in pois:
                self.__dynamicAnalyzer.setBreakpoint(poi['addr'])
        except Exception as err:
            print(err)

    def runDynamic(self, selectedPois):
        self.__message = "Dynamic Analysis Started."
        self.stopFlag = []
        Thread(target=self.__runDynamic, args=[selectedPois]).start()

    def __runDynamic(self, selectedPois):
        self.__dynamicAnalyzer.start(selectedPois, self.stopFlag)

        while not self.stopFlag:
            pass

        if self.stopFlag[0] == 2:
            self.__message = "Radare failed to initailize the binary emulation. This is sometimes caused by the arguments the program uses."
            self.__dynamicAnalyzer.close(force=True)
        else:
            self.__message = "Dynamic analysis complete."
            self.__dynamicAnalyzer.close()

    def killDynamic(self):
        self.stopFlag = [1]
        self.__dynamicAnalyzer.close(force=True)



