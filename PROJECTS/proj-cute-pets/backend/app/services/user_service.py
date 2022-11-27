from typing import Optional
from uuid import UUID
from app.schemas.user_schema import UserAuth , UserUpdate
from app.models.user_model import User 
from app.core.security import get_password , verify_password 
from typing import List
import pymongo



class UserService:
    @staticmethod
    async def create_user(user: UserAuth): 
        user_in = User(
            username = user.username ,
            email = user.email,  
            first_name= user.first_name,
            last_name= user.last_name,
            disabled=user.disabled,
            hashed_password=get_password(user.password)
        )  
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str , password: str) -> Optional[User]: 
        user = await  UserService.get_user_by_email(email = email)         
        if not user:
            return None    
        if not verify_password(password=password,hashed_pass=user.hashed_password):        
            return None

        return user

    @staticmethod
    async def list_users()-> List[User]:    
        users = await User.find().to_list()    
        return users


    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]: 
        user = await  User.find_one(User.email == email) 
        return user    

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]: 
        user = await  User.find_one(User.user_id == id) 
        return user            

    @staticmethod
    async def update_user(id: UUID, data: UserUpdate) -> User:
        user = await User.find_one(User.user_id == id)
        if not user:
            raise pymongo.errors.OperationFailure("User not found")
    
        await user.update({"$set": data.dict(exclude_unset=True)})
        return user    

    @staticmethod
    async def delete_user(id: UUID)-> None:
        user = await UserService.get_user_by_id(id)
        if user:
            await user.delete() 
        return None   
