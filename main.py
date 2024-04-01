import subprocess

from fastapi import FastAPI

app = FastAPI(
    title="Robot"
)

@app.get("/robot/start")
def robot_start(value: int = 0):
    global robot
    robot = subprocess.Popen(['python', 'robot.py', str(value)])
    return "The robot has started working"

#
@app.get("/robot/stop")
def robot_stop():
    robot.terminate()
    return "The robot has stoped working"
