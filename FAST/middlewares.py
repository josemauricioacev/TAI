from genToken import validateToken
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

# Middleware de autenticación con JWT
class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)

        if not isinstance(data, dict):  # Verificar si es un diccionario válido
            raise HTTPException(status_code=401, detail="Token inválido")

        if data.get('mail') != 'angel@gmail.com':  # Corrección: ahora usa 'mail' en lugar de 'email'
            raise HTTPException(status_code=403, detail="Credenciales no válidas")

        return data