from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
        userId: str
        password: str
        firstName: str
        lastName: str
        nickName: str
        email: str
        phone: str 
        role: str
        status: str
        createBy: str
        createDate: datetime
        updateBy: str
        updateDate: datetime        