from fastapi import FastAPI

app = FastAPI(title="Docker Desktop K8s Lab")

@app.get("/")
def root():
    return {"msg": "hello from docker-desktop k8s"}

from fastapi import HTTPException

@app.get("/health")
def health():
    raise HTTPException(status_code=500, detail="принудительная ошибка health для демонстрации probes")

@app.post("/crash")
def crash():
    import os
    os._exit(1)

@app.get("/slow")
def slow():
    import time
    time.sleep(20)
    return {"msg": "slow response"}