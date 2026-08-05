from fastapi import FastAPI
from app.api.students import router as student_router

app = FastAPI()
app.include_router(student_router)

@app.get("/")
def home():
    return {"message": "Welcome to School Management"}

@app.get("/health")
def health():
    return {"status": "OK"}
