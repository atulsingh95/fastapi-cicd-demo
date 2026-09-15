from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")


@app.get("/")
def hello_world():
    return {
        "message": "Hello Atul",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }