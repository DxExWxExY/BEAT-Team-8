import os

from xmlschema import XMLSchema
import xml.etree.ElementTree as ET

from src.items.plugin_item import PluginItem
from src.items.project_item import ProjectItem
from src.storage.database import Database


class EntriesParser:
    def __init__(self):
        self.db = Database()
        self.schema = XMLSchema(f"..{os.sep}..{os.sep}res{os.sep}plugin_schema.xsd")

    def validatePluginSchema(self, instancePath):
        xml = open(instancePath, "r").read().strip()
        return self.schema.is_valid(xml)

    def updateEntry(self, which, item):
        if which == "project":
            self.db.updateEntry("project", item.asDictionary())
        if which == "plugin":
            self.db.updateEntry("plugin", item.asDictionary())

    def getEntries(self, which):
        if which == "plugin":
            entries = {}
            for entry in self.db.getEntries('plugin'):
                item = PluginItem()
                item.id = entry['_id']
                item.name = entry['name']
                item.description = entry['description']
                item.outputFields = entry['fields']
                item.pois = entry['pois']
                item.types = entry['types']
                entries[item.name] = item
            return entries
        if which == "project":
            entries = {}
            for entry in self.db.getEntries('project'):
                item = ProjectItem()
                item.id = entry['_id']
                item.name = entry['name']
                item.description = entry['description']
                item.binaryPath = entry['path']
                item.binaryProperties = entry['properties']
                item.results = entry['results']
                entries[item.name] = item
            return entries

    def deleteEntry(self, which, item):
        self.db.deleteEntry(which, item.id)