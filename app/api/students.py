from fastapi import APIRouter, status
from app.schemas.student import StudentCreate, StudentUpdate
from app.services.student_service import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
)

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/{student_id}")
def get_student(student_id: str):
    student = get_student_by_id(student_id)
    if not student:
        return {"message": "Student not found"}
    return student

@router.get("/")
def get_students():
    return get_all_students()   

'''
   return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
'''

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    created_student = create_student(student)
    return {
        "message": "Student created successfully",
        "student": created_student,
    }

@router.put("/{student_id}")
def update(student_id: str, student: StudentUpdate):
    return update_student(student_id, student)

@router.delete("/{student_id}")
def delete(student_id: str):
    return delete_student(student_id)