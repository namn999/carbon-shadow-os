from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scheduler import optimize_task

app = FastAPI()

# Allow browser to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/optimize")
def optimize(runtime: int, deadline: int):
    return optimize_task(runtime, deadline)
