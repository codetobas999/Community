from fastapi import APIRouter , Depends
from app.models.user_model import User
from app.services.permission_user_service import AuthGroupService 
from app.api.deps.user_deps import get_current_user

permission_user_router = APIRouter()
@permission_user_router.get('/',summary="Get all pages of the user")
async def list_authen_by_group(current_user: User =  Depends(get_current_user)): 
    user_code = current_user.email
    print(user_code)
    return  await AuthGroupService.list_authen_by_group(user_code)

@permission_user_router.get('/xx',summary="Get all pages of the user")
async def list_authen_by_group(current_user: User =  Depends(get_current_user)): 
    user_code = current_user.email
    print(user_code)
    return  await AuthGroupService.list_authen_by_group2(user_code)