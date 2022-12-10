from app.models.auth_group_model import AuthGroup  
from app.models.page_model import Page  

class AuthGroupService:
    @staticmethod
    async def list_authen_by_group(user_code):         
        print("list_authen_by_group 2" + user_code)  
        stage_lookup_AuthUser = {
                "$lookup": {
                    "from": "AuthUserGroup", 
                    "let": {"groupCode":"$group_code"},  
                    "pipeline": [{
                            "$match": {
                                "$expr": {
                                    "$and": [
                                            { "$eq": ["$group_code", "$$groupCode"]}, 
                                            { "$eq": ["$user_code", user_code]}
                                    ]            
                                }
                            }
                    }],
                    "as": "group"
                 }
        }

        stage_lookup_AuthPage = {
                "$lookup": {
                    "from": "AuthPage", 
                    "let": {"pageCode":"$page_code"},  
                    "pipeline": [{
                            "$match": {
                                "$expr": {
                                    "$and": [
                                        { "$eq": ["$page_code", "$$pageCode"]}, 
                                        { "$eq": ["$status", True]}
                                    ]            
                                }
                            }
                    }],
                    "as": "page"
                 }
        }
        stage_lookup_AuthPageSub = {
                "$lookup": {
                    "from": "AuthPageSub", 
                    "let": {"pageCode":"$page_code" , "pageSubCode":"$page_sub_code" }, 
                    "pipeline": [{
                            "$match": {
                                "$expr": {
                                    "$and": [
                                        { "$eq": ["$page_code", "$$pageCode"]},
                                        { "$in": ["$page_sub_code", "$$pageSubCode"]},
                                        { "$eq": ["$status", True]}
                                    ]            
                                }
                            }
                    }],
                    "as": "page_subs"
                 }
        }
        
        stage_hide_fiels = { "$unset": [ "_id" , "group_code" ,"page_code" ,"page_sub_code" ,"status", "page._id", "page_subs._id"    ] }                
        stage_unarray_page = { "$unwind": "$page" }
        stage_unarray_group = { "$unwind": "$group" }
        stage_field_filter = { "$project" : { "_id": 0 , "group._id": 0 , "pages._id": 0 , "page_subs._id": 0 }  } #hide Column
        pipeline = [
            stage_lookup_AuthUser,
            stage_unarray_group,
            stage_lookup_AuthPage,
            stage_unarray_page,
            stage_lookup_AuthPageSub, 
            stage_field_filter,
            stage_hide_fiels, 
        ]
 
        todos= AuthGroup.aggregate(pipeline)
        return await todos.to_list()
