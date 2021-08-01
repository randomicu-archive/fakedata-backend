#!/usr/bin/env python
import re

from requests import Response

UUID_REGEX_UPPERCASE = r'[0-9A-F]{8}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{12}'

UUID_REGEX_LOWERCASE = r'[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}'

RESPONSE_STRUCTURE = {
    'uuid': {
        'uuid': '',
        'version': ''
    },
    'uppercase': ''
}


def test_uuid_router_with_version_4_lowercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=false&version=4')

    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
    assert re.match(UUID_REGEX_LOWERCASE,
                    response.json()['uuid']['uuid'])
    assert response.json()['uuid']['version'] == 4


def test_uuid_router_with_version_4_uppercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=true&version=4')

    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
    assert re.match(UUID_REGEX_UPPERCASE,
                    response.json()['uuid']['uuid'])
    assert response.json()['uuid']['version'] == 4


def test_uuid_router_default(client):
    with client:
        response: Response = client.get('/v1/uuid')

    assert response.status_code == 200
    assert RESPONSE_STRUCTURE.keys() == response.json().keys()
    assert re.match(UUID_REGEX_LOWERCASE,
                    response.json()['uuid']['uuid'])
    assert response.json()['uuid']['version'] == 4


def test_uuid_router_unsupported_version(client):
    with client:
        response: Response = client.get('/v1/uuid?version=5')

    assert response.status_code == 400

    # A bit of magic happens below: unpacking dict with * returns list of keys so [0] will equal to the first key
    assert [*response.json()][0] == 'detail'
    assert 'Unsupported uuid version. Use version `4` as path param' == response.json()['detail']
