import sqlite3
import subprocess
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Robot"
)


class WorkingData(BaseModel):
    begin_time: datetime
    work_duration: datetime
    start_value: int


data = WorkingData
is_working = False


@app.get("/robot")
def robot_start(value: int = 0):
    with sqlite3.connect('db/database.db') as db:
        global is_working
        cursor = db.cursor()
        if not is_working:
            global robot
            robot = subprocess.Popen(['python', 'robot.py', str(value)])
            global data
            data.begin_time = datetime.now()
            data.start_value = value
            is_working = True
            return "The robot has started working"
        else:
            robot.terminate()
            data.work_duration = datetime.now() - data.begin_time
            query = """INSERT INTO robot_working_info(begin_time, work_duration, start_value) VALUES (?, ?, ?)"""
            cursor.execute(query, (str(data.begin_time), str(data.work_duration), data.start_value))
            is_working = False
            return "The robot has stoped working"
