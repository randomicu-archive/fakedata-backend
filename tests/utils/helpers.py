#!/usr/bin/env python
from requests import Response
from starlette import status

from tests.utils.constants import MEDIATYPE_APPLICATION_JSON


def check_response(response: Response):
    assert response.status_code == status.HTTP_200_OK
    assert response.headers['content-type'] == MEDIATYPE_APPLICATION_JSON


def check_data(data: dict[str, str | float], **kwargs):
    for key in data.keys():
        assert data[key] == kwargs[key]


def check_structure(response_structure: dict, expected_structure: dict):
    assert response_structure.keys() == expected_structure.keys()
    assert len(response_structure.keys()) == len(expected_structure.keys())
