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


def test_en_person_seed_count_param(client):
    seed: str = '34d796a995a270905f72f1e94eb48fb6'
    count = 2
    with client:
        response: Response = client.get(f'/v1/en/person?seed={seed}&count={count}')

    data_first = {
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

    data_second = {
        'age': 60,
        'email': 'along2078@yandex.com',
        'first_name': 'Stephnie',
        'full_name': 'Stephnie Robles',
        'gender': 'Female',
        'height': 1.83,
        'identifier': '17-34/09',
        'last_name': 'Robles',
        'nationality': 'Danish',
        'occupation': 'Builder',
        'password': 's(Rs&d{%',
        'political_views': 'Anarchism',
        'telephone': '822.764.7267',
        'title': 'M.D.',
        'university': 'Florida Gulf Coast University (FGCU)',
        'username': 'prove_2003',
        'weight': 52,
        'work_experience': 38
    }

    result_raw: dict = response.json()
    result_json_first: dict = response.json()['result'][0]
    result_json_second: dict = response.json()['result'][1]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json_first, expected_structure=RESPONSE_STRUCTURE['result'][0])
    check_structure(response_structure=result_json_second, expected_structure=RESPONSE_STRUCTURE['result'][0])

    check_data(data=data_first,
               age=result_json_first['age'],
               email=result_json_first['email'],
               full_name=result_json_first['full_name'],
               first_name=result_json_first['first_name'],
               gender=result_json_first['gender'],
               height=result_json_first['height'],
               identifier=result_json_first['identifier'],
               last_name=result_json_first['last_name'],
               nationality=result_json_first['nationality'],
               occupation=result_json_first['occupation'],
               password=result_json_first['password'],
               political_views=result_json_first['political_views'],
               telephone=result_json_first['telephone'],
               title=result_json_first['title'],
               university=result_json_first['university'],
               username=result_json_first['username'],
               weight=result_json_first['weight'],
               work_experience=result_json_first['work_experience'])

    check_data(data=data_second,
               age=result_json_second['age'],
               email=result_json_second['email'],
               full_name=result_json_second['full_name'],
               first_name=result_json_second['first_name'],
               gender=result_json_second['gender'],
               height=result_json_second['height'],
               identifier=result_json_second['identifier'],
               last_name=result_json_second['last_name'],
               nationality=result_json_second['nationality'],
               occupation=result_json_second['occupation'],
               password=result_json_second['password'],
               political_views=result_json_second['political_views'],
               telephone=result_json_second['telephone'],
               title=result_json_second['title'],
               university=result_json_second['university'],
               username=result_json_second['username'],
               weight=result_json_second['weight'],
               work_experience=result_json_second['work_experience'])


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


def test_ru_person_seed_count_param(client):
    seed: str = 'a8e9b85955cf294c3c2525f1643c610c'
    count = 2
    with client:
        response: Response = client.get(f'/v1/ru/person?seed={seed}&count={count}')

    data_first = {
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

    data_second = {
        'age': 21,
        'email': 'bases1980@example.org',
        'first_name': 'Дженнифер',
        'full_name': 'Дженнифер Сбруева Устиновна',
        'gender': 'Female',
        'height': 1.65,
        'identifier': '13-84/96',
        'last_name': 'Сбруева',
        'nationality': 'Китаянка',
        'occupation': 'Милиционер',
        'password': '8:PVWViz',
        'political_views': 'Умеренные',
        'telephone': '+7-(909)-497-33-76',
        'title': 'Доктор',
        'university': 'МГУ им. Ломоносова',
        'username': 'discussion_2022',
        'weight': 52,
        'work_experience': 0,
        'patronymic': 'Устиновна',
        'inn': '434720544026',
        'kpp': '010066710',
        'bic': '040556853',
        'ogrn': '4925315929589',
        'passport': '88 17 508640'
    }

    result_raw: dict = response.json()
    result_json_first: dict = response.json()['result'][0]
    result_json_second: dict = response.json()['result'][1]

    check_response(response=response)
    check_structure(response_structure=result_raw, expected_structure=RESPONSE_STRUCTURE)
    check_structure(response_structure=result_json_first, expected_structure=RESPONSE_RU_STRUCTURE['result'][0])
    check_structure(response_structure=result_json_second, expected_structure=RESPONSE_RU_STRUCTURE['result'][0])
    check_data(data=data_first,
               age=result_json_first['age'],
               email=result_json_first['email'],
               first_name=result_json_first['first_name'],
               full_name=result_json_first['full_name'],
               gender=result_json_first['gender'],
               height=result_json_first['height'],
               identifier=result_json_first['identifier'],
               last_name=result_json_first['last_name'],
               nationality=result_json_first['nationality'],
               occupation=result_json_first['occupation'],
               password=result_json_first['password'],
               political_views=result_json_first['political_views'],
               telephone=result_json_first['telephone'],
               title=result_json_first['title'],
               university=result_json_first['university'],
               username=result_json_first['username'],
               weight=result_json_first['weight'],
               work_experience=result_json_first['work_experience'],
               patronymic=result_json_first['patronymic'],
               inn=result_json_first['inn'],
               kpp=result_json_first['kpp'],
               bic=result_json_first['bic'],
               ogrn=result_json_first['ogrn'],
               passport=result_json_first['passport'])

    check_data(data=data_second,
               age=result_json_second['age'],
               email=result_json_second['email'],
               first_name=result_json_second['first_name'],
               full_name=result_json_second['full_name'],
               gender=result_json_second['gender'],
               height=result_json_second['height'],
               identifier=result_json_second['identifier'],
               last_name=result_json_second['last_name'],
               nationality=result_json_second['nationality'],
               occupation=result_json_second['occupation'],
               password=result_json_second['password'],
               political_views=result_json_second['political_views'],
               telephone=result_json_second['telephone'],
               title=result_json_second['title'],
               university=result_json_second['university'],
               username=result_json_second['username'],
               weight=result_json_second['weight'],
               work_experience=result_json_second['work_experience'],
               patronymic=result_json_second['patronymic'],
               inn=result_json_second['inn'],
               kpp=result_json_second['kpp'],
               bic=result_json_second['bic'],
               ogrn=result_json_second['ogrn'],
               passport=result_json_second['passport'])


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/person')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
