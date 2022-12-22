from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.setting_app_by_user_model import SettingAppByUser
from app.schemas.setting_app_by_user_schema import SettingAppByUserCreate , SettingAppByUserUpdate 


class SettingAppByUserService:
    @staticmethod
    async def list_settingAppByUsers(user: User)-> List[SettingAppByUser]:
        settingAppByUsers = await SettingAppByUser.find({}).to_list()
        return settingAppByUsers
         
    @staticmethod
    async def get_settingAppByUsers(user: User)-> SettingAppByUser :
        settingAppByUsers = await SettingAppByUser.find_one({"user_code":user.email})
        return settingAppByUsers         
     
    @staticmethod
    async def create_settingAppByUsers(user: User, data: SettingAppByUserCreate)-> SettingAppByUser: 
        settingAppByUsers = SettingAppByUser(**data.dict(), owner=user)
        return await settingAppByUsers.insert()        
    
    @staticmethod
    async def retrieve_settingAppByUsers(current_user: User, setting_app_by_user_id: UUID): 
        settingAppByUsers = await SettingAppByUser.find_one(SettingAppByUser.setting_app_by_user_id == setting_app_by_user_id )
        return settingAppByUsers

    @staticmethod
    async def update_settingAppByUsers(current_user: User, setting_app_by_user_id: UUID ,data: SettingAppByUserUpdate): 
        settingAppByUsers = await SettingAppByUserService.retrieve_settingAppByUsers(current_user,setting_app_by_user_id)
        await settingAppByUsers.update({"$set": data.dict(exclude_unset=True)})
        await settingAppByUsers.save()
        return settingAppByUsers   

    @staticmethod
    async def delete_settingAppByUsers(current_user: User, setting_app_by_user_id: UUID)-> None:
        settingAppByUsers = await SettingAppByUserService.retrieve_settingAppByUsers(current_user,setting_app_by_user_id)
        if settingAppByUsers:
            await settingAppByUsers.delete() 
        return None         
    