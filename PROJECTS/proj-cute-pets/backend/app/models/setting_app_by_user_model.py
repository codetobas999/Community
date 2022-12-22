from datetime import datetime
from uuid import UUID ,uuid4
from beanie import Document , Indexed  , before_event , Replace , Insert
from pydantic import Field

class SettingAppByUser(Document):
    setting_app_by_user_id: UUID = Field(default_factory=uuid4, unique=True)
    user_code: Indexed(str)
    language: str = None
    theme: str = None
    show_page: int = None
    token_age: int = None
    status: bool = False 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<SettingAppByUser {self.user_code}>"

    def __str__(self) -> str:
        return self.user_code

    def __hash__(self) -> int:
        return hash(self.user_code)

    def __eq__(self , other: object) -> bool:
        if isinstance(other,SettingAppByUser):
            return self.setting_app_by_user_id == other.setting_app_by_user_id
        return False
 
    @before_event([Replace,Insert])
    def update_updated_at(self):
        self.updated_at= datetime.utcnow()

    class Collection:
        name = "setting_app_by_user"