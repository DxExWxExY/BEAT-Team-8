import os

from xmlschema import XMLSchema
import xml.etree.ElementTree as ET

from src.items.plugin_item import PluginItem
from src.items.project_item import ProjectItem
from src.storage.database import Database


class EntriesParser:
    def __init__(self):
        self.db = Database()
        self.schema = XMLSchema(f"res{os.sep}schemas{os.sep}plugin_schema.xsd")

    def validatePluginSchema(self, instancePath):
        xml = open(instancePath, "r").read().strip()
        return self.schema.is_valid(xml)

    def getPluginFromXml(self, instancePath):
        xml = open(instancePath, "r").read().strip()
        tree = ET.fromstring(xml)
        plugin = PluginItem()
        plugin.name = tree[0].text
        plugin.description = tree[1].text
        plugin.types = ["All"] + [t.text for t in tree[2]]
        plugin.outputs = [o.text for o in tree[3]]
        for i in range(4, len(tree)):
            poi = {}
            poi['name'] = tree[i][0].text
            poi['type'] = tree[i][1].text
            poi['map'] = tree[i][2].text
            plugin.pois[tree[i][0].text] = poi
        self.db.updateEntry("plugin", plugin.asDictionary())

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
                item.outputs = entry['fields']
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
