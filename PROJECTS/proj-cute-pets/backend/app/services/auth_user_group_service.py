from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.auth_user_group_model import AuthUserGroup
from app.schemas.auth_user_group_schema import AuthUserGroupCreate , AuthUserGroupUpdate 


class AuthUserGroupService:
    @staticmethod
    async def list_authUserGroups(user: User)-> List[AuthUserGroup]:
        authUserGroups = await AuthUserGroup.find({}).to_list()
        return authUserGroups
         
     
    @staticmethod
    async def create_authUserGroups(user: User, data: AuthUserGroupCreate)-> AuthUserGroup: 
        authUserGroup = AuthUserGroup(**data.dict(), owner=user)
        return await authUserGroup.insert()        
    
    @staticmethod
    async def retrieve_authUserGroups(current_user: User, auth_user_id: UUID): 
        authUserGroup = await AuthUserGroup.find_one(AuthUserGroup.auth_user_id == auth_user_id )
        return authUserGroup

    @staticmethod
    async def update_authUserGroups(current_user: User, auth_user_id: UUID ,data: AuthUserGroupUpdate): 
        authUserGroup = await AuthUserGroupService.retrieve_authUserGroups(current_user,auth_user_id)
        await authUserGroup.update({"$set": data.dict(exclude_unset=True)})
        await authUserGroup.save()
        return authUserGroup   

    @staticmethod
    async def delete_authUserGroups(current_user: User, auth_user_id: UUID)-> None:
        authUserGroup = await AuthUserGroupService.retrieve_authUserGroups(current_user,auth_user_id)
        if authUserGroup:
            await authUserGroup.delete() 
        return None         
    