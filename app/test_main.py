import datetime
import pytest
from typing import Callable, List
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture
def products() -> List[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today,expected_result",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 1, 31), []),
        (datetime.date(2022, 2, 1), [])
    ],
    ids=[
        "should return outdated products if today is past expiry date",
        "should return empty list if no outdated products",
        "should not return product with today's expiration date"
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: Callable,
        products: List[dict],
        today: tuple,
        expected_result: List[str]
) -> None:
    mock_date.today.return_value = today
    assert outdated_products(products) == expected_result
