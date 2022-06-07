#!/usr/bin/env python
from requests import Response

RESPONSE_STRUCTURE = {
    'result': [
        {
            'address': '',
            'calling_code': '',
            'city': '',
            'continent': '',
            'coordinates': '',
            'country': '',
            'country_code': '',
            'state': '',
            'street_name': '',
            'street_number': '',
            'street_suffix': '',
            'zip_code': '',
        }
    ],
    'seed': ''
}


def test_en_address_router(client, setup_test_db):
    with client:
        response: Response = client.get('/v1/en/address')

    ensure_valid_response(response)


def test_ru_address_router(client):
    with client:
        response: Response = client.get('/v1/ru/address')

    ensure_valid_response(response)


def test_en_address_count_param(client):
    with client:
        response: Response = client.get('/v1/en/address?count=2')

    ensure_valid_response(response)
    assert len(response.json()['result']) == 2


def test_ru_address_count_param(client):
    with client:
        response: Response = client.get('/v1/ru/address?count=2')

    ensure_valid_response(response)
    assert len(response.json()['result']) == 2


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/address')

    assert response.status_code == 400


def test_inexistent_route(client):
    with client:
        response: Response = client.get('/v1/en/no_route')

    assert response.status_code == 404


def ensure_valid_response(response: Response):
    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
