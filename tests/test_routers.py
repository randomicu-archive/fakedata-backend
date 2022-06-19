#!/usr/bin/env python
from requests import Response
from starlette import status

from tests.utils.helpers import check_data
from tests.utils.helpers import check_structure


def test_en_inexistent_route(client):
    with client:
        response: Response = client.get('/v1/en/no_route')

    data = {
        'detail': 'Not Found'
    }

    check_structure(response_structure=response.json(), expected_structure=data)
    check_data(data=data, detail='Not Found')

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_ru_inexistent_route(client):
    with client:
        response: Response = client.get('/v1/ru/no_route')

    data = {
        'detail': 'Not Found'
    }

    check_structure(response_structure=response.json(), expected_structure=data)
    check_data(data=data, detail='Not Found')

    assert response.status_code == status.HTTP_404_NOT_FOUND
