from database import Base
from sqlalchemy import create_engine, Column, String, Text

class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)

class ProductRecommendation(Base):
    __tablename__ = "product_recommendations"
    model_name = Column(String, primary_key=True)
    list_of_recs = Column(Text, nullable=False)