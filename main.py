from fastapi import FastAPI

app = FastAPI()

@app.get("/robot_start")
def start():
    return "initial"