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

    def getSelectedProject(self, key):
        if len(self.__projectList) > 0:
            try:
                return self.__projectList[key]
            except KeyError:
                pass
        return None

    def verifyBinary(self, path):
        item = ProjectItem(path=path)
        self.__checkAttributes(item)
        return item


    def deleteProject(self, i):
        self.__parser.deleteEntry("project" ,self.__projectList[i])
        del self.__projectList[i]

    def saveProject(self, item):
        self.__projectList[item.name] = item
        self.__parser.updateEntry("project", item)

    def __checkAttributes(self, item):
        self.__staticAnalyzer.setPath(item.binaryPath)
        item.binaryProperties = self.__staticAnalyzer.getBinaryProperties()
        self.__staticAnalyzer.close()

    def addProject(self, param):
        pass
