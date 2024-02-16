from pydantic import BaseModel

class TouristType(BaseModel):
    name : str

    
class Tourist(BaseModel):
    id : int
    name : str
    nationality : str
    type : TouristType
    