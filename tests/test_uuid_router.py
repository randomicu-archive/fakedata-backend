#!/usr/bin/env python
import re

from requests import Response

from tests.utils.constants import UUID_REGEX_LOWERCASE
from tests.utils.constants import UUID_REGEX_UPPERCASE
from tests.utils.constants import UUID_RESPONSE_STRUCTURE
from tests.utils.helpers import ensure_valid_response

RESPONSE_STRUCTURE = UUID_RESPONSE_STRUCTURE


def test_uuid_router_v4_lowercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=false&version=4')

    ensure_valid_response(response, RESPONSE_STRUCTURE)

    assert re.match(UUID_REGEX_LOWERCASE, response.json()['result'][0]['uuid']['uuid'])
    assert len(response.json()['result']) == 1
    assert response.json()['result'][0]['uuid']['version'] == 4


def test_uuid_router_v4_uppercase(client):
    with client:
        response: Response = client.get('/v1/uuid?uppercase=true&version=4')

    ensure_valid_response(response, RESPONSE_STRUCTURE)

    assert re.match(UUID_REGEX_UPPERCASE, response.json()['result'][0]['uuid']['uuid'])
    assert len(response.json()['result']) == 1
    assert response.json()['result'][0]['uuid']['version'] == 4


def test_uuid_router_count_param_lowercase(client):
    with client:
        response: Response = client.get('/v1/uuid?count=2')

    ensure_valid_response(response, RESPONSE_STRUCTURE)

    assert re.match(UUID_REGEX_LOWERCASE, response.json()['result'][1]['uuid']['uuid'])
    assert len(response.json()['result']) == 2
    assert response.json()['result'][0]['uuid']['version'] == 4


def test_uuid_router_count_param_uppercase(client):
    with client:
        response: Response = client.get('/v1/uuid?count=2&uppercase=true')

    ensure_valid_response(response, RESPONSE_STRUCTURE)

    assert re.match(UUID_REGEX_UPPERCASE, response.json()['result'][1]['uuid']['uuid'])
    assert len(response.json()['result']) == 2
    assert response.json()['result'][1]['uuid']['version'] == 4


def test_uuid_router_default(client):
    with client:
        response: Response = client.get('/v1/uuid')

    ensure_valid_response(response, RESPONSE_STRUCTURE)

    assert re.match(UUID_REGEX_LOWERCASE, response.json()['result'][0]['uuid']['uuid'])
    assert len(response.json()['result']) == 1
    assert response.json()['result'][0]['uuid']['version'] == 4


def test_uuid_router_unsupported_version(client):
    with client:
        response: Response = client.get('/v1/uuid?version=5')

    assert response.status_code == 400

    # A bit of magic happens below: unpacking dict with * returns list of keys so [0] will equal to the first key
    assert [*response.json()][0] == 'detail'
    assert 'Unsupported uuid version. Use version `4` as a query param' == response.json()['detail']
