from pydantic import BaseModel

class BookCreate(BaseModel):

    title :str
    auther :str
    available :bool =True

class BookResponse(BookCreate):
    id :int

    class config:
        orm_mode = True
        