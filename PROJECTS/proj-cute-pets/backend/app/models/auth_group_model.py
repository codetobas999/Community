from beanie import Document 

class AuthGroup(Document):
  
    class Collection:
        name = "auth_group"