from fastapi import FastAPI
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

#Endpoint promedio
@app.get('/promedio', tags = ['Mi calificación TAI'])
def promedio():
    return 10.5

@app.get('/usuario/{id}', tags = ['Endpoint parametro obligatorio'])
def consultarUsuario(id : int):
    return "Se encontro el usuario: {id}"

#Endpoint parametro opcional
@app.get('/usuario2/', tags = ['Endpoint parametro opcional'])
def consultarUsuario2(id : Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return{"mensaje ":"usuario encontrado", "El usaurio esta es":usuario}
            
        return{"mensaje":f"No se encontró el id:{id}" }
    return{"mensaje":"No se proporcionó un id"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}