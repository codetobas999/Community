from fastapi import APIRouter 
from app.api.api_v1.handlers import user , todo ,page,auth_group
from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(user.user_router,prefix='/users',tags=["users"])
router.include_router(todo.todo_router,prefix='/todo',tags=["todo"])
router.include_router(auth_router,prefix='/auth',tags=["auth"])

router.include_router(page.page_router,prefix='/page',tags=["page"])
router.include_router(auth_group.auth_group_router,prefix='/auth_group',tags=["auth_group"])