from app.db.database import db
from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId

students_collection = db.students

def get_student_by_id(student_id: str):

    try:
        object_id = ObjectId(student_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student["_id"] = str(student["_id"])

    return student

def update_student(student_id: str, student):
    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return get_student_by_id(student_id)

def get_all_students():
    students = []

    for student in students_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)

    return students


def create_student(student):
    if student.grade < 1 or student.grade > 12:
        raise HTTPException(
            status_code=400,
            detail="Grade must be between 1 and 12"
        )


    existing = students_collection.find_one(
        {"email": student.email}
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
            )
        
    student_data = student.model_dump()
    result = students_collection.insert_one(student_data)
    return {
    "id": str(result.inserted_id)
    }
#return student_data

def delete_student(student_id: str):
    result = students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }
