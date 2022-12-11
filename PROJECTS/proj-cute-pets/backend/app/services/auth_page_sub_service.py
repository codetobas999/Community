from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.auth_page_sub_model import AuthPageSub
from app.schemas.auth_page_sub_schema import AuthPageSubCreate , AuthPageSubUpdate 


class AuthPageSubService:
    @staticmethod
    async def list_authPageSubs(user: User)-> List[AuthPageSub]:
        authPageSubs = await AuthPageSub.find({}).to_list()
        return authPageSubs
         
     
    @staticmethod
    async def create_authPageSubs(user: User, data: AuthPageSubCreate)-> AuthPageSub: 
        authPageSub = AuthPageSub(**data.dict(), owner=user)
        return await authPageSub.insert()        
    
    @staticmethod
    async def retrieve_authPageSub(current_user: User, auth_page_sub_id: UUID): 
        authPageSub = await AuthPageSub.find_one(AuthPageSub.auth_page_sub_id == auth_page_sub_id )
        return authPageSub

    @staticmethod
    async def update_authPageSubs(current_user: User, auth_page_sub_id: UUID ,data: AuthPageSubUpdate): 
        authPageSub = await AuthPageSubService.retrieve_authPageSub(current_user,auth_page_sub_id)
        await authPageSub.update({"$set": data.dict(exclude_unset=True)})
        await authPageSub.save()
        return authPageSub   

    @staticmethod
    async def delete_authPageSubs(current_user: User, auth_page_sub_id: UUID)-> None:
        authPageSub = await AuthPageSubService.retrieve_authPageSub(current_user,auth_page_sub_id)
        if authPageSub:
            await authPageSub.delete() 
        return None         
    