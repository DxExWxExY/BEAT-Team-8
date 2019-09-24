from xmlschema import XMLSchema
from lxml import etree
schema = XMLSchema("C:\\Users\\DxExWxExY\\PycharmProjects\\BEAT\\res\\project_schema.xsd")

project = etree.Element("project")
name = etree.SubElement(project, "name")
description = etree.SubElement(project, "description")
binaryPath = etree.SubElement(project, "binaryPath")
binaryProperties = etree.SubElement(project, "binaryProperties")

name.text = "Project 1"

print(etree.tostring(project, pretty_print=True))

# class ProjectSchemaParser:
#     def __init__(self):
#         pass
