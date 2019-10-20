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

    def addProject(self, path):
        item = ProjectItem(path=path)
        self.checkAttributes(item)
        self.__projectList.append(item)

    def deleteProject(self, i):
        self.__projectList.pop(i)

    def checkAttributes(self, item):
        if not item.hasBinaryAttributes():
            self.__staticAnalyzer.setPath(item.binaryPath)
            item.binaryProperties = self.__staticAnalyzer.getBinaryProperties()
            self.__staticAnalyzer.close()

    def saveProject(self, i):
        item = self.__projectList[i]
        self.__parser.updateEntry(item)