from src.items.project_item import ProjectItem
from src.parsers.project_xml_parser import ProjectSchemaParser


class ProjectModel:
    def __init__(self):
        self.__parser = ProjectSchemaParser()

    def getProjectList(self):
        # TODO: Use parser
        return [ProjectItem(i) for i in range(5)]

    def sendStateData(self, data):
        pass

    def addNewProject(self):
        pass