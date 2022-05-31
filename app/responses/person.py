#!/usr/bin/env python
# This module is wrapper for Mimesis's gender provider
import functools
from typing import Dict
from typing import Optional
from typing import Union

from mimesis import Person
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender


@functools.lru_cache()
def get_person_object(lang: str) -> Person:
    return Person(lang)


@functools.lru_cache()
def get_ru_special_fields() -> RussiaSpecProvider:
    return RussiaSpecProvider()


def get_data(person: Person, gender: Gender):
    first_name = person.first_name(gender=gender)
    last_name = person.last_name(gender=gender)

    return {
        'age': person.age(),
        'email': person.email(),
        'first_name': first_name,
        'full_name': f'{first_name} {last_name}',
        'gender': str(gender.value).capitalize(),
        'height': person.height(),
        'identifier': person.identifier(),
        'last_name': last_name,
        'nationality': person.nationality(gender=gender),
        'occupation': person.occupation(),
        'password': person.password(),
        'political_views': person.political_views(),
        'telephone': person.telephone(),
        'title': person.title(gender=gender),
        'university': person.university(),
        'username': person.username(),
        'weight': person.weight(),
        'work_experience': person.work_experience(),
    }


def get_additional_data(lang: str, gender: Gender) -> Optional[Dict[str, str]]:
    if lang == 'ru':
        ru = get_ru_special_fields()
        additional_data = {
            'patronymic': ru.patronymic(gender=gender),
            'inn': ru.inn(),
            'kpp': ru.kpp(),
            'bic': ru.bic(),
            'ogrn': ru.ogrn(),
            'passport': ru.series_and_number()
        }
        return additional_data
    else:
        return None


def get_person_gender(gender_code: Union[str, int]) -> Gender:
    """
    :param gender_code:
        Codes for the representation of human sexes is an international
        standard (0 - not known, 1 - male, 2 - female, 9 - not applicable).
    """

    if gender_code == 0:
        return Gender.MALE
    elif gender_code == 1:
        return Gender.MALE
    elif gender_code == 2:
        return Gender.FEMALE
    else:
        return Gender.FEMALE
