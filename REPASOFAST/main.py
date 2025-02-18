from fastapi import FastAPI, HTTPException

app = FastAPI(
    title = "Mi primer API",
    description = "Jose Armando Mauricio Acevedo",
    version = "10.0.0.1"
)

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "14-02-2025",
        "estado": "completada"
    },
    {
        "id": 2,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "11-02-2025",
        "estado": "completada"
    },
    {
        "id": 3,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "14-01-2025",
        "estado": "incompletada"
    }
]

#ENDPOINTS

#a. Obtener todas las tareas.
@app.get("/tareas", tags = ["Obten todas las tareas"])
def obtener_tareas():
    return tareas

#b. Obtener una tarea específica por su ID.
@app.get("/tareas/{id}", tags = ["Encuentra una tarea por ID"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#c. Crear una nueva tarea.
@app.post("/tareas", tags = ["Crea tareas"])
def crear_tarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea["id"]:
            raise HTTPException(status_code=400, detail="El ID de la tarea ya existe")
    tareas.append(tarea)
    return {"mensaje": "Tarea creada exitosamente", "tarea": tarea}

#d. Actualizar una tarea existente.
@app.put("/tareas/{id}", tags = ["Actualiza tus tareas"])
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea.update(tarea_actualizada)
            return {"mensaje": "Tarea actualizada exitosamente", "tarea": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#e. Eliminar una tarea.
@app.delete("/tareas/{id}", tags = ["Elimina tareas"])
def eliminar_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            return {"mensaje": "Tarea eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
