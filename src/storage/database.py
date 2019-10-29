from pymongo import MongoClient

from src.items.plugin_item import PluginItem


class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['beat']
        self.projectsCollection = self.db['project']
        self.pluginsCollection = self.db['plugins']

    def getEntries(self, type):
        return self.db[type].find()

    def updateEntry(self, which, data):
        if which == "project":
            if not "_id" in data.keys():
                self.projectsCollection.insert_one(data)
            else:
                condition = {"_id": data["_id"]}
                values = {"$set": data}
                self.projectsCollection.update_one(condition, values)
        if which == "plugin":
            if not "_id" in data.keys():
                self.pluginsCollection.insert_one(data)
            else:
                condition = {"_id": data["_id"]}
                values = {"$set": data}
                self.projectsCollection.update_one(condition, values)

    def deleteEntry(self, which, id):
        self.db[which].delete_one({"_id": id})

if __name__ == "__main__":
    item = PluginItem()
    item.name = "Network Plugin"
    item.types = ["All", "Function", "Variable", "String", "DLL", "Struct", "Packet Protocol"]
    item.pois = ["network", "socket", "ip"]
    item.outputFields = ["Jinja Script"]

    db = Database()
    db.updateEntry("plugin", item.asDictionary())