from datetime import datetime
from uuid import UUID ,uuid4
from beanie import Document , Indexed  , before_event , Replace , Insert
from pydantic import Field
from .user_model import User

class AuthUserGroup(Document):
    auth_user_id: UUID = Field(default_factory=uuid4, unique=True)
    user_code: Indexed(str)
    group_code: str = None
    status: bool = False 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<AuthUserGroup {self.user_code}>"

    def __str__(self) -> str:
        return self.user_code

    def __hash__(self) -> int:
        return hash(self.user_code)

    def __eq__(self , other: object) -> bool:
        if isinstance(other,AuthUserGroup):
            return self.auth_user_id == other.auth_user_id
        return False
 
    @before_event([Replace,Insert])
    def update_updated_at(self):
        self.updated_at= datetime.utcnow()

    class Collection:
        name = "auth_user_group"