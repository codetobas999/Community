from fastapi import APIRouter

from models.location import Location
from config.db import db 
from schemas.location import serializeDict , serializeList
from bson import ObjectId

location = APIRouter()
tb_name = 'location'

@location.get('/location')
async def find_all_location(): 
    return serializeList(db[tb_name].find())


@location.get('/location/{id}')
async def find_one_location(id): 
    return serializeDict(db[tb_name].find_one({"_id":ObjectId(id)}))

@location.post('/location/')
async def create_location(location: Location): 
    db[tb_name].insert_one(dict(location))
    return serializeList(db[tb_name].find())

@location.put('/location/{id}')
async def update_location(id,location: Location): 
    db[tb_name].find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(location)
    })
    return serializeDict(db[tb_name].find_one({"_id":ObjectId(id)}))

@location.delete('/location/{id}')
async def delete_location(id):  
    return serializeDict(db[tb_name].find_one_and_delete({"_id":ObjectId(id)}))
