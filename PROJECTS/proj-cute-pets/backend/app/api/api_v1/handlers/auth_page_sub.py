from uuid import UUID
from fastapi import APIRouter , Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.auth_page_sub_schema import AuthPageSubOut, AuthPageSubCreate , AuthPageSubUpdate 
from app.services.auth_page_sub_service import AuthPageSubService
from app.models.auth_page_sub_model import AuthPageSub
from typing import List

auth_page_sub_router = APIRouter()

@auth_page_sub_router.get('/',summary="Get all Auth Page Sub all",response_model=List[AuthPageSubOut])
async def list(current_user: User =  Depends(get_current_user)):
    return await AuthPageSubService.list_authPageSubs(current_user)


@auth_page_sub_router.post('/create',summary="Create Auth Page Sub",response_model=AuthPageSub)
async def create_auth_page_sub(data: AuthPageSubCreate , current_user: User =  Depends(get_current_user)):
    return await AuthPageSubService.create_authPageSubs(current_user,data)

@auth_page_sub_router.get('/{auth_page_sub_id}',summary="Get a Auth Page Sub by auth_page_sub_id",response_model=AuthPageSubOut)
async def retrieve(auth_page_sub_id: UUID , current_user: User =  Depends(get_current_user)):
    return await AuthPageSubService.retrieve_authPageSub(current_user,auth_page_sub_id)
 
@auth_page_sub_router.put('/{auth_page_sub_id}',summary="Update Auth Page Sub by auth_page_sub_id",response_model=AuthPageSubOut)
async def update(auth_page_sub_id: UUID , data: AuthPageSubUpdate ,current_user: User =  Depends(get_current_user)):
    return await AuthPageSubService.update_authPageSubs(current_user,auth_page_sub_id,data)

@auth_page_sub_router.delete('/{auth_page_sub_id}',summary="Delete Auth Page Sub by auth_page_sub_id")
async def delete(auth_page_sub_id: UUID ,current_user: User =  Depends(get_current_user)):
    await AuthPageSubService.delete_authPageSubs(current_user,auth_page_sub_id)    
    return None
