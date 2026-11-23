# Python Load Balancer

A hands-on implementation of a Layer 7 HTTP load balancer using Python, FastAPI and HTTPX.

The project explores how incoming HTTP traffic can be distributed across multiple backend servers, how reverse proxies work, and how load balancing algorithms affect application performance and reliability.

## Architecture

```text
                  Client
                    |
                    v
           Load Balancer (:8000)
                    |
             Routing Algorithm
              (Round Robin)
                    |
          +---------+---------+
          |         |         |
          v         v         v
      Server 1  Server 2  Server 3
       :8001     :8002     :8003
```

The client communicates with a single entry point. The load balancer forwards incoming requests to one of the available backend servers.

## Tech Stack

- Python
- FastAPI
- HTTPX
- Uvicorn
- AsyncIO

## Current Features

- Multiple independent FastAPI backend servers
- HTTP request forwarding using HTTPX
- Reverse proxy implementation
- Asynchronous HTTP client with connection pooling
- Round Robin load balancing
- Backend connection error handling
- Basic backend health endpoint
- Slow endpoint for testing concurrent requests

## Project Structure

```text
python-load-balancer/
├── backend/
│   ├── __init__.py
│   └── server.py
├── load_balancer/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-load-balancer.git
cd python-load-balancer
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend servers

Open three separate terminals.

**Server 1**
```bash
SERVER_NAME=server-1 SERVER_PORT=8001 \
uvicorn backend.server:app --port 8001
```

**Server 2**
```bash
SERVER_NAME=server-2 SERVER_PORT=8002 \
uvicorn backend.server:app --port 8002
```

**Server 3**
```bash
SERVER_NAME=server-3 SERVER_PORT=8003 \
uvicorn backend.server:app --port 8003
```

### 5. Start the load balancer

Open another terminal:

```bash
uvicorn load_balancer.main:app --port 8000
```

The load balancer is now available at:

`http://localhost:8000`

## Testing

Send a request:

```bash
curl http://localhost:8000/
```

Send multiple requests to observe Round Robin distribution:

```bash
for i in {1..9}; do
    curl -s http://localhost:8000/
    echo
done
```

Generate concurrent traffic:

```bash
seq 1 100 | xargs -P 20 -I {} \
curl -s http://localhost:8000/
```

## Learning Roadmap

The following features are planned:

- [x] Multiple backend servers
- [x] Reverse proxy
- [x] Round Robin algorithm
- [ ] Concurrent traffic benchmarking
- [ ] Least Connections algorithm
- [ ] Weighted Round Robin
- [ ] Active backend health monitoring
- [ ] Automatic failover
- [ ] Request latency and throughput metrics
- [ ] Sticky sessions / IP Hash
- [ ] Rate limiting
- [ ] Docker containerization
- [ ] Horizontal backend scaling
- [ ] Redis-based shared state for multi-worker coordination

## Motivation

This project is being developed as a practical exploration of backend infrastructure and system design.

Rather than treating load balancing as a theoretical concept, the goal is to implement the underlying mechanisms, generate traffic, simulate failures, and understand how real backend systems distribute workloads.

More features and experiments will be added incrementally.