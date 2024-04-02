import subprocess
from fastapi import FastAPI

app = FastAPI(
    title="Robot"
)
is_working = False

@app.get("/robot")
def robot_start(value: int = 0):
    global is_working
    if not is_working:
        global robot
        robot = subprocess.Popen(['python', 'robot.py', str(value)])
        is_working = True
        return "The robot has started working"
    else:
        robot.terminate()
        is_working = False
        return "The robot has stoped working"
