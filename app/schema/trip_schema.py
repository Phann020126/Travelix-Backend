from pydantic import BaseModel
from datetime import datetime

class Trip(BaseModel):
    id : int
    pickup_date : datetime
    pickup_place : str
    pickup_weekday : str
    return_date : datetime
    return_place : str
    return_weekday : str
    price : float