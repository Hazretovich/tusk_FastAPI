import sqlite3
import subprocess
from datetime import datetime

import uvicorn
from fastapi import FastAPI

from models import WorkingData

app = FastAPI(
    title="Robot"
)

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


@app.get("/robot/working_info")
def working_info():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """SELECT * FROM robot_working_info;"""
        cursor.execute(query)
        return {"datas": [{"begin_time": res[0],
                           "work_duration": res[1],
                           "start_value": res[2]} for res in cursor]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
