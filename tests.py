import pytest
from fastapi.exceptions import HTTPException
from pytest import raises
from .methods import (
    sort_opening_hours,
    get_the_day_before,
    get_time,
    fix_next_day_closure,
    divide_into_pairs,
)


def test_sort_opening_hours():
    opening_hours = {
        "monday": [{"type": "close", "value": 2500}, {"type": "open", "value": 1600}],
        "tuesday": [
            {"type": "close", "value": 2300},
            {"type": "open", "value": 1600},
            {"type": "open", "value": 3000},
        ],
        "wednesday": [{"type": "close", "value": 2500}],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    expected = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2300},
            {"type": "open", "value": 3000},
        ],
        "wednesday": [{"type": "close", "value": 2500}],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    actual = sort_opening_hours(opening_hours)
    assert expected == actual


def test_get_the_day_before_1():
    with raises(ValueError):
        get_the_day_before("not_a_day")


def test_get_the_day_before_2():
    expected_1 = "sunday"
    actual_1 = get_the_day_before("monday")
    expected_2 = "tuesday"
    actual_2 = get_the_day_before("wednesday")
    assert expected_1 == actual_1
    assert expected_2 == actual_2


def test_get_time_1():
    expected = "12:00 PM"
    actual = get_time(43200)
    assert expected == actual


def test_get_time_2():
    expected = "01:00 PM"
    actual = get_time(46800)
    assert expected == actual


def test_fix_next_day_closure():
    opening_hours = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 3000},
        ],
        "wednesday": [{"type": "close", "value": 2500}],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    expected = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 3000},
            {"type": "close", "value": 2500},
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    fix_next_day_closure(opening_hours)
    assert expected == opening_hours


def test_divide_into_pairs_1():
    opening_hours = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 3000},
            {"type": "close", "value": 2500},
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    expected = {
        "monday": [({"type": "open", "value": 1600}, {"type": "close", "value": 2500})],
        "tuesday": [
            ({"type": "open", "value": 1600}, {"type": "close", "value": 2500}),
            ({"type": "open", "value": 3000}, {"type": "close", "value": 2500}),
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    divide_into_pairs(opening_hours)
    assert expected == opening_hours


def test_divide_into_pairs_2():
    opening_hours = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 3000},
            {"type": "close", "value": 3500},
        ],
        "wednesday": [{"type": "close", "value": 2500}],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    with raises(HTTPException):
        divide_into_pairs(opening_hours)
