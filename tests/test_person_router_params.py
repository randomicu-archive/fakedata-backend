#!/usr/bin/env python
import pytest
from requests import Response

from tests.utils.constants import PERSON_RESPONSE_STRUCTURE
from tests.utils.helpers import check_response

RESPONSE_STRUCTURE = PERSON_RESPONSE_STRUCTURE
TEST_EN_DATA = [
    ('age', 66),
    ('email', 'test_email@domain.com'),
    ('first_name', 'test_name'),
    ('height', 66.6),
    ('identifier', 'test_identifier'),
    ('last_name', 'test_lastname'),
    ('nationality', 'test_nationality'),
    ('occupation', 'pizza maker'),
    ('political_views', 'test_views'),
    ('telephone', '1-800-666-9999'),
    ('title', 'test_title'),
    ('university', 'test_university'),
    ('weight', 66.99),
    ('work_experience', 11.6)
]

TEST_RU_DATA = [*TEST_EN_DATA,
                ('patronymic', 'test patronymic'),
                ('inn', '223512526456'),
                ('kpp', '995880419'),
                ('bic', '041082839'),
                ('ogrn', '9132439447065'),
                ('passport', '86 16 539204')]


@pytest.mark.parametrize('param,expected', TEST_EN_DATA)
def test_en_person_router(param, expected, client):
    with client:
        response: Response = client.get(f'/v1/en/person?{param}={expected}')

    check_response(response=response)
    assert response.json()['result'][0][param] == expected


@pytest.mark.parametrize('param,expected', TEST_RU_DATA)
def test_ru_person_router(param, expected, client):
    with client:
        response: Response = client.get(f'/v1/ru/person?{param}={expected}')

    check_response(response=response)
    assert response.json()['result'][0][param] == expected
