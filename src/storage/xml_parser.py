import os

from xmlschema import XMLSchema
from lxml import etree
import xml.etree.ElementTree as ET

from src.items.plugin_item import PluginItem
from src.items.project_item import ProjectItem


class XMLParser:
    def __init__(self):
        self.schema = XMLSchema("res%sproject_schema.xsd" % os.sep)

    def __getObject(self):
        # TODO: Get everything from the DB
        xml = open("res%sproject_sample.xml" % os.sep, "r").read().strip()
        parser = ET.fromstring(xml)
        if self.schema.is_valid(xml):
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

    def updateEntry(self, item):
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

        name.text = item.name
        description.text = item.description
        binaryPath.text = item.binaryPath
        osType.text = item.binaryProperties['os']
        binaryType.text = item.binaryProperties['arch']
        machine.text = item.binaryProperties['machine']
        binaryClass.text = item.binaryProperties['class']
        bits.text = item.binaryProperties['bits']
        language.text = item.binaryProperties['lang']
        canary.text = item.binaryProperties['canary']
        crypto.text = item.binaryProperties['crypto']
        nx.text = item.binaryProperties['nx']
        pic.text = item.binaryProperties['pic']
        relocs.text = item.binaryProperties['relocs']
        relro.text = item.binaryProperties['relro']
        stripped.text = item.binaryProperties['stripped']

        xml = etree.tostring(project).decode()
        if self.schema.is_valid(xml):
            # TODO: send query to DB to update this specific entry
            print("XML IS VALID")

    def getFilterAndPlugin(self, plugin):
        if plugin == 'pa':
            return plugin

    def __pluginsFromDB(self):
        # DB query as objs
        return []

    def __deserializer(self):
        return object()

    def getEntries(self, which):
        if which == "plugin":
            item = PluginItem()
            item.name = "Network Plugin"
            item.types = ["All", "Function" , "Variable", "String", "DLL", "Struct", "Packet Protocol"]
            return [item]