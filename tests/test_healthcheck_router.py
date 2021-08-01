#!/usr/bin/env python
from requests import Response

from app import __version__


def test_healthcheck_router(client):
    with client:
        response: Response = client.get('/healthcheck')

    response_structure = {
        'status': 'UP',
        'version': __version__
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()
    assert response_structure == response.json()
    assert response.json()['version'] == __version__
