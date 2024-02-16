from pydantic import BaseModel

class Agency(BaseModel):
    id : int
    name : str
    address : str
    fax_number : int
    email : str