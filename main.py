from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
import datetime as dt

app = FastAPI()


class Type(BaseModel):
    type: Literal['open', 'close']
    value: int = Field(lt=86400, gt=-1)


class OpeningHours(BaseModel):
    monday: list[Type] | None
    tuesday: list[Type] | None
    wednesday: list[Type] | None
    thursday: list[Type] | None
    friday: list[Type] | None
    saturday: list[Type] | None
    sunday: list[Type] | None


def get_time(unix_time: int) -> str:
    time = dt.datetime.fromtimestamp(unix_time, dt.timezone.utc)
    return time.strftime("%I:%M %p")



@app.post('/opening_hours')
def add_opening_hours(opening_hours: OpeningHours) -> OpeningHours:  # todo change
    return opening_hours
