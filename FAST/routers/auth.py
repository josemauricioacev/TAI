from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from modelsPydantics import modelAuth
from genToken import createToken
from middlewares import BearerJWT
from fastapi import APIRouter #Agregamos nueva importacion

routerAuth = APIRouter()

#Endpoint de tipo POST para tokens
@routerAuth.post("/auth", tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'angel@gmail.com' and credenciales.passw == '12345678':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso:": "Credenciales incorrectas"}