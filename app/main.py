from fastapi import FastAPI

from routes.vendor_routes import router as vendor_router

app = FastAPI(
    title="ShopSense API",
    description="Multi-Vendor E-Commerce Analytics Platform",
    version="0.1.0",
)

app.include_router(vendor_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}