from datetime import datetime
from pydantic import BaseModel , Field
from uuid import UUID
from typing import Optional

class AuthPageSubCreate(BaseModel):
    page_code: str = Field(...,title='Page Code',min_length=1 ,max_length=55)
    page_sub_code: str = Field(...,title='Page Sub Code',min_length=1 ,max_length=55)
    menu_sub_name_en : str = Field(...,title='Menu Name EN',min_length=1 ,max_length=755)
    menu_sub_name_th : str = Field(...,title='Menu Name TH',min_length=1 ,max_length=755)
    icon : str = Field(...,title='Icon',min_length=1 ,max_length=150)
    to : str = Field(...,title='To',min_length=1 ,max_length=755)
    status: Optional[bool] = False  


class AuthPageSubUpdate(BaseModel):
    page_code: str = Field(...,title='Page Code',min_length=1 ,max_length=55)
    page_sub_code: str = Field(...,title='Page Sub Code',min_length=1 ,max_length=55)
    menu_sub_name_en : str = Field(...,title='Menu Name EN',min_length=1 ,max_length=755)
    menu_sub_name_th : str = Field(...,title='Menu Name TH',min_length=1 ,max_length=755)
    icon : str = Field(...,title='Icon',min_length=1 ,max_length=150)
    to : str = Field(...,title='To',min_length=1 ,max_length=755)
    status: Optional[bool] = False 

class AuthPageSubOut(BaseModel):
    auth_page_sub_id: UUID 
    page_code: str
    page_sub_code: str
    menu_sub_name_en: str
    menu_sub_name_th: str
    icon: str
    to: str
    status: bool
    created_at: datetime
    updated_at: datetime
     