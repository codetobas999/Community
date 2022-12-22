from datetime import datetime 
from pydantic import BaseModel ,EmailStr , Field
from uuid import UUID
from typing import Optional

class SettingAppByUserCreate(BaseModel):
    user_code: EmailStr = Field(...,description="user email")
    language: str = Field(...,title='language',min_length=2 ,max_length=2) 
    theme: str = Field(...,title='theme',min_length=1 ,max_length=20) 
    show_page: int 
    token_age: int
    status: Optional[bool] = False  
 
class SettingAppByUserUpdate(BaseModel):
    user_code: EmailStr = Field(...,description="user email")
    language: str = Field(...,title='language',min_length=2 ,max_length=2) 
    theme: str = Field(...,title='theme',min_length=1 ,max_length=20) 
    show_page: int 
    token_age: int
    status: Optional[bool] = False

class SettingAppByUserOut(BaseModel):
    setting_app_by_user_id: UUID
    user_code: EmailStr
    language: str
    theme: str
    show_page: int
    token_age: int
    status: bool
    created_at: datetime
    updated_at: datetime
     