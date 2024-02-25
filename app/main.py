import uvicorn
from fastapi import FastAPI
from api.routes import router 
from app.database.database import Base, engine

def create_tables():
    Base.metadata.create_all(bimd=engine)
create_tables()

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)