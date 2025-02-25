from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from models import modelUsuario

app = FastAPI(
    title="Mi primera API",
    description="José Armando Mauricio Acevedo",
    version="1.0.1"
)

# Ya NO definas nuevamente la clase modelUsuario aquí.

usuarios = [
    {"id": 1, "nombre": "Pepe", "edad": 20, "correo": "pepe@gmail.com"},
    {"id": 2, "nombre": "Gonza", "edad": 20, "correo": "gonza@gmail.com"},
    {"id": 3, "nombre": "Karla", "edad": 21, "correo": "karla@gmail.com"},
    {"id": 4, "nombre": "Maru", "edad": 22, "correo": "maru@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return {"message": "!Bienvenido a FastAPI!"}

@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return usuarios

@app.post("/usuarios/", response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario.dict())
    return usuario

@app.put("/usuarios/{id}", response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {'Usuarios Registrados: ': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")
