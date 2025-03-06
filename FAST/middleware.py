from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from genToken import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):  # <-- Corregido (método mágico con doble __)
        auth = await super().__call__(request)  # <-- Corregido (super() con doble __)

        data = validateToken(auth.credentials)

        if not isinstance(data, dict):
            raise HTTPException(status_code=401, detail="Token inválido")

        if data.get('mail') != 'pepe@gmail.com':  # <-- Corregido (usar 'mail' en vez de 'email')
            raise HTTPException(status_code=403, detail="Credenciales no válidas")