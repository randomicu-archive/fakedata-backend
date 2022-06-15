#!/usr/bin/env python
from requests import Response

from app import __version__
from tests.utils.helpers import check_data
from tests.utils.helpers import check_response
from tests.utils.helpers import check_structure


def test_health_router(client):
    with client:
        response: Response = client.get('/health')

    data = {
        'version': __version__,
        'status': 'UP',
    }

    result_json: dict = response.json()

    check_response(response=response)
    check_data(data=data,
               version=result_json['version'],
               status=result_json['status'])
    check_structure(response_structure=result_json, expected_structure=data)
