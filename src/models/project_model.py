from src.items.project_item import ProjectItem
from src.parsers.project_xml_parser import ProjectSchemaParser


class ProjectModel:
    def __init__(self):
        # TODO: Use parser
        self.__parser = ProjectSchemaParser()
        self.__projectList = [ProjectItem(i) for i in range(5)]

    def getProjectList(self):
        return self.__projectList

    def getSelectedProject(self, i):
        return self.__projectList[i]

    def addProject(self):
        self.__projectList.append(ProjectItem(len(self.__projectList)))

    def deleteProject(self, i):
        self.__projectList.pop(i)