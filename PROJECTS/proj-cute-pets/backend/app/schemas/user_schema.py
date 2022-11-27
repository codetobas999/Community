from pydantic import BaseModel ,EmailStr , Field
from uuid import UUID
from typing import Optional

class UserAuth(BaseModel):
    email: EmailStr = Field(...,description="user email")
    username: str = Field(...,min_length=5 ,max_length=50, description="user username")
    password: str = Field(...,min_length=5 ,max_length=50 ,description="user password")
    first_name: str = Field(...,min_length=1 ,max_length=50 ,description="first name")
    last_name: str  = Field(...,min_length=1 ,max_length=50 ,description="last name")
    disabled: bool = False
 
class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr 
    first_name: str #Optional[str]
    last_name: str #Optional[str]
    disabled: Optional[bool] = False

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None