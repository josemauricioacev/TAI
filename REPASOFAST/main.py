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

#b. Obtener una tarea específica por su ID.
@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#c. Crear una nueva tarea.
@app.post("/tareas")
def crear_tarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea["id"]:
            raise HTTPException(status_code=400, detail="El ID de la tarea ya existe")
    tareas.append(tarea)
    return {"mensaje": "Tarea creada exitosamente", "tarea": tarea}

#d. Actualizar una tarea existente.
@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea.update(tarea_actualizada)
            return {"mensaje": "Tarea actualizada exitosamente", "tarea": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
