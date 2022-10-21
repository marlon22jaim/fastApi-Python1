# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()


# Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Person(BaseModel):
    first_name: str = Field(
        min_Length=1,
        max_Length=50,
        example="Marlon"
    )
    last_name: str = Field(
        min_Length=1,
        max_Length=50,
        example="Rangel"
    )
    age: int = Field(
        gt=0,
        le=115,
        example=24

    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black")  # null
    is_married: Optional[bool] = Field(default=None, example=False)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Marlon",
                "last_name": "Jaimes Rangel",
                "age": 24,
                "hair_color": "black",
                "is_married": False
            }
        }


class Location(BaseModel):
    city: str = Field(default=None, example="Toledo")
    state: str = Field(default=None, example="Departamento cualquiera XD")
    country: str = Field(default=None, example="Colombia")


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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name, It's between 1 and 50 characters",
        example="Artico"
    ),
    age: str = Query(
        title="Person Age",
        description="This is the person age. It's required",
        example=10
    ),
    age2: int = Query(
        example=10
    ),
    age3: str = Query(
        None,
        example=10)
):
    return [{name}, {age: age2}, {age2}]


# Validaciones: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        gt=0,
        title="Person id",
        description="This is the Person ID. It's required",
        example=54378910
    )
):
    return {person_id: "It exist!"}


# Validaciones:  Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=54378910
    ),
    person: Person = Body(),
    location: Location = Body()
):
    result = person.dict()
    result.update(location.dict())
    return result
