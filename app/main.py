from fastapi import FastAPI

app = FastAPI(
    title="Hello FastAPI",
    description="Sample application for AWS EKS deployment",
    version="1.0.0"
)


@app.get("/")
def hello():
    return {
        "message": "Hello World!",
        "application": "FastAPI",
        "environment": "development"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def application_info():
    return {
        "name": "hello-fastapi-eks",
        "version": "1.0.0",
        "technology": "Python FastAPI"
    }