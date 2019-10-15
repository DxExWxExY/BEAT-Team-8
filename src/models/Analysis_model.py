import time

from src.items.project_item import ProjectItem
from src.models.static_analyzer import StaticAnalyzer
from src.parsers.project_xml_parser import ProjectSchemaParser


class AnalysisModel:
    def __init__(self):
        # TODO: Use parser
        self.__staticAnalyzer = StaticAnalyzer()
        self.__POISlist = dict()
        self.__message = ''


    def run_static(self):
        # time.sleep(5)
        self.__staticAnalyzer.setPath("res/ex.o")
        self.__POISlist ["Function"] = self.__staticAnalyzer.R2findPOI("function")
        self.__POISlist ["DLL"]= self.__staticAnalyzer.R2findPOI("dll")
        self.__POISlist ["String"] = self.__staticAnalyzer.R2findPOI("strings")
        print(self.__POISlist,"-----")
        self.__message= "Static analysis complete."

    def getPoiList(self):
        return self.__POISlist

    def getTerminalOutput(self):
        return self.__message

    def getFilterList(self, filter):
        if filter == "All":
            temp = []
            for key in self.__POISlist.keys():
                temp += self.__POISlist[key]
            return temp

        if filter not in "Variable Struct Packet Protocol":
            return self.__POISlist[filter]
        else:
            return []



