from fastapi import FastAPI

app = FastAPI()

#Ruta o EndPoint
@app.get('/')
def home():
    return {'Hola':'mundo FastAPI'}

#EndPoint promedio
@app.get('/promedio')
def promedio():
    return 10.5

#EndPoint con parámetro obligatorio
@app.get('/usuario/{id}')
def consultausuario(id:int):
    #Caso ficticio de búsqueda en BD
    return {'Se encontró el usuario':id}