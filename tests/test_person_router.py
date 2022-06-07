#!/usr/bin/env python
from requests import Response

RESPONSE_STRUCTURE = {
    'result': [
        {
            'age': '',
            'email': '',
            'first_name': '',
            'full_name': '',
            'gender': '',
            'height': '',
            'identifier': '',
            'last_name': '',
            'nationality': '',
            'occupation': '',
            'password': '',
            'political_views': '',
            'telephone': '',
            'title': '',
            'university': '',
            'username': '',
            'weight': '',
            'work_experience': ''
        }
    ],
    'seed': ''
}


def test_en_person_router(client):
    with client:
        response: Response = client.get('/v1/en/person')

    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()


def test_ru_person_router(client):
    with client:
        response: Response = client.get('/v1/ru/person')

    ru_response_structure = {**RESPONSE_STRUCTURE}

    ru_response_structure['result'][0]['patronymic'] = ''
    ru_response_structure['result'][0]['inn'] = ''
    ru_response_structure['result'][0]['kpp'] = ''
    ru_response_structure['result'][0]['bic'] = ''
    ru_response_structure['result'][0]['ogrn'] = ''
    ru_response_structure['result'][0]['passport'] = ''

    assert response.status_code == 200
    assert ru_response_structure.keys() == response.json().keys()


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/person')
    assert response.status_code == 400
