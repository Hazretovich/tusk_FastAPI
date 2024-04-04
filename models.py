from datetime import datetime

from pydantic import BaseModel


class WorkingData(BaseModel):
    begin_time: datetime
    work_duration: datetime
    start_value: int
