#!/usr/bin/env python
from requests import Response

from app.responses.address import get_country_code

EN_LOCALE_COUNTRY_CODE = 'us'
RU_LOCALE_COUNTRY_CODE = 'ru'


def test_en_address_router(client, setup_test_db):
    with client:
        response: Response = client.get('/v1/en/address')

    response_structure = {
        'address': '',
        'calling_code': '',
        'city': '',
        'continent': '',
        'coordinates': '',
        'country': '',
        'country_code': get_country_code(language='en') == EN_LOCALE_COUNTRY_CODE,
        'latitude': '',
        'longitude': '',
        'postal_code': '',
        'state': '',
        'street_name': '',
        'street_number': '',
        'street_suffix': '',
        'zip_code': '',
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()


def test_ru_address_router(client):
    with client:
        response: Response = client.get('/v1/ru/address')

    response_structure = {
        'address': '',
        'calling_code': '',
        'city': '',
        'continent': '',
        'coordinates': '',
        'country': '',
        'country_code': get_country_code(language='ru') == RU_LOCALE_COUNTRY_CODE,
        'latitude': '',
        'longitude': '',
        'postal_code': '',
        'state': '',
        'street_name': '',
        'street_number': '',
        'street_suffix': '',
        'zip_code': '',
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/address')

    assert response.status_code == 400


def test_inexistent_route(client):
    with client:
        response: Response = client.get('/v1/en/no_route')

    assert response.status_code == 404
