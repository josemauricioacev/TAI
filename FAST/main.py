from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from modelsPydantics import modelUsuario, modelAuth
from genToken import createToken
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from middlewares import BearerJWT


app = FastAPI(
    title="Mi primera API",
    description="Jose Armando Mauricio Acevedo",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

usuarios=[
    {"id":1, "nombre":"Angel", "edad":20,"correo":"angelmaryinez1@gmail.com"},
    {"id":2, "nombre":"Daniel", "edad":20,"correo":"daniel@gmail.com"},
    {"id":3, "nombre":"Alfredo", "edad":21,"correo":"alfredo@gmail.com"},
    {"id":4, "nombre":"Aaron", "edad":22,"correo":"aaron@gmail.com"},
]

@app.get("/", tags=['Inicio'])
def main():
    return{"message": "!Bienvenido a FasAPI!"}





#Endpoint de tipo POST para tokens
@app.post("/auth", tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'angel@gmail.com' and credenciales.passw == '12345678':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso:": "Credenciales incorrectas"}





#EndPoint Consultar Usuarios (GET)
@app.get("/todosUsuarios/", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leer(): #funcion que se ejecutará cuando se entre a la ruta
    db=Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible consultar al usuario.", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()


#EndPoint Consultar Usuarios por ID (GET)
@app.get("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leeruno(id:int): #funcion que se ejecutará cuando se entre a la ruta
    db=Session()
    try:
        consulta1=db.query(User).filter(User.id==id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={'mensaje':"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta1))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible consultar al usuario.", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()




# Endpoint para registrar un nuevo usuario
@app.post("/usuarios/", response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario: modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario Guardado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()



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