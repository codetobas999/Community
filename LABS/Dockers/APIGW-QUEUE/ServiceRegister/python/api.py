from fastapi import FastAPI
from pydantic import BaseModel



class Student(BaseModel):
    firstname:str
    lastname:str
    email:str

app = FastAPI() 

@app.post("/register")
def api(student_item: Student):
    print("IN Loop register")
    return {'results': 'registered'}
 