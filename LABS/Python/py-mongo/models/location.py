from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
        locationId: str
        locationName: str
        addr1: str
        addr2: str
        addr3: str
        district: str #ตำบล
        amphoe: str #อำเภอ
        province: str #จังหวัด
        zipcode: str  #รหัสไปรษณี
        status: str
        createBy: str
        createDate: datetime
        updateBy: str
        updateDate: datetime 
