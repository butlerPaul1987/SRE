from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from datetime import datetime
import uvicorn
import json
import subprocess

app = FastAPI()
time_started = datetime.now()


@app.get('/', response_class=HTMLResponse)
def root():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.get('/api/docker-info')
def getDockerInfo():
    result = subprocess.run(
        ["docker", "ps", "-a", "--format", "{{ json . }}"],
        capture_output=True,
        text=True,
        check=True,
    )
    containers = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        containers.append(json.loads(line))
    return containers

@app.post('/api/docker/start/{container_id}')
def start_container(container_id: str):
    try:
        subprocess.run(
            ["docker", "start", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        return {"status": "success", "action": "start", "container_id": container_id}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to start container: {e.stderr}")

@app.post('/api/docker/stop/{container_id}')
def stop_container(container_id: str):
    try:
        subprocess.run(
            ["docker", "stop", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        return {"status": "success", "action": "stop", "container_id": container_id}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to stop container: {e.stderr}")

@app.post('/api/docker/restart/{container_id}')
def restart_container(container_id: str):
    try:
        subprocess.run(
            ["docker", "restart", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        return {"status": "success", "action": "restart", "container_id": container_id}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to restart container: {e.stderr}")

@app.get('/api/docker/logs/{container_id}')
def get_container_logs(container_id: str):
    try:
        result = subprocess.run(
            ["docker", "logs", "--tail", "500", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        return {"logs": result.stdout, "container_id": container_id}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to get container logs: {e.stderr}")

@app.post('/api/docker/remove/{container_id}')
def remove_container(container_id: str):
    try:
        subprocess.run(
            ["docker", "rm", "-f", container_id],
            capture_output=True,
            text=True,
            check=True
        )
        return {"status": "success", "action": "remove", "container_id": container_id}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to remove container: {e.stderr}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)