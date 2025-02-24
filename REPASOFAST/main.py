from fastapi import FastAPI, HTTPException
from typing import Optional, List # define para que los caracteres en las api sean opcionales o no
from pydantic import BaseModel

app = FastAPI(
    title="Mi primera API",
    description="José Armando Mauricio Acevedo",
    version="1.0.1"
)
class modelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

usuarios=[
    {"id":1, "nombre":" Pepe", "edad":20,"correo":"pepe@gmail.com"},
    {"id":2, "nombre":"Gonza", "edad":20,"correo":"gonza@gmail.com"},
    {"id":3, "nombre":"Karla", "edad":21,"correo":"karla@gmail.com"},
    {"id":4, "nombre":"Maru", "edad":22,"correo":"maru@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FastAPI!"}



# Enpoint CONSULTA TODOS
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return usuarios


#Endpoint de tipo POST
@app.post("/usuarios/", response_model= modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"]==usuario.id:
         raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario.dict())
    return usuario

#Endpoint para actualizar
@app.put("/usuarios/{id}",response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")



#Endpoint para eliminar
@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios.pop(index)
            return { 'Usuarios Registrados: ': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")
    