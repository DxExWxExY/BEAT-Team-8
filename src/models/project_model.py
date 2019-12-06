from src.items.project_item import ProjectItem
from src.analyzers.static_analyzer import StaticAnalyzer
from src.storage.entries_parser import EntriesParser


class ProjectModel:
    def __init__(self):
        self.__parser = EntriesParser()
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
        item = ProjectItem(path)
        self.__checkAttributes(item)
        return item

    def deleteProject(self, i):
        self.__parser.deleteEntry("project", self.__projectList[i])
        del self.__projectList[i]

    def saveProject(self, item):
        self.__parser.updateEntry("project", item)
        self.__projectList = self.__parser.getEntries("project")
        return self.__projectList[item.name]

    def __checkAttributes(self, item):
        self.__staticAnalyzer.setPath(item.binaryPath)
        item.binaryProperties = self.__staticAnalyzer.getBinaryProperties()
        self.__staticAnalyzer.close()

