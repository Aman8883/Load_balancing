from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Response
import httpx


BACKENDS = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    "http://127.0.0.1:8003",
]

current_index = 0


# TODO: Create an HTTPX AsyncClient
@asynccontextmanager
async def lifespan(app : FastAPI):
    async with httpx.AsyncClient(timeout=5.0) as client:
        app.state.client = client
        yield

app = FastAPI(title="Load Balancer", lifespan=lifespan)



@app.get("/")
async def forward_request():
    global  current_index
    backend_url = BACKENDS[current_index]
    current_index = (current_index +1) % len(BACKENDS)
    
    client : httpx.AsyncClient = app.state.client

    try:
        response = await client.get(f"{backend_url}/")
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, 
                            detail=f"Failed to reach backend {backend_url}: {exc}"
                            ) from exc
    return Response(
        content = response.content,
        status_code = response.status_code,
        media_type = response.headers.get("content-type","application/json")
    )    