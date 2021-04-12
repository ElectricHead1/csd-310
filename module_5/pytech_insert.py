from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4ysrd.mongodb.net/pytech?authSource=admin&replicaSet=atlas-115hgx-shard-0&readPreference=primary&ssl=true"

client = MongoClient(url)

db = client.pytech

Daniel = {
    "student_id": "1007",
    "first_name": "Daniel",
    "last_name": "Luo",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.9",
            "start_date": "Feb 15, 2021",
            "end_date": "May 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "JAVA ",
                    "instructor": "Professor Payne",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD310",
                    "description": "Database",
                    "instructor": "Professor Soriano",
                    "grade": "A+"
                }
            ]
        }
    ]

}


Erikson = {
    "student_id": "1008",
    "first_name": "Erikson",
    "last_name": "Tuazama",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "4.0",
            "start_date": "Feb 15, 2021",
            "end_date": "May 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "JAVA",
                    "instructor": "Professor Payne",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD310",
                    "description": "Database",
                    "instructor": "Professor Soriano",
                    "grade": "B+"
                }
            ]
        }
    ]
}

Amber = {
    "student_id": "1009",
    "first_name": "Amber",
    "last_name": "Jones",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.5",
            "start_date": "Feb 15, 2021",
            "end_date": "May 20, 2021",
            "courses": [
                {
                    "course_id": "CSD320",
                    "description": "JAVA",
                    "instructor": "Professor Payne",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD310",
                    "description": "Database",
                    "instructor": "Professor Soriano",
                    "grade": "B+"
                }
            ]
        }
    ]
}

students = db.students
print("\n  -- INSERT STATEMENTS --")
Daniel_student_id = students.insert_one(Daniel).inserted_id
print("  Inserted student record Daniel Luo into the students collection with document_id " + str(Daniel_student_id))

Erikson_student_id = students.insert_one(Erikson).inserted_id
print("  Inserted student record Erikson Tuazama into the students collection with document_id " + str(Erikson_student_id))

Amber_student_id = students.insert_one(Amber).inserted_id
print("  Inserted student record Amber Jones into the students collection with document_id " + str(Amber_student_id))

input("\n\n  End of program, press any key to exit... ")