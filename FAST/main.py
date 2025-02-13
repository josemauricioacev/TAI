from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title = "Mi primer API",
    description = "Jose Armando",
    version = "10.0.0.1"
)

usuarios = [
    {"id":1, "nombre":"Jose", "edad":21},
    {"id":2, "nombre":"Pepe", "edad":20},
    {"id":3, "nombre":"Gonza", "edad":19},
    {"id":4, "nombre":"Perla", "edad":21},
]

#Ruta o EndPoint
@app.get('/', tags = ["inicio"])
def home():
    return {'Hola':'mundo FastAPI'}

#Ruta o EndPoint para consultar todos los usuarios
@app.get('/todosUsuarios', tags = ["Operaciones CRUD"])
def leer():
    return {'Usuarios' : usuarios}

#Ruta o EndPoint POST
@app.post('/usuarios/', tags = ["Operaciones CRUD"])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code = 400, detail = "El usuario ya existe") #Sirve para marcar error
    usuarios.append(usuario)
    return usuario

#Ruta o EndPoint para actualizar
@app.put('/usuarios/{id}', tags = ["Operaciones CRUD"])
def actualizar(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code = 400, detail = "El usuario no existe")

#Ruta o EndPoint para eliminar
@app.delete('/usuarios/{id}', tags = ["Operaciones CRUD"])
def eliminar(id:int, usuarioEliminado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            del usuarios[index]
            return ("El usuario ha sido eliminado")
        else:
            raise HTTPException(status_code=404, detail="El usuario no ha sido encontrado")