from uuid import UUID
from fastapi import APIRouter , Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.auth_page_schema import AuthPageOut, AuthPageCreate , AuthPageUpdate 
from app.services.auth_page_service import AuthPageService
from app.models.auth_page_model import AuthPage
from typing import List

auth_page_router = APIRouter()

@auth_page_router.get('/',summary="Get all Auth Page all",response_model=List[AuthPageOut])
async def list(current_user: User =  Depends(get_current_user)):
    return await AuthPageService.list_authPages(current_user)


@auth_page_router.post('/create',summary="Create Auth Page",response_model=AuthPage)
async def create_auth_page(data: AuthPageCreate , current_user: User =  Depends(get_current_user)):
    return await AuthPageService.create_authPages(current_user,data)

@auth_page_router.get('/{auth_page_id}',summary="Get a Auth Page by auth_page_id",response_model=AuthPageOut)
async def retrieve(auth_page_id: UUID , current_user: User =  Depends(get_current_user)):
    return await AuthPageService.retrieve_authPage(current_user,auth_page_id)
 
@auth_page_router.put('/{auth_page_id}',summary="Update Auth Page by auth_page_id",response_model=AuthPageOut)
async def update(auth_page_id: UUID , data: AuthPageUpdate ,current_user: User =  Depends(get_current_user)):
    return await AuthPageService.update_authPages(current_user,auth_page_id,data)

@auth_page_router.delete('/{auth_page_id}',summary="Delete Auth Page by auth_page_id")
async def delete(auth_page_id: UUID ,current_user: User =  Depends(get_current_user)):
    await AuthPageService.delete_authPages(current_user,auth_page_id)    
    return None
