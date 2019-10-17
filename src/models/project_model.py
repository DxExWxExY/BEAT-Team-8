from src.items.project_item import ProjectItem
from src.models.static_analyzer import StaticAnalyzer
from src.parsers.project_xml_parser import ProjectSchemaParser


class ProjectModel:
    def __init__(self):
        self.__parser = ProjectSchemaParser()
        self.__staticAnalyzer = StaticAnalyzer()
        self.__projectList = self.__parser.getItems()

    def getProjectList(self):
        return self.__projectList

    def getSelectedProject(self, i):
        return self.__projectList[i]

    def addProject(self):
        self.__projectList.append(ProjectItem())

    def deleteProject(self, i):
        self.__projectList.pop(i)

    def checkAttributes(self, i):
        if not self.__projectList[i].hasBinaryAttributes():
            self.__staticAnalyzer.setPath(self.__projectList[i].binaryPath)
            self.__projectList[i].binaryProperties = self.__staticAnalyzer.getBinaryProperties()
            self.__staticAnalyzer.close()

