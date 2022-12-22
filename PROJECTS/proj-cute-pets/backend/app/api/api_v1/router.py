from fastapi import APIRouter 
from app.api.api_v1.handlers import user , todo ,page,permission_user ,auth_user_group ,auth_page , auth_page_sub , setting_app_by_user
from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(user.user_router,prefix='/users',tags=["users"])
router.include_router(todo.todo_router,prefix='/todo',tags=["todo"])
router.include_router(auth_router,prefix='/auth',tags=["auth"])

router.include_router(page.page_router,prefix='/page',tags=["page"])

router.include_router(auth_page.auth_page_router,prefix='/auth_page',tags=["auth_page"])
router.include_router(auth_page_sub.auth_page_sub_router,prefix='/auth_page_sub',tags=["auth_page_sub"])
router.include_router(auth_user_group.auth_user_group_router,prefix='/auth_user_group',tags=["auth_user_group"])
router.include_router(permission_user.permission_user_router,prefix='/permission_user',tags=["permission_user"])
router.include_router(setting_app_by_user.setting_app_by_user_router,prefix='/setting_app_by_user',tags=["setting_app_by_user"])