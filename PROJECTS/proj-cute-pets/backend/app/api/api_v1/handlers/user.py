from uuid import UUID
from fastapi import APIRouter , HTTPException , status
from app.schemas.user_schema import UserAuth, UserOut, UserUpdate
from app.services.user_service import UserService
from fastapi import Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from typing import List
import pymongo 


user_router = APIRouter()

@user_router.get('/',summary="Get all user",response_model=List[User])
async def list():
    return await UserService.list_users()


@user_router.post('/create' , summary="Create new user", response_model=User)
async def create_user(data: UserAuth):
    try: 
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
 
#@user_router.get('/me', summary='Get details of currently logged in user', response_model=User)
#async def get_me(user: User = Depends(get_current_user)):
#   return user    
@user_router.get('/me', summary='Get details of currently logged in user')
async def get_me(user: User = Depends(get_current_user)):
    return {
        "data":{
            "user": user
        }
    }
    #return user


@user_router.post('/update', summary='Update User', response_model=User)
async def update_user(data: UserUpdate, user: User = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist"
        )

@user_router.delete('/{user_id}',summary="Delete User by User id")
async def delete(user_id: UUID):
    await UserService.delete_user(user_id)    
    return None