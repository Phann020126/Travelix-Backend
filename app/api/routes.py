from fastapi import APIRouter

from api.endpoints.user import router as user_router

routers = APIRouter()

user_router.tags = routers.tags.append("v1")
routers.include_router(user_router)