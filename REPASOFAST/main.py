from fastapi import FastAPI, HTTPException

app = FastAPI()

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "14-02-2025",
        "estado": "completada"
    }
]

#ENDPOINTS

#a. Obtener todas las tareas.
@app.get("/tareas")
def obtener_tareas():
    return tareas

