from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from database import SessionLocal, ProductDB, create_tables

app = FastAPI(title="E-Commerce API", version="1.0.0")

# Create tables on startup
create_tables()

# Pydantic model for API
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    stock: int
    description: Optional[str] = None

    class Config:
        from_attributes = True

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to E-Commerce API!"}

@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductDB).all()
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = ProductDB(
        name=product.name,
        price=product.price,
        stock=product.stock,
        description=product.description
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated: Product, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = updated.name
    product.price = updated.price
    product.stock = updated.stock
    product.description = updated.description
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": f"Product {product_id} deleted"}

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(products_db):
        if product.id == product_id:
            products_db[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")