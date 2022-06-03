#!/usr/bin/env python
from fastapi import APIRouter
from fastapi import Depends
from mimesis import Person

from app.enums import EventType
from app.helpers.event import Event
from app.middlewares import verify_locale
from app.models.schema.person import PersonSchema
from app.responses.person import get_additional_data
from app.responses.person import get_data
from app.responses.person import get_person_gender
from app.responses.person import get_person_object

router = APIRouter()


@router.get('/{lang}/person', dependencies=[Depends(verify_locale)],
            response_model=PersonSchema,
            response_model_exclude_none=True)
async def get_person(lang: str):
    person: Person = get_person_object(lang)
    person_gender = get_person_gender(person.gender(iso5218=True))
    data = get_data(person, person_gender)
    additional_data = get_additional_data(lang, person_gender)

    if additional_data:
        if additional_data.get('patronymic'):
            patronymic = additional_data.get('patronymic')
            first_name = data['first_name']
            last_name = data['last_name']

            data['full_name'] = f'{last_name} {first_name} {patronymic}'

        data.update(additional_data)

    await Event.send_event(event_type=EventType.person, language=lang)

    return PersonSchema(**data)
