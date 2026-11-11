from fastapi import FastAPI, Request
import time

app = FastAPI()
request_logs = []
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    log = {
        "method": request.method,
        "path": request.url.path,
        "ip": request.client.host,
        "status_code": response.status_code,
        "response_time": process_time
    }
    request_logs.append(log)
    print(log)
    return response

@app.get("/")
def home():
    return {
        "message": "API Security Monitor is running!"
    }

@app.get("/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"},
            {"id": 3, "name": "Keyboard"}
        ]
    }

@app.post("/login")
def login():
    return {
        "message": "Login endpoint reached"
    }
    
@app.get("/security/logs")
def get_logs():
    return {
        "total_requests": len(request_logs),
        "logs": request_logs
    }