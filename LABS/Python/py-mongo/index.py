from fastapi import FastAPI
from routes.user import user
from routes.location import location

app = FastAPI()    
app.include_router(user)
app.include_router(location) 

 