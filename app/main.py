from fastapi import FastAPI
import uvicorn
from app.database.database import Base, engine

def create_tables():
    Base.metadata.create_all(bimd=engine)
create_tables()

app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)