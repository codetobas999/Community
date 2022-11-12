from fastapi import APIRouter , Depends , HTTPException , status , Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService
from app.core.security import create_access_token , create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserOut 
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.core.config import settings
from app.schemas.auth_schema import TokenPayload
from pydantic import ValidationError
from jose import jwt
from uuid import UUID

auth_router = APIRouter()

@auth_router.post('/login', summary="Create access and refresh token for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Incorrect email or password")

    #create  accessand refresh token
    return {
           "access_token":create_access_token(user.user_id),
           "refresh_token":create_refresh_token(user.user_id)
    }

'''
https://stackoverflow.com/questions/70928816/how-to-logout-from-jwt-security-scheme-in-fastapi
 '''
@auth_router.post("/logout", summary="Logout access token for user")
async def logout(user:User = Depends(get_current_user)):  # logout function to delete access token
    print(">>>logout : " + user.email) 
    #print(user.user_id)
    #payload = jwt.decode(token, settings.JWT_SECRET_KEY,algorithms=[settings.ALGORITHM])
    #print(payload)

    #token_data = TokenPayload(sub=1668226715,exp=0)
    #print(token_data)
    payload = {'sub': user.user_id ,'exp':0 }
    token_data = TokenPayload(**payload) 
    print(token_data)
    #return "User logout sucessful." 


@auth_router.post('/test-token', summary="Test if the access token is valid", response_model=User)
async def test_token(user:User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary="Refresh token", response_model=TokenSchema)
async def refresh_token(refresh_token:str = Body(...)):
    try:
        payload = jwt.decode(refresh_token, settings.JWT_REFRESH_SECRET_KEY,algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)
    except(jwt.JWTError,ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid  token",headers={"WWW-Authenticate":"Bearer"})
    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid  token for user")
       
    return {
        "access_token":create_access_token(user.user_id),
        "refresh_token":create_refresh_token(user.user_id)
    }
