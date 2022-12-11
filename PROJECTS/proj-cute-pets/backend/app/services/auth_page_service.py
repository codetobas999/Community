from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.auth_page_model import AuthPage
from app.schemas.auth_page_schema import AuthPageCreate , AuthPageUpdate 


class AuthPageService:
    @staticmethod
    async def list_authPages(user: User)-> List[AuthPage]:
        authPages = await AuthPage.find({}).to_list()
        return authPages
         
     
    @staticmethod
    async def create_authPages(user: User, data: AuthPageCreate)-> AuthPage: 
        authPage = AuthPage(**data.dict(), owner=user)
        return await authPage.insert()        
    
    @staticmethod
    async def retrieve_authPage(current_user: User, auth_page_id: UUID): 
        authPage = await AuthPage.find_one(AuthPage.auth_page_id == auth_page_id )
        return authPage

    @staticmethod
    async def update_authPages(current_user: User, auth_page_id: UUID ,data: AuthPageUpdate): 
        authPage = await AuthPageService.retrieve_authPage(current_user,auth_page_id)
        await authPage.update({"$set": data.dict(exclude_unset=True)})
        await authPage.save()
        return authPage   

    @staticmethod
    async def delete_authPages(current_user: User, auth_page_id: UUID)-> None:
        authPage = await AuthPageService.retrieve_authPage(current_user,auth_page_id)
        if authPage:
            await authPage.delete() 
        return None         
    