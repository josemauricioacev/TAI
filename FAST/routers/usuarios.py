from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantics import modelUsuario
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from middlewares import BearerJWT
from fastapi import APIRouter #Agregamos nueva importacion

routerUsuario = APIRouter()


# -------------------------- CRUD DE USUARIOS -------------------------- #

#EndPoint Consultar Usuarios (GET)
@routerUsuario.get("/todosUsuarios/", tags=["Operaciones CRUD"]) #declarar ruta del servidor
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
@routerUsuario.get("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
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




#Endpoint para registrar un nuevo usuario (POST)
@routerUsuario.post("/usuarios/", response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put("/usuarios/{id}", tags=["Operaciones CRUD"])
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
@routerUsuario.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
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