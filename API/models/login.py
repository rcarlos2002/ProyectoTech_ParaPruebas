from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

class LoginData(BaseModel):
    correo: str
    clave: str
