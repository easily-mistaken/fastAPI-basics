from typing import Dict, Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()



class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

students: Dict[str, Student] = {
    '1': Student( name='john', age=13, year='sophomore' )
}

@app.get("/")
def index():
    return {"name": "first Data"}

@app.get("/get-all")
def get_all_students():
    return students

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=100)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if(students[student_id].name == name):
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    print(student)
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    print('student id is ', student_id)
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id] 

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]

    return students
