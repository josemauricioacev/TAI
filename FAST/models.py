from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id siempre debe ser positivo")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios...")
    edad: int = Field(..., ge=0, le=100, description="Solo se aceptan edades desde 0 a 100")
    correo: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', description="Debe ser un correo válido")
