from app.models.auth_group_model import AuthGroup  
from app.models.page_model import Page  

class AuthGroupService:
    @staticmethod
    async def list_authen_by_group(group_code):         
        print("list_authen_by_group 2" + group_code)  
        stage_row_filter1 = {'$match': {'group_code':{"$in":[group_code]}}}
        stage_lookup2 = {
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
        stage_lookup3 = {
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
        
        stage_unset4 = { "$unset": [ "_id" , "group_code" ,"page_code" ,"page_sub_code" ,"status", "page._id", "page_subs._id"    ] }                
        stage_unwind5 = { "$unwind": "$page" }

        stage_limit = { "$limit": 20 }
        stage_field_filter = { "$project" : { "_id": 0, "pages._id": 0 , "page_subs._id": 0 }  } #hide Column
        stage_row_filter = {'$match': {'status': True}}
        pipeline = [
            stage_row_filter1,
            stage_lookup2,
            stage_unwind5,
            stage_lookup3,
            #stage_limit, 
            stage_field_filter,
            stage_unset4,
            
            #stage_row_filter
        ]
 
        todos= AuthGroup.aggregate(pipeline)
        return await todos.to_list()

        '''
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