from xmlschema import XMLSchema
from lxml import etree
schema = XMLSchema("C:\\Users\\DxExWxExY\\PycharmProjects\\BEAT\\res\\project_schema.xsd")

project = etree.Element("project")
name = etree.SubElement(project, "name")
description = etree.SubElement(project, "description")
binaryPath = etree.SubElement(project, "binaryPath")
binaryProperties = etree.SubElement(project, "binaryProperties")
'''
os = etree.SubElement(binary, "")
binaryType = etree.SubElement(binary, "")
machine = etree.SubElement(binary, "")
binaryClass = etree.SubElement(binary, "")
bits = etree.SubElement(binary, "")
language = etree.SubElement(binary, "")
canary = etree.SubElement(binary, "")
crypto = etree.SubElement(binary, "")
nx = etree.SubElement(binary, "")
pic = etree.SubElement(binary, "")
relocs = etree.SubElement(binary, "")
relro = etree.SubElement(binary, "")
stripped = etree.SubElement(binary, "")
'''
name.text = "Project 1"

print(etree.tostring(project, pretty_print=True))

# class ProjectSchemaParser:
#     def __init__(self):
#         pass
