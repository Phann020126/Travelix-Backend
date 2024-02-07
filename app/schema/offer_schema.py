from pydantic import BaseModel

class Offer(BaseModel):
    id : int
    price : float
    descrpition : str