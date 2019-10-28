from src.items.project_item import ProjectItem
from src.analyzers.static_analyzer import StaticAnalyzer
from src.storage.xml_parser import XMLParser


class ProjectModel:
    def __init__(self):
        self.__parser = XMLParser()
        self.__staticAnalyzer = StaticAnalyzer()
        self.__projectList = self.__parser.getEntries("project")

    def getProjectList(self):
        return self.__projectList

    def getSelectedProject(self, i):
        if len(self.__projectList) > 0:
            return self.__projectList[i % len(self.__projectList)]
        return None

    def addProject(self, path):
        item = ProjectItem(path=path)
        self.__checkAttributes(item)
        self.__projectList.append(item)

    def deleteProject(self, i):
        self.__parser.deleteEntry("project" ,self.__projectList.pop(i))

    def saveProject(self, i):
        item = self.__projectList[i]
        self.__parser.updateEntry("project", item)

    def __checkAttributes(self, item):
        self.__staticAnalyzer.setPath(item.binaryPath)
        item.binaryProperties = self.__staticAnalyzer.getBinaryProperties()
        self.__staticAnalyzer.close()
