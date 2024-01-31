from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_1():
    body = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 200


def test_2():
    body = {
        "monday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "close", "value": 2500},
        ],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 400


def test_3():
    body = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 422


def test_4():
    body = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 2000},
            {"type": "close", "value": 5000},
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 400


def test_5():
    body = {
        "monday": [{"type": "open", "value": 1600}, {"type": "close", "value": 2500}],
        "tuesday": [
            {"type": "open", "value": 1600},
            {"type": "close", "value": 2500},
            {"type": "open", "value": 3000},
            {"type": "close", "value": 5000},
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 200


def test_6():
    body = {
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
    response = client.post("/opening_hours", json=body)
    assert response.status_code == 200
