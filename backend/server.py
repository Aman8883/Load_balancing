import os
import asyncio
from fastapi import FastAPI

SERVER_NAME = os.getenv("SERVER_NAME","server-1")
SERVER_PORT = int(os.getenv("SERVER_PORT","8001"))

app = FastAPI(title=SERVER_NAME)

@app.get("/")
async def root():
    return {
        "server" : SERVER_NAME,
        "port" : SERVER_PORT,
        "message" : "Request Processed Successfully",
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "server": SERVER_NAME,
        "port" : SERVER_PORT,
    }

@app.get("/slow")
async def slow():
    await asyncio.sleep(2)
    return {
        "server" : SERVER_NAME,
        "port" : SERVER_PORT,
        "message" : "Slow request processed successfully",
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.server:app", host="0.0.0.0", port=SERVER_PORT, reload=False)