#!/usr/bin/env python
import pytest
from requests import Response

from tests.constants import ADDRESS_RESPONSE_STRUCTURE

pytestmark = pytest.mark.parametrize(
    "param,expected",
    [
        ("address", "test_address"),
        ("calling_code", 111),
        ("city", "test_city"),
        ("continent", "test_continent"),
        ("country", "test_country"),
        ("country_code", "test_country_code"),
        ("state", "test_state"),
        ("street_name", "test_street_name"),
        ("street_number", 444),
        ("street_suffix", "test_street_suffix"),
    ]
)


RESPONSE_STRUCTURE = ADDRESS_RESPONSE_STRUCTURE


def test_en_address_router_with_params(param, expected, client):
    with client:
        response: Response = client.get(f'/v1/en/address?{param}={expected}')

    ensure_valid_response(response)
    assert response.json()['result'][0][param] == expected


def test_ru_address_router_with_params(param, expected, client):
    with client:
        response: Response = client.get(f'/v1/ru/address?{param}={expected}')

    ensure_valid_response(response)
    assert response.json()['result'][0][param] == expected


def ensure_valid_response(response: Response):
    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
