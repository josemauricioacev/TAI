from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List 
from pydantic import BaseModel
from models import modelUsuario, modelAuth
from genToken import createToken
from middleware import BearerJWT

app = FastAPI(
    title="Mi primera API",
    description="Jose Armando Mauricio Acevedo",
    version="1.0.1"
)

# Lista de todos los usuarios
usuarios=[
    {"id":1, "nombre":"Armando", "edad":20,"correo":"armando@gmail.com"},
    {"id":2, "nombre":"Pepe", "edad":20,"correo":"pepe@gmail.com"},
    {"id":3, "nombre":"Gonza", "edad":21,"correo":"gonza@gmail.com"},
    {"id":4, "nombre":"Karen", "edad":22,"correo":"karen@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "¡Bienvenido a FastAPI!"}

#Endpoint para autenticar
@app.post("/auth", tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.mail == 'pepe@gmail.com' and autorizado.passw == '1234567890':
        token: str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso:": "Credenciales incorrectas"}

# Enpoint para consultar todos los usuarios
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer(token: str = Depends(BearerJWT())):
    return usuarios

#Endpoint para agregar usuarios
@app.post("/usuarios/", response_model= modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"]==usuario.id:
         raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario.dict())
    return usuario

#Endpoint para actualizar usuarios
@app.put("/usuarios/{id}",response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

#Endpoint para eliminar usuarios
@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios.pop(index)
            return { 'Usuarios Registrados: ': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")