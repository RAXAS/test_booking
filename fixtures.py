import requests
import pytest
from constant import HEADERS, BASE_URL, AUTH_JSON
from faker import Faker

fake = Faker()


@pytest.fixture(scope="session")
def auth():
    session = requests.Session()

    session.headers.update(HEADERS)
    auth_response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json=AUTH_JSON)
    assert auth_response.status_code == 200, "Auth Error"
    token = auth_response.json().get("token")
    assert token is not None, "Token is None"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture(scope="session")
def unauthorized_session():
    session = requests.Session()
    session.headers.update(HEADERS)  # если HEADERS не содержит токена
    return session

@pytest.fixture()
def booking_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    total_price = fake.random_int(1, 20000)
    deposit_paid = fake.boolean()
    additional_needs = fake.random_element(elements=("Breakfast", "Late Checkout", "Baby crib", ""))
    checkin_date = fake.date_between(start_date="today", end_date="+10d")
    checkout_date = fake.date_between(start_date=checkin_date, end_date="+10d")
    return {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin_date.isoformat(),
            "checkout": checkout_date.isoformat()
        },
        "additionalneeds": additional_needs
    }


@pytest.fixture()
def booking_update_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    total_price = fake.random_int(1, 20000)
    deposit_paid = fake.boolean()
    additional_needs = fake.random_element(elements=("Breakfast", "Late Checkout", "Baby crib", ""))
    checkin_date = fake.date_between(start_date="today", end_date="+10d")
    checkout_date = fake.date_between(start_date=checkin_date, end_date="+10d")
    return {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin_date.isoformat(),
            "checkout": checkout_date.isoformat()
        },
        "additionalneeds": additional_needs
    }
