#!/usr/bin/env python

UUID_REGEX_UPPERCASE = r'[0-9A-F]{8}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{4}\-[0-9A-F]{12}'
UUID_REGEX_LOWERCASE = r'[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}'

MEDIATYPE_APPLICATION_JSON = 'application/json'

ADDRESS_RESPONSE_STRUCTURE = {
    'result': [
        {
            'address': '',
            'calling_code': '',
            'city': '',
            'continent': '',
            'coordinates': '',
            'country': '',
            'country_code': '',
            'state': '',
            'street_name': '',
            'street_number': '',
            'street_suffix': '',
            'zip_code': '',
        }
    ],
    'seed': ''
}

PERSON_RESPONSE_STRUCTURE = {
    'result': [
        {
            'age': '',
            'email': '',
            'first_name': '',
            'full_name': '',
            'gender': '',
            'height': '',
            'identifier': '',
            'last_name': '',
            'nationality': '',
            'occupation': '',
            'password': '',
            'political_views': '',
            'telephone': '',
            'title': '',
            'university': '',
            'username': '',
            'weight': '',
            'work_experience': ''
        }
    ],
    'seed': ''
}

PERSON_RU_RESPONSE_STRUCTURE = {
    'result': [
        {
            'age': '',
            'email': '',
            'first_name': '',
            'full_name': '',
            'gender': '',
            'height': '',
            'identifier': '',
            'last_name': '',
            'nationality': '',
            'occupation': '',
            'password': '',
            'political_views': '',
            'telephone': '',
            'title': '',
            'university': '',
            'username': '',
            'weight': '',
            'work_experience': '',
            'patronymic': '',
            'inn': '',
            'kpp': '',
            'bic': '',
            'ogrn': '',
            'passport': ''
        }
    ],
    'seed': ''
}

UUID_RESPONSE_STRUCTURE = {
    'result': [
        {
            'uuid': {
                'uuid': '',
                'version': ''
            },
            'uppercase': ''
        }
    ]
}
