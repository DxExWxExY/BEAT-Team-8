import os

from xmlschema import XMLSchema
from lxml import etree
import xml.etree.ElementTree as ET

from src.items.project_item import ProjectItem

schema = XMLSchema("res/project_schema.xsd")

project = etree.Element("project")
name = etree.SubElement(project, "name")
description = etree.SubElement(project, "description")
binaryPath = etree.SubElement(project, "binaryPath")
binaryProperties = etree.SubElement(project, "binaryProperties")
osType = etree.SubElement(binaryProperties, "os")
binaryType = etree.SubElement(binaryProperties, "binaryType")
machine = etree.SubElement(binaryProperties, "machine")
binaryClass = etree.SubElement(binaryProperties, "class")
bits = etree.SubElement(binaryProperties, "bits")
language = etree.SubElement(binaryProperties, "language")
canary = etree.SubElement(binaryProperties, "canary")
crypto = etree.SubElement(binaryProperties, "crypto")
nx = etree.SubElement(binaryProperties, "nx")
pic = etree.SubElement(binaryProperties, "pic")
relocs = etree.SubElement(binaryProperties, "relocs")
relro = etree.SubElement(binaryProperties, "relro")
stripped = etree.SubElement(binaryProperties, "stripped")

name.text = "Project 1"
description.text = "My first project"
binaryPath.text = "/mnt/c/Windows/System32/PING.exe"
osType.text = "windows"
# TODO: fill in the rest of the code

xml = open("res/project_sample.xml", "r").read().strip()
parser = ET.fromstring(xml)


# for table in parser.getiterator('project'):
#     for child in table:
#         print(child.tag, child.text)

# print(parser[3][0].tag)
# schema.is_valid(etree.tostring(project).decode())

# print(f"IS XML VALID: {schema.is_valid(etree.tostring(project).decode())}")


class ProjectSchemaParser:
    def __init__(self):
        self.schema = XMLSchema("res%sproject_schema.xsd" % os.sep)

    #     TODO: Figure out proper coupling

    def __getObject(self):
        # TODO: Get everything from the DB
        self.xml = open("res/project_sample.xml", "r").read().strip()
        parser = ET.fromstring(self.xml)
        if self.schema.is_valid(self.xml):
            item = ProjectItem()
            item.name = parser[0].text
            item.description = parser[1].text
            item.binaryPath = parser[2].text
            properties = dict()
            properties['os'] = parser[3][0].text
            properties['arch'] = parser[3][1].text
            properties['machine'] = parser[3][2].text
            properties['class'] = parser[3][3].text
            properties['bits'] = parser[3][4].text
            properties['lang'] = parser[3][5].text
            properties['canary'] = parser[3][6].text
            properties['crypto'] = parser[3][7].text
            properties['nx'] = parser[3][8].text
            properties['pic'] = parser[3][9].text
            properties['relocs'] = parser[3][10].text
            properties['relro'] = parser[3][11].text
            properties['stripped'] = parser[3][12].text
            item.binaryProperties = properties
            return item

    def getItems(self):
        return [self.__getObject()]
