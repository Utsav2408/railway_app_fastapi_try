from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Railway FastAPI App",
    description="A simple FastAPI application deployed on Railway",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to FastAPI on Railway!",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "fastapi-railway"
        }
    )


@app.get("/api/hello/{name}")
async def hello_name(name: str):
    """Greet a user by name"""
    return {
        "message": f"Hello, {name}!",
        "endpoint": "/api/hello/{name}"
    }


@app.get("/api/info")
async def get_info():
    """Get application information"""
    return {
        "app_name": "Railway FastAPI App",
        "version": "1.0.0",
        "framework": "FastAPI",
        "deployment": "Railway"
    }
