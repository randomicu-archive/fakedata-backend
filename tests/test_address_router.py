#!/usr/bin/env python
from requests import Response

from tests.utils.constants import ADDRESS_RESPONSE_STRUCTURE
from tests.utils.helpers import check_data
from tests.utils.helpers import check_response
from tests.utils.helpers import check_structure

RESPONSE_STRUCTURE = ADDRESS_RESPONSE_STRUCTURE


def test_en_address_router(client, setup_test_db):
    with client:
        response: Response = client.get('/v1/en/address')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])


def test_ru_address_router(client):
    with client:
        response: Response = client.get('/v1/ru/address')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])


def test_en_address_count_param(client):
    with client:
        response: Response = client.get('/v1/en/address?count=2')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result']

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json[0], expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json[1], expected_structure=RESPONSE_STRUCTURE['result'][0])

    assert len(response.json()['result']) == 2


def test_ru_address_count_param(client):
    with client:
        response: Response = client.get('/v1/ru/address?count=2')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result']

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json[0], expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json[1], expected_structure=RESPONSE_STRUCTURE['result'][0])

    assert len(response.json()['result']) == 2


def test_en_address_seed_param(client):
    seed: str = '1'
    with client:
        response: Response = client.get(f'/v1/en/address?seed={seed}')

    data = {
        'address': '980 Shaw Bay',
        'calling_code': 218,
        'city': 'Lynwood',
        'continent': 'South America',
        'coordinates': dict(longitude=-43.064257, latitude=72.016566),
        'country': 'Antigua & Barbuda',
        'country_code': 'AD',
        'state': 'North Carolina',
        'street_name': 'Tiffany',
        'street_number': 471,
        'street_suffix': 'Trail',
        'zip_code': '60542'
    }

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])

    __validate_seed_data(result_json=result_json, data=data)


def test_en_address_seed_count_param(client):
    seed = '1'
    count = 2
    with client:
        response: Response = client.get(f'/v1/en/address?seed={seed}&count={count}')

    data_first = {
        'address': '980 Shaw Bay',
        'calling_code': 218,
        'city': 'Lynwood',
        'continent': 'South America',
        'coordinates': dict(longitude=-43.064257, latitude=72.016566),
        'country': 'Antigua & Barbuda',
        'country_code': 'AD',
        'state': 'North Carolina',
        'street_name': 'Tiffany',
        'street_number': 471,
        'street_suffix': 'Trail',
        'zip_code': '60542'
    }

    data_second = {
        'address': '1397 Commer Square',
        'calling_code': 1876,
        'city': 'Lake Havasu City',
        'continent': 'Australia',
        'coordinates': dict(longitude=125.20391, latitude=64.901646),
        'country': 'Syria',
        'country_code': 'MR',
        'state': 'Colorado',
        'street_name': 'Bowdoin',
        'street_number': 171,
        'street_suffix': 'Expressway',
        'zip_code': '48721'
    }

    result_raw: dict = response.json()
    result_json_first: dict = response.json()['result'][0]
    result_json_second: dict = response.json()['result'][1]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json_first, expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json_second, expected_structure=RESPONSE_STRUCTURE['result'][0])

    __validate_seed_data(result_json=result_json_first, data=data_first)
    __validate_seed_data(result_json=result_json_second, data=data_second)


def test_ru_address_seed_param(client):
    seed: str = '1467eabc9438489d629c7e6ab1f052ac'
    with client:
        response: Response = client.get(f'/v1/ru/address?seed={seed}')

    data = {
        'address': 'Аллея Кропоткинская 1289',
        'calling_code': 56,
        'city': 'Истра',
        'continent': 'Америка',
        'coordinates': dict(longitude=-117.100362, latitude=-19.217369),
        'country': 'Великобритания',
        'country_code': 'TW',
        'state': 'Приморский край',
        'street_name': 'Русаковская',
        'street_number': 252,
        'street_suffix': 'Аллея',
        'zip_code': '930335'
    }

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])

    __validate_seed_data(result_json=result_json, data=data)


def test_ru_address_seed_count_param(client):
    seed: str = '1467eabc9438489d629c7e6ab1f052ac'
    count = 2
    with client:
        response: Response = client.get(f'/v1/ru/address?seed={seed}&count={count}')

    data_first = {
        'address': 'Аллея Кропоткинская 1289',
        'calling_code': 56,
        'city': 'Истра',
        'continent': 'Америка',
        'coordinates': dict(longitude=-117.100362, latitude=-19.217369),
        'country': 'Великобритания',
        'country_code': 'TW',
        'state': 'Приморский край',
        'street_name': 'Русаковская',
        'street_number': 252,
        'street_suffix': 'Аллея',
        'zip_code': '930335'
    }

    data_second = {
        'address': 'ул. Ремесленная 195',
        'calling_code': 501,
        'city': 'Зима',
        'continent': 'Австралия и Океания',
        'coordinates': dict(longitude=102.671557, latitude=-29.729219),
        'country': 'Шпицберген и Ян-Майен',
        'country_code': 'KN',
        'state': 'Пермский край',
        'street_name': 'Новодевичая',
        'street_number': 1143,
        'street_suffix': 'ул.',
        'zip_code': '825653'
    }

    result_raw: dict = response.json()
    result_json_first: dict = response.json()['result'][0]
    result_json_second: dict = response.json()['result'][1]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json_first, expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json_second, expected_structure=RESPONSE_STRUCTURE['result'][0])

    __validate_seed_data(result_json=result_json_first, data=data_first)
    __validate_seed_data(result_json=result_json_second, data=data_second)


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/address')

    assert response.status_code == 400


def __validate_seed_data(result_json, data):

    check_data(data=data,
               address=result_json['address'],
               calling_code=result_json['calling_code'],
               city=result_json['city'],
               continent=result_json['continent'],
               coordinates=dict(longitude=result_json['coordinates']['longitude'],
                                latitude=result_json['coordinates']['latitude']),
               country=result_json['country'],
               country_code=result_json['country_code'],
               state=result_json['state'],
               street_name=result_json['street_name'],
               street_number=result_json['street_number'],
               street_suffix=result_json['street_suffix'],
               zip_code=result_json['zip_code'])
