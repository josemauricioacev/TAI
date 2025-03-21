from fastapi import FastAPI, HTTPException, Depends
from typing import  List
from pydantic import BaseModel
from modelsPydantic import modeloUsuario, modelAuth
from genToken import creartoken
from middleware import BearerJWT
from fastapi.responses import JSONResponse
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
    title="Mi primera API",
    description="Jose Armando Mauricio Acevedo",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

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
#EndPoint POST
@app.post("/usuarios/", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
#primero se pide el parametro y luego el tipo de datp que estamos usando
def guardar(usuario:modeloUsuario): #se guarda como usuario diccionario para pedir todos los usuarios juntos
    db=Session() #se crea la sesion
    try:
        db.add(User(**usuario.model_dump())) #se agrega el usuario a la base de datos
        db.commit() #se guarda el usuario
        return JSONResponse(status_code=201,
                            content={"mensaje": "Usuario guardado", ""
                            "usuario": usuario.model_dump()}) #se regresa el mensaje de que se guardó el usuario
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "Error al guardar el usuario", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()

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