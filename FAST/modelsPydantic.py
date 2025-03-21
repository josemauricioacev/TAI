from pydantic import BaseModel, Field, EmailStr


class modeloUsuario(BaseModel):
    name:str = Field(..., min_length=1, max_length=85, description="Letras y espacios min. 1,  máx. 85")
    age:int 
    email:str

class modelAuth(BaseModel):
    correo: EmailStr 
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña al menos de 8 caracteres")