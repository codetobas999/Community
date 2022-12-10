from fastapi import APIRouter  
from app.services.auth_group_service import AuthGroupService 

auth_group_router = APIRouter()
@auth_group_router.get('/',summary="Get all pages of the user")
async def list_authen_by_group(): 
    group_code = "G0001"
    return  await AuthGroupService.list_authen_by_group(group_code)