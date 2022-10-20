# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

app = FastAPI()


# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None  # null
    is_married: Optional[bool] = None


# path operation decorator
@app.get("/")
# path operation function
def home():
    return {"hello": "World"}  # JSON


# Request and Response Body
@app.post("/person/new")
def create_person(persona:  Person = Body()):
    return {"Response": "Success",
            "Code": 200,
            "Datos_persona": persona}


# Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(None),
    age2: int = Query(),
    age3: str = Query()
):
    return [{name},{age:age2},{age2}]
