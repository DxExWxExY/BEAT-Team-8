from xmlschema import XMLSchema
from lxml import etree
import xml.etree.ElementTree as ET

from src.items.project_item import ProjectItem

schema = XMLSchema("C:\\Users\\DxExWxExY\\PycharmProjects\\BEAT\\res\\project_schema.xsd")

project = etree.Element("project")
name = etree.SubElement(project, "name")
description = etree.SubElement(project, "description")
binaryPath = etree.SubElement(project, "binaryPath")
binaryProperties = etree.SubElement(project, "binaryProperties")
os = etree.SubElement(binaryProperties, "os")
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
os.text = "windows"
# TODO: fill in the rest of the code

xml = open("C:\\Users\\DxExWxExY\\PycharmProjects\\BEAT\\res\\project_sample.xml", "r").read().strip()
parser = ET.fromstring(xml)

# for table in parser.getiterator('project'):
#     for child in table:
#         print(child.tag, child.text)

# print(parser[3][0].tag)
# schema.is_valid(etree.tostring(project).decode())

# print(f"IS XML VALID: {schema.is_valid(etree.tostring(project).decode())}")



class ProjectSchemaParser:
    def __init__(self):
        self.schema = XMLSchema("C:\\Users\\DxExWxExY\\PycharmProjects\\BEAT\\res\\project_schema.xsd")
    #     TODO: Figure out proper coupling

    def __getObject(self):
        self.xml = ""
        # TODO: Get everything from the DB
        parser = ET.fromstring(self.xml)
        if self.schema.is_valid(self.xml):
            print("Is valid")

    def getItems(self):
        if type is 0:
            return [ProjectItem(i) for i in range(5)]