from sqlalchemy import Column,Integer,String,Boolean
from config.database import Base

class Book(Base):
    __tablename__ ="books"

    id = Column(Integer,primary_key=True,index=True)
    title= Column(String, nullable=False)
    auther = Column(String, nullable=False)
    available = Column(Boolean, default=True)

 

