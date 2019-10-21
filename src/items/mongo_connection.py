import pymongo

client = pymongo.MongoClient(
   "mongodb+srv://eaelguea:beat2019>@beatteam8-qil4h.mongodb.net/test?retryWrites=true&w=majority")

db = client.test

db = client['project_sample']
project = db['pro']

project_sample = {
    'name': 'sample',
    'description': ' ',
    'binaryPath': ' ',
    'binaryProperties': ' ',

}
contents = project.insert_one(project_sample)
print('One session: {0}' . format(contents.inserted_id))

for contents in project.find():
    print(contents)