from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4ysrd.mongodb.net/pytech?authSource=admin&replicaSet=atlas-115hgx-shard-0&readPreference=primary&ssl=true"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

student_list ={
    "student_id": "1007",
    "first_name": "Daniel",
    "last_name": "Luo",

    "student_id": "1008",
    "first_name": "Erikson",
    "last_name": "Tuazama",

    "student_id": "1009",
    "first_name": "Amber",
    "last_name": "Jones",
}


for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

test_doc_id = students.insert_one(test_doc).inserted_id

print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

student_test_doc = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

deleted_student_test_doc = students.delete_one({"student_id": "1010"})

new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")