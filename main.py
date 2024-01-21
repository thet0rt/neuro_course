import uvicorn
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


def get_the_day_before(current_day):
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    index = day_list.index(current_day) - 1
    return day_list[index]


@app.post('/opening_hours')
def add_opening_hours(opening_hours: OpeningHours):  # todo change
    opening_hours_sorted = {}
    opening_hourse_dict = opening_hours.model_dump()
    for day, time in opening_hourse_dict.items():
        opening_hours_sorted[day] = sorted(time, key=lambda x: x['value']) if time else []

    for day, time_period in opening_hours_sorted.items():
        if not time_period:
            continue
        if time_period[0]['type'] == 'close':
            the_day_before = get_the_day_before(day)
            opening_hours_sorted[the_day_before].append(time_period.pop(0))
    for day, time_period_list in opening_hours_sorted.items():
        if time_period_list:
            opening_hours_sorted[day] = list(zip(*[iter(time_period_list)] * 2))
    message = 'A restaurant is open:\n'
    for day, time_period_list in opening_hours_sorted.items():
        message += f'{get_message(day, time_period_list)}\n'
    print(message)
    return message


def get_message(day, time_list):
    message = f'{day}: '
    if len(time_list) == 0:
        message += 'closed'
        return message
    if len(time_list[-1]) % 2 == 1:
        raise InputError
    for time_period in time_list:
        if not time_period[0]['type'] == 'open':
            raise InputError
        if not time_period[-1]['type'] == 'close':
            raise InputError
        message += f'{get_time(time_period[0]["value"])} - {get_time(time_period[-1]["value"])}, '
    return message[:-2]


class InputError(Exception):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
