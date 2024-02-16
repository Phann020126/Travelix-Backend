from pydantic import BaseModel
from time_period_schema import TimePeriod

class Package(BaseModel):
    id : int
    price : float
    description : str
    time_period : TimePeriod
