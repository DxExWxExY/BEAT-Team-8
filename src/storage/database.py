from pymongo import MongoClient

from src.items.project_item import ProjectItem


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
            if data["_id"] is None:
                self.projectsCollection.insert_one(data)
            else:
                condition = {"_id": data["_id"]}
                values = {"$set": data}
                self.projectsCollection.update_one(condition, values)

    def deleteEntry(self, which, id):
        self.db[which].delete_one({"_id": id})
