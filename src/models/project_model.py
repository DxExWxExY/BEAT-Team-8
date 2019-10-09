from src.items.project_item import ProjectItem
from src.models.static_analyzer import StaticAnalyzer
from src.parsers.project_xml_parser import ProjectSchemaParser


class ProjectModel:
    def __init__(self):
        # TODO: Use parser
        self.__parser = ProjectSchemaParser()
        self.__staticAnalyzer = StaticAnalyzer()
        self.__projectList = [ProjectItem(i) for i in range(5)]
        self.__checkAttributes()

    def getProjectList(self):
        return self.__projectList

    def getSelectedProject(self, i):
        return self.__projectList[i]

    def addProject(self):
        self.__projectList.append(ProjectItem(len(self.__projectList)))

    def deleteProject(self, i):
        self.__projectList.pop(i)

    # def runStatic(self, pluginName, filterType):
    #     plugin = self.__parser.getPlugin(pluginName)
    #     return self.__staticAnalyzer.getPois(pluginName, filterType)

    def __checkAttributes(self):
        for e in self.__projectList:
            if not e.hasBinaryAttributes():
                self.__staticAnalyzer.setPath(e.binaryPath)
                e.binaryProperties = self.__staticAnalyzer.getBinaryProperties()