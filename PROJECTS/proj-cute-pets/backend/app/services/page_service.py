from app.models.user_model import User
from app.models.page_model import Page 

class PageService:
    @staticmethod
    async def list_pages(user: User):  
        #pipeline = [{'$group': { "_id": "$page_code" }}] 
        #todos= Page.aggregate(pipeline) 
        stage_lookup = {
                "$lookup": {
                    "from": "PageSub", 
                    "localField": "page_code", 
                    "foreignField": "page_code", 
                    "as": "pages",
                 }
        }
        stage_limit = { "$limit": 20 }
        stage_field_filter = { "$project" : { "_id": 0, "pages._id": 0 }  } #hide Column
        stage_row_filter = {'$match': {'status': True}}
        pipeline = [
            stage_lookup,
            stage_limit,
            stage_field_filter,
            stage_row_filter
        ]
 
        todos= Page.aggregate(pipeline)
        
        return await todos.to_list()
 

        '''
        pages = await Page.aggregate([{'$lookup': {
                                        'from': 'auth_sub_page',
                                        'localField': 'page_code',
                                        'foreignField': 'page_code',
                                        'as': 'pages'
                                    }
                                    }]).to_list()
        return pages
        '''
'''
    @staticmethod
    async def list_todos(user: User)-> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos
         

    @staticmethod
    async def create_todo(user: User, data: TodoCreate)-> Todo: 
        todo = Todo(**data.dict(), owner=user)
        return await todo.insert()        

    @staticmethod
    async def retrieve_todo(current_user: User, todo_id: UUID): 
        todo = await Todo.find_one(Todo.todo_id == todo_id ,Todo.owner.id == current_user.id)
        return todo

    @staticmethod
    async def update_todo(current_user: User, todo_id: UUID ,data: TodoUpdate): 
        todo = await TodoService.retrieve_todo(current_user,todo_id)
        await todo.update({"$set": data.dict(exclude_unset=True)})
        await todo.save()
        return todo   

    @staticmethod
    async def delete_todo(current_user: User, todo_id: UUID)-> None:
        todo = await TodoService.retrieve_todo(current_user,todo_id)
        if todo:
            await todo.delete() 
        return None         
'''    