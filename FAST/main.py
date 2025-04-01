from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from modelsPydantics import modelUsuario, modelAuth
from genToken import createToken
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from middlewares import BearerJWT
from routers.usuarios import routerUsuario #Agregamos importacion
from routers.auth import routerAuth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Mi primera API",
    description="Jose Armando Mauricio Acevedo",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lista con el string "*"
    allow_credentials=True,
    allow_methods=["*"],  # Lista con el string "*"
    allow_headers=["*"]   # Lista con el string "*"
)

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


#Endpoint para registrar un nuevo usuario
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


#Endpoint para actualizar un usuario (PUT)
@app.put("/usuarios/{id}", tags=["Operaciones CRUD"])
def actualizar_usuario(id: int, usuario: modelUsuario):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        usuario_data = usuario.model_dump()
        for key, value in usuario_data.items():
            setattr(usuario_db, key, value)
        
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado correctamente", "usuario": jsonable_encoder(usuario_db)})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                          content={"mensaje": "Error al actualizar el usuario", 
                                   "error": str(e)})
    finally:
        db.close()


#Endpoint para eliminar un usuario (DELETE)
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminar_usuario(id: int):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        db.delete(usuario_db)
        db.commit()
        return JSONResponse(content={"mensaje": f"Usuario con ID {id} eliminado correctamente"})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                          content={"mensaje": "Error al eliminar el usuario", 
                                   "error": str(e)})
    finally:
        db.close()