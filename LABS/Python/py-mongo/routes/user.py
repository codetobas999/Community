from fastapi import APIRouter

from models.user import User
from config.db import db
#from schemas.user import userEntity , usersEntity
from schemas.user import serializeDict , serializeList
from bson import ObjectId

user = APIRouter()
tb_name = 'user'

@user.get('/user')
async def find_all_user():
    #print(conn.user.find())
    #print(usersEntity(conn.user.find()))
    return serializeList(db[tb_name].find())


@user.get('/user/{id}')
async def find_one_user(id): 
    return serializeDict(db[tb_name].find_one({"_id":ObjectId(id)}))

@user.post('/user')
async def create_user(user: User): 
    db[tb_name].insert_one(dict(user))
    return serializeList(db[tb_name].find())

@user.put('/user/{id}')
async def update_user(id,user: User): 
    db[tb_name].find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(db[tb_name].find_one({"_id":ObjectId(id)}))

@user.delete('/user/{id}')
async def delete_user(id):  
    return serializeDict(db[tb_name].find_one_and_delete({"_id":ObjectId(id)}))
