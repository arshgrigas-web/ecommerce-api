from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.database import engine, Base
from app.routers import auth, products, orders

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="Real e-commerce platform with users, products, orders and payments",
    version="2.0.0"
)

# Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Include routers
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message": "E-Commerce API v2.0", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}