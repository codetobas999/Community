from pydantic import BaseModel 
from uuid import UUID
#from app.models.user_model import User

class TokenSchema(BaseModel):
    #user: User
    access_token: str 
    refresh_token: str 

class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None