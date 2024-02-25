from fastapi import APIRouter

from app.api.endpoints.agency import router as agency_router

routers = APIRouter()

routers.include_router(agency_router)