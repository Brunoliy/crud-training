from sqlalchemy import Column, Integer, String
from database import Base


# Create a class that represents the table in the database
class User(Base): 
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    email: str = Column(String, unique=True, index=True)
    cpf: str = Column(String, unique=True, index=True)
    phone: str = Column(String, index=True)
    address: str = Column(String, index=True)
    profession: str = Column(String, index=True)
    description: str = Column(String, index=True)
