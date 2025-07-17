
from typing import Optional
from pydantic import BaseModel

class Profesional(BaseModel):
    nombre:str
    img:str
    celular:str
    descripcion:Optional[str]
    profesionCateg:str
    email: Optional[str]
    genero: Optional[str]
    edad: Optional[int]