from pydantic import BaseModel
from typing import List

# Pydantic Schemas
class ProductSchema(BaseModel):
    id: str
    name: str
    description: str

class ProductRecResponse(BaseModel):
    productRecs: List[str]

class ProductDetail(BaseModel):
    id: str
    name: str
    description: str

class ProductDetailsResponse(BaseModel):
    recommendations: List[ProductDetail]
