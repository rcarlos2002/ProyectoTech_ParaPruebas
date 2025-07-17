from models.login import LoginData
from models.profesionales import Profesional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import json

from models.usuario import Usuario
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


usuarios_db = {}
profesionales_db = {}

DB_FILE="usuarios_db.json"
def CargarDB():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
            print(f"Cargando Base de datos desde {DB_FILE}")
            return{str(k): Usuario(**v) for k, v in data.items()}
    else:
        return{}
    
def guardarDB():
    with open(DB_FILE, 'w') as f:
        json.dump({str(k): v.model_dump() for k, v in usuarios_db.items()}, f, indent=4)

usuarios_db = CargarDB()



@app.get('/usuarios', response_model=list[Usuario])
async def listarUsuarios():
    return list(usuarios_db.values())

@app.post('/registrar', response_model=Usuario)
async def RegistrarUsuario(i:Usuario):
    usuarios_db[i.correo] = i
    guardarDB()
    return i

#PROFESIONES

DB_FILE_PRO="profesionales_db.json"
def CargarDBPro():
    if os.path.exists(DB_FILE_PRO):
        with open(DB_FILE_PRO, 'r') as f:
            data = json.load(f)
            print(f"Cargando Base de datos desde {DB_FILE_PRO}")
            return{str(k): Profesional(**v) for k, v in data.items()}
    else:
        return{}
    
def guardarDBPro():
    with open(DB_FILE_PRO, 'w') as f:
        json.dump({str(k): v.model_dump() for k, v in profesionales_db.items()}, f, indent=4)

profesionales_db = CargarDBPro()

@app.get('/usuarios_Pro', response_model=list[Profesional])
async def listarProfesionales():
    return list(profesionales_db.values())

@app.post('/registrar_Pro', response_model=Profesional)
async def RegistrarProfesionales(i:Profesional):
    profesionales_db[i.celular] = i
    guardarDBPro()
    return i

#LOGIN ------------------------------------------------------------------------------
@app.post("/login")
def login(data: LoginData):
    try:
        with open("usuarios_db.json", "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Base de datos no encontrada")

    # Verificamos si el correo está como clave
    if data.correo in usuarios:
        usuario = usuarios[data.correo]
        if usuario["clave"] == data.clave:
            return {"mensaje": "Inicio de sesión exitoso", "usuario": usuario}
        else:
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


#DASHBOARD
from fastapi.responses import JSONResponse

@app.get("/usuarios_Pro", response_model=list[Profesional])
async def listar_profesionales():
    return JSONResponse(content=[profesional.model_dump() for profesional in profesionales_db.values()])