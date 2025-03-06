import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(data:dict):
    token: str = jwt.encode( payload=data, key='secretKey', algorithm='HS256')
    return token

def validateToken(token:str):
    try:
        data:dict = jwt.decode(token,key='secretKey', algorithm=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token Expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")