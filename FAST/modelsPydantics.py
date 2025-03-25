from pydantic import BaseModel, Field, EmailStr

# Modelo de usuario
class modelUsuario(BaseModel):
    name: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios, mínimo 1 y máximo 85 caracteres")
    age: int = Field(..., ge=0, le=120, description="La edad debe ser entre 0 y 120")
    email: str = Field(..., description="El correo debe ser un email válido", pattern=r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$')

# Modelo para autenticación
class modelAuth(BaseModel):
    mail: EmailStr = Field(..., description="El correo debe ser un email válido")
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña debe tener al menos 8 caracteres")