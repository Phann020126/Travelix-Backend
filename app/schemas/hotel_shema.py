from pydantic import BaseModel

class Hotel(BaseModel):
    id : int
    name : str
    address : str
    category : int