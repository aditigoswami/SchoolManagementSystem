from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    grade: int


class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    grade: int