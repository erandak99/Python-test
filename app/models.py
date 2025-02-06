from sqlalchemy import Column, Integer, String, Float, JSON
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    image = Column(String, nullable=False)
    rating = Column(JSON, nullable=False)