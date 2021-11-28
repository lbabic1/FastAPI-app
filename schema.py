from pydantic import BaseModel

class Player(BaseModel):
    name: str
    date_of_birth: str
    position: str
    club_id: int

    class Config:
        orm_mode=True

class Club(BaseModel):
    name: str
    country: str

    class Config:
        orm_mode=True