from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import json
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/getProductRecommendations", response_model=schemas.ProductRecResponse)
def get_product_recommendations(modelname: str, db: Session = Depends(get_db)):
    entry = db.query(models.ProductRecommendation).filter_by(model_name=modelname).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Model not found")
    return {"productRecs": json.loads(entry.list_of_recs)}

@router.get("/getProductRecommendationDetails", response_model=schemas.ProductDetailsResponse)
def get_product_details(modelname: str, db: Session = Depends(get_db)):
    entry = db.query(models.ProductRecommendation).filter_by(model_name=modelname).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Model not found")
    ids = json.loads(entry.list_of_recs)
    products = db.query(models.Product).filter(models.Product.id.in_(ids)).all()
    return {"recommendations": [schemas.ProductDetail(id=p.id, name=p.name, description=p.description) for p in products]}

@router.put("/addProduct")
def add_product(product: schemas.ProductSchema, db: Session = Depends(get_db)):
    if not product.id or not product.name or not product.description:
        raise HTTPException(status_code=400, detail="All fields are required")
    if db.query(models.Product).filter_by(id=product.id).first():
        raise HTTPException(status_code=400, detail="Product ID already exists")
    db.add(models.Product(**product.dict()))
    db.commit()
    return {"message": "Product added successfully"}
