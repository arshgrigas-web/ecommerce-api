from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from app.database import engine, Base
from app.routers import auth, products, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="Real e-commerce platform",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
ORDER_COUNT = Counter('orders_total', 'Total orders placed')
PAYMENT_SUCCESS = Counter('payments_success_total', 'Successful payments')
PAYMENT_FAILED = Counter('payments_failed_total', 'Failed payments')

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/', status='200').inc()
    return {"message": "E-Commerce API v2.0", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)