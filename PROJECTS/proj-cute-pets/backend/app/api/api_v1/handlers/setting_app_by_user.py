from uuid import UUID
from fastapi import APIRouter , Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.setting_app_by_user_schema import SettingAppByUserOut, SettingAppByUserCreate , SettingAppByUserUpdate 
from app.services.setting_app_by_user_service import SettingAppByUserService
from app.models.setting_app_by_user_model import SettingAppByUser
from typing import List

setting_app_by_user_router = APIRouter()

@setting_app_by_user_router.get('/',summary="Get all Setting All by User all",response_model=List[SettingAppByUserOut])
async def list(current_user: User =  Depends(get_current_user)):
    return await SettingAppByUserService.list_settingAppByUsers(current_user)

@setting_app_by_user_router.get('/user',summary="Get all Setting All by User",response_model=SettingAppByUserOut)
async def get(current_user: User =  Depends(get_current_user)):
    return await SettingAppByUserService.get_settingAppByUsers(current_user)


@setting_app_by_user_router.post('/create',summary="Create Setting All by User",response_model=SettingAppByUser)
async def create_auth_user_group(data: SettingAppByUserCreate , current_user: User =  Depends(get_current_user)):
    return await SettingAppByUserService.create_settingAppByUsers(current_user,data)

@setting_app_by_user_router.get('/{setting_app_by_user_id}',summary="Get by setting_app_by_user_id",response_model=SettingAppByUserOut)
async def retrieve(setting_app_by_user_id: UUID , current_user: User =  Depends(get_current_user)):
    return await SettingAppByUserService.retrieve_settingAppByUsers(current_user,setting_app_by_user_id)
 
@setting_app_by_user_router.put('/{setting_app_by_user_id}',summary="Update by setting_app_by_user_id",response_model=SettingAppByUserOut)
async def update(setting_app_by_user_id: UUID , data: SettingAppByUserUpdate ,current_user: User =  Depends(get_current_user)):
    return await SettingAppByUserService.update_settingAppByUsers(current_user,setting_app_by_user_id,data)

@setting_app_by_user_router.delete('/{setting_app_by_user_id}',summary="Delete by setting_app_by_user_id")
async def delete(setting_app_by_user_id: UUID ,current_user: User =  Depends(get_current_user)):
    await SettingAppByUserService.delete_settingAppByUsers(current_user,setting_app_by_user_id)    
    return None
