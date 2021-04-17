from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4ysrd.mongodb.net/pytech?authSource=admin&replicaSet=atlas-115hgx-shard-0&readPreference=primary&ssl=true"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit... ")