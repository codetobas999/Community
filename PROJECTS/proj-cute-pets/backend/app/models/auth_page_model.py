from datetime import datetime
from uuid import UUID ,uuid4
from beanie import Document , Indexed  , before_event , Replace , Insert
from pydantic import Field
from .user_model import User

class AuthPage(Document):
    auth_page_id: UUID = Field(default_factory=uuid4, unique=True)
    page_code: Indexed(str)
    menu_name_en: str = None
    menu_name_th: str = None
    icon: str = None
    to: str = None
    status: bool = False 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<AuthPage {self.page_code}>"

    def __str__(self) -> str:
        return self.page_code

    def __hash__(self) -> int:
        return hash(self.page_code)

    def __eq__(self , other: object) -> bool:
        if isinstance(other,AuthPage):
            return self.auth_page_id == other.auth_page_id
        return False
 
    @before_event([Replace,Insert])
    def update_updated_at(self):
        self.updated_at= datetime.utcnow()

    class Collection:
        name = "auth_page"