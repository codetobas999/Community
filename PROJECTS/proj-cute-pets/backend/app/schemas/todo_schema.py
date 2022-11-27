from datetime import datetime
from pydantic import BaseModel , Field
from uuid import UUID
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(...,title='Title',min_length=1 ,max_length=55)
    description: str = Field(...,title='Title',min_length=1 ,max_length=755)
    todo_date: str = Field(...,title='Title',min_length=1 ,max_length=10)
    status: Optional[bool] = False 


class TodoUpdate(BaseModel):
    title: Optional[str]  = Field(...,title='Title',min_length=1 ,max_length=55)
    description: Optional[str]  = Field(...,title='Title',min_length=1 ,max_length=755)
    todo_date: Optional[str] = Field(...,title='Title',min_length=1 ,max_length=10)
    status: Optional[bool] = False 

class TodoOut(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    todo_date: str
    created_at: datetime
    updated_at: datetime
     