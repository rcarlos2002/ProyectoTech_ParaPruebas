from pydantic import BaseModel

class Usuario(BaseModel):
    nombre:str
    correo:str
    clave:str