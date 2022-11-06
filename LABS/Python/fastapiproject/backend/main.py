from fastapi import FastAPI
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware
from database.connection import Settings
from routes.users import user_router

app = FastAPI()
settings = Settings()

# register origins

origins = [
    "*",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Register Router
app.include_router(user_router, prefix="/user")
 
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
 

@app.get("/")
async def home():
    return {"message","Welcom to FastAPI"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)