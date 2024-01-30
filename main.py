import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from methods import (
    sort_opening_hours,
    fix_next_day_closure,
    divide_into_pairs,
    get_schedule,
)
from models import OpeningHours

app = FastAPI()


@app.post("/opening_hours")
async def add_opening_hours(opening_hours: OpeningHours):
    opening_hours_sorted = sort_opening_hours(opening_hours.model_dump())
    fix_next_day_closure(opening_hours_sorted)
    divide_into_pairs(opening_hours_sorted)
    message = get_schedule(opening_hours_sorted)
    return PlainTextResponse(content=message)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
