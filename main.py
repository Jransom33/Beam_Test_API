from fastapi import FastAPI
import uvicorn
from datetime import datetime

app = FastAPI(title="Beam Test API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    """Event handler that runs on application startup"""
    print(f"🚀 Application started at {datetime.now()}")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Beam Test API"}


@app.get("/health/detailed")
async def detailed_health_check():
    """Detailed health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Beam Test API",
        "version": "1.0.0",
        "uptime": "running"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
