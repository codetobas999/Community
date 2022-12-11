from uuid import UUID
from fastapi import APIRouter , Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.auth_user_group_schema import AuthUserGroupOut, AuthUserGroupCreate , AuthUserGroupUpdate 
from app.services.auth_user_group_service import AuthUserGroupService
from app.models.auth_user_group_model import AuthUserGroup
from typing import List

auth_user_group_router = APIRouter()

@auth_user_group_router.get('/',summary="Get all auth user all",response_model=List[AuthUserGroupOut])
async def list(current_user: User =  Depends(get_current_user)):
    return await AuthUserGroupService.list_authUserGroups(current_user)


@auth_user_group_router.post('/create',summary="Create auth user",response_model=AuthUserGroup)
async def create_auth_user_group(data: AuthUserGroupCreate , current_user: User =  Depends(get_current_user)):
    return await AuthUserGroupService.create_authUserGroups(current_user,data)

@auth_user_group_router.get('/{auth_user_id}',summary="Get a auth user by auth_user_id",response_model=AuthUserGroupOut)
async def retrieve(auth_user_id: UUID , current_user: User =  Depends(get_current_user)):
    return await AuthUserGroupService.retrieve_authUserGroups(current_user,auth_user_id)
 
@auth_user_group_router.put('/{auth_user_id}',summary="Update auth user by auth_user_id",response_model=AuthUserGroupOut)
async def update(auth_user_id: UUID , data: AuthUserGroupUpdate ,current_user: User =  Depends(get_current_user)):
    return await AuthUserGroupService.update_authUserGroups(current_user,auth_user_id,data)

@auth_user_group_router.delete('/{auth_user_id}',summary="Delete todo by auth_user_id")
async def delete(auth_user_id: UUID ,current_user: User =  Depends(get_current_user)):
    await AuthUserGroupService.delete_authUserGroups(current_user,auth_user_id)    
    return None
