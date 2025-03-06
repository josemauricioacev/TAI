from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List # define para que los caracteres en las api sean opcionales o no
from pydantic import BaseModel
from models import modelUsuario, modelAuth
from genToken import createToken
from middleware import BearerJWT

app = FastAPI(
    title="Mi primera API",
    description="Jose Armando Mauricio Acevedo",
    version="1.0.1"
)

usuarios=[
    {"id":1, "nombre":"Armando", "edad":20,"correo":"armando@gmail.com"},
    {"id":2, "nombre":"Pepe", "edad":20,"correo":"pepe@gmail.com"},
    {"id":3, "nombre":"Gonza", "edad":21,"correo":"gonza@gmail.com"},
    {"id":4, "nombre":"Karen", "edad":22,"correo":"karen@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}





#Endpoint de tipo POST para tokens
@app.post("/auth", tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'pepe@gmail.com' and credenciales.passw == '1234567890':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return {"Aviso:": "Token Generado"}
    else:
        return{"Aviso:": "Credenciales incorrectas"}






# Enpoint CONSULTA TODOS
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer(token: str = Depends(BearerJWT())):
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