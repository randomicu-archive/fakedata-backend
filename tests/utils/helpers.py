#!/usr/bin/env python
from requests import Response


def ensure_valid_response(response: Response, response_structure: dict):
    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()
