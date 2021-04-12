from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4ysrd.mongodb.net/pytech?authSource=admin&replicaSet=atlas-115hgx-shard-0&readPreference=primary&ssl=true"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Erikson = students.find_one({"student_id": "1008"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + Erikson["student_id"] + "\n  First Name: " + Erikson["first_name"] + "\n  Last Name: " + Erikson["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")