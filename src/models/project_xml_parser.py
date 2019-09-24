from xmlschema import XMLSchema
from lxml import etree
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

schema.is_valid(etree.tostring(project).decode())

print(schema.is_valid(etree.tostring(project).decode()))

# class ProjectSchemaParser:
#     def __init__(self):
#         pass
