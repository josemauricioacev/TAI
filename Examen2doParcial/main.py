from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from models import modelUsuario

app = FastAPI(
    title="Examen 2do parcial",
    description="José Armando Mauricio Acevedo",
    version="1.0.1"
)

vehiculos = [
    {"id":1, "modelo":"Urus", "año":2020, "placa":100},
    {"id":2, "modelo":"Civic", "año":2024, "placa":101},
    {"id":3, "modelo":"Tsuru", "año":1999, "placa":102},
]

@app.get("/", tags=['Inicio'])
def main():
    return {"message": "!Bienvenido a mi examen!"}
