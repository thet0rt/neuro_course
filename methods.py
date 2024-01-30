import datetime as dt

from fastapi import HTTPException


def get_time(unix_time: int) -> str:
    time = dt.datetime.fromtimestamp(unix_time, dt.timezone.utc)
    return time.strftime("%I:%M %p")


def get_the_day_before(current_day):
    day_list = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    index = day_list.index(current_day) - 1
    return day_list[index]


def sort_opening_hours(opening_hours: dict) -> dict:
    """
    Сортирует списки словарей по параметру value
    (по времени)
    :param opening_hours: dict
    :return: dict
    """
    opening_hours_sorted = {}
    for day, time in opening_hours.items():
        opening_hours_sorted[day] = (
            sorted(time, key=lambda x: x["value"]) if time else []
        )
    return opening_hours_sorted


def fix_next_day_closure(opening_hours: dict) -> None:
    """
    Переносит закрытие следующим днем в день открытия
    :param opening_hours: dict
    :return: dict
    """
    for day, time_period in opening_hours.items():
        if not time_period:
            continue
        if time_period[0]["type"] == "close":
            the_day_before = get_the_day_before(day)
            opening_hours[the_day_before].append(time_period.pop(0))


def divide_into_pairs(opening_hours: dict) -> None:
    """
    Разбивает по периодам работы - open-close, open-close
    :param opening_hours: dict
    :return: dict
    """
    for day, time_period_list in opening_hours.items():
        if time_period_list:
            if len(time_period_list) % 2 == 1:
                raise HTTPException(status_code=400, detail="Bad request")
            time_period_list_sorted = list(zip(*[iter(time_period_list)] * 2))
            opening_hours[day] = time_period_list_sorted


def get_schedule(opening_hours: dict) -> str:
    """
    Makes schedule
    :param opening_hours: dict
    :return: str
    """
    message = "A restaurant is open:\n"
    for day, time_period_list in opening_hours.items():
        message += f"{get_message(day, time_period_list)}\n"
    return message


def get_message(day, time_list):
    message = f"{day}: "
    if len(time_list) == 0:
        message += "closed"
        return message
    for time_period in time_list:
        if not time_period[0]["type"] == "open":
            raise HTTPException(status_code=400, detail="Bad request")
        if not time_period[-1]["type"] == "close":
            raise HTTPException(status_code=400, detail="Bad request")
        message += f'{get_time(time_period[0]["value"])} - {get_time(time_period[-1]["value"])}, '
    return message[:-2]
