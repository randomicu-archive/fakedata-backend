#!/usr/bin/env python
from requests import Response

from tests.constants import ADDRESS_RESPONSE_STRUCTURE


RESPONSE_STRUCTURE = ADDRESS_RESPONSE_STRUCTURE


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


def test_en_address_seed_param(client):
    with client:
        response: Response = client.get('/v1/en/address?seed=1')

    address = '980 Shaw Bay'
    calling_code = 218
    city = 'Lynwood'
    continent = 'South America'
    coordinates = dict(longitude=-43.064257, latitude=72.016566)
    country = 'Antigua & Barbuda'
    country_code = 'AD'
    state = 'North Carolina'
    street_name = 'Tiffany'
    street_number = 471
    street_suffix = 'Trail'
    zip_code = '60542'

    ensure_valid_response(response)

    assert response.json()['result'][0]['address'] == address
    assert response.json()['result'][0]['calling_code'] == calling_code
    assert response.json()['result'][0]['city'] == city
    assert response.json()['result'][0]['continent'] == continent
    assert response.json()['result'][0]['coordinates']['longitude'] == coordinates['longitude']
    assert response.json()['result'][0]['coordinates']['latitude'] == coordinates['latitude']
    assert response.json()['result'][0]['country'] == country
    assert response.json()['result'][0]['country_code'] == country_code
    assert response.json()['result'][0]['state'] == state
    assert response.json()['result'][0]['street_name'] == street_name
    assert response.json()['result'][0]['street_number'] == street_number
    assert response.json()['result'][0]['street_suffix'] == street_suffix
    assert response.json()['result'][0]['zip_code'] == zip_code


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
