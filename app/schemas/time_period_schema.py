from pydantic import BaseModel
from datetime import datetime

class TimePeriod(BaseModel):
    begins : datetime
    ends : datetime