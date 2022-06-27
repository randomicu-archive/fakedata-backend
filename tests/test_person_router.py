#!/usr/bin/env python
from requests import Response
from starlette import status

from tests.utils.constants import PERSON_RESPONSE_STRUCTURE
from tests.utils.constants import PERSON_RU_RESPONSE_STRUCTURE
from tests.utils.helpers import check_data
from tests.utils.helpers import check_response
from tests.utils.helpers import check_structure

RESPONSE_STRUCTURE = PERSON_RESPONSE_STRUCTURE
RESPONSE_RU_STRUCTURE = PERSON_RU_RESPONSE_STRUCTURE


def test_en_person_router(client):
    with client:
        response: Response = client.get('/v1/en/person')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])


def test_ru_person_router(client):
    with client:
        response: Response = client.get('/v1/ru/person')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_RU_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_RU_STRUCTURE['result'][0])


def test_en_person_count_param(client):
    with client:
        response: Response = client.get('/v1/en/person?count=2')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result']

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json[0], expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json[1], expected_structure=RESPONSE_STRUCTURE['result'][0])

    assert len(response.json()['result']) == 2


def test_ru_person_count_param(client):
    with client:
        response: Response = client.get('/v1/ru/person?count=2')

    result_raw: dict = response.json()
    result_json: dict = response.json()['result']

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_RU_STRUCTURE)
    check_structure(response_structure=result_json[0], expected_structure=RESPONSE_RU_STRUCTURE['result'][0])
    check_structure(response_structure=result_json[1], expected_structure=RESPONSE_RU_STRUCTURE['result'][0])

    assert len(response.json()['result']) == 2


def test_en_person_seed_param(client):
    seed: str = '34d796a995a270905f72f1e94eb48fb6'
    with client:
        response: Response = client.get(f'/v1/en/person?seed={seed}')

    data = {
        'age': 27,
        'email': 'dry1942@outlook.com',
        'first_name': 'Maragret',
        'full_name': 'Maragret Thornton',
        'gender': 'Female',
        'height': 1.5,
        'identifier': '26-19/91',
        'last_name': 'Thornton',
        'nationality': 'Ecuadorian',
        'occupation': 'Shipyard Worker',
        'password': 'Wi\"I_G2_',
        'political_views': 'Anarchism',
        'telephone': '(999) 940-2420',
        'title': 'B.E.',
        'university': 'Worcester State University',
        'username': 'contributors_2083',
        'weight': 53,
        'work_experience': 5
    }

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json, expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_data(data=data,
               age=result_json['age'],
               email=result_json['email'],
               full_name=result_json['full_name'],
               first_name=result_json['first_name'],
               gender=result_json['gender'],
               height=result_json['height'],
               identifier=result_json['identifier'],
               last_name=result_json['last_name'],
               nationality=result_json['nationality'],
               occupation=result_json['occupation'],
               password=result_json['password'],
               political_views=result_json['political_views'],
               telephone=result_json['telephone'],
               title=result_json['title'],
               university=result_json['university'],
               username=result_json['username'],
               weight=result_json['weight'],
               work_experience=result_json['work_experience'])


def test_ru_person_seed_param(client):
    seed: str = 'a8e9b85955cf294c3c2525f1643c610c'
    with client:
        response: Response = client.get(f'/v1/ru/person?seed={seed}')

    data = {
        'age': 30,
        'email': 'images1874@yahoo.com',
        'first_name': 'Тереза',
        'full_name': 'Тереза Никитина Устиновна',
        'gender': 'Female',
        'height': 1.97,
        'identifier': '73-98/00',
        'last_name': 'Никитина',
        'nationality': 'Нидерландка',
        'occupation': 'Биолог',
        'password': 'yP[4F]-1',
        'political_views': 'Либертарианские',
        'telephone': '+7-(968)-656-54-45',
        'title': 'Миссис',
        'university': 'Бауманское МГТУ',
        'username': 'telling_1892',
        'weight': 58,
        'work_experience': 8,
        'patronymic': 'Устиновна',
        'inn': '434720544026',
        'kpp': '010066710',
        'bic': '040556853',
        'ogrn': '4925315929589',
        'passport': '88 17 508640'
    }

    result_raw: dict = response.json()
    result_json: dict = response.json()['result'][0]

    check_response(response=response)

    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_data(data=data,
               age=result_json['age'],
               email=result_json['email'],
               first_name=result_json['first_name'],
               full_name=result_json['full_name'],
               gender=result_json['gender'],
               height=result_json['height'],
               identifier=result_json['identifier'],
               last_name=result_json['last_name'],
               nationality=result_json['nationality'],
               occupation=result_json['occupation'],
               password=result_json['password'],
               political_views=result_json['political_views'],
               telephone=result_json['telephone'],
               title=result_json['title'],
               university=result_json['university'],
               username=result_json['username'],
               weight=result_json['weight'],
               work_experience=result_json['work_experience'],
               patronymic=result_json['patronymic'],
               inn=result_json['inn'],
               kpp=result_json['kpp'],
               bic=result_json['bic'],
               ogrn=result_json['ogrn'],
               passport=result_json['passport'])


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/person')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
