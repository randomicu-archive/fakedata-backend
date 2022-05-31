#!/usr/bin/env python
import re

from requests import Response

UUID_REGEX_UPPERCASE = r'[0-9A-F]{8}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{12}'
UUID_REGEX_LOWERCASE = r'[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}'
RESPONSE_STRUCTURE = {
    'result': [
        {
            'uuid': {
                'uuid': '',
                'version': ''
            },
            'uppercase': ''
        }
    ]
}


def test_uuid_router_with_version_4_lowercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=false&version=4')

    ensure_valid_response(response, UUID_REGEX_LOWERCASE, 0)

    assert len(response.json()['result']) == 1


def test_uuid_router_with_version_4_uppercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=true&version=4')

    ensure_valid_response(response, UUID_REGEX_UPPERCASE, 0)

    assert len(response.json()['result']) == 1


def test_uuid_router_count_param_lowercase(client):
    with client:
        response: Response = client.get('/v1/uuid?count=2')

    ensure_valid_response(response, UUID_REGEX_LOWERCASE, 1)

    assert len(response.json()['result']) == 2


def test_uuid_router_count_param_uppercase(client):
    with client:
        response: Response = client.get('/v1/uuid?count=2&uppercase=true')

    ensure_valid_response(response, UUID_REGEX_UPPERCASE, 1)

    assert len(response.json()['result']) == 2


def test_uuid_router_default(client):
    with client:
        response: Response = client.get('/v1/uuid')

    ensure_valid_response(response, UUID_REGEX_LOWERCASE, 0)

    assert len(response.json()['result']) == 1


def test_uuid_router_unsupported_version(client):
    with client:
        response: Response = client.get('/v1/uuid?version=5')

    assert response.status_code == 400

    # A bit of magic happens below: unpacking dict with * returns list of keys so [0] will equal to the first key
    assert [*response.json()][0] == 'detail'
    assert 'Unsupported uuid version. Use version `4` as a query param' == response.json()['detail']


def ensure_valid_response(response: Response, regex_pattern: str, object_number: int):
    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
    assert re.match(regex_pattern,
                    response.json()['result'][object_number]['uuid']['uuid'])
    assert response.json()['result'][object_number]['uuid']['version'] == 4
