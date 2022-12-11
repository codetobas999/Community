from datetime import datetime 
from pydantic import BaseModel ,EmailStr , Field
from uuid import UUID
from typing import Optional

class AuthUserGroupCreate(BaseModel):
    user_code: EmailStr = Field(...,description="user email")
    group_code: str = Field(...,title='group_code',min_length=1 ,max_length=55) 
    status: Optional[bool] = False 


class AuthUserGroupUpdate(BaseModel):
    user_code: EmailStr = Field(...,description="user email")
    group_code: str = Field(...,title='group_code',min_length=1 ,max_length=55) 
    status: Optional[bool] = False 

class AuthUserGroupOut(BaseModel):
    auth_user_id: UUID
    user_code: EmailStr
    group_code: str
    status: bool
    created_at: datetime
    updated_at: datetime
     