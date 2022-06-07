#!/usr/bin/env python
import secrets

from fastapi import APIRouter
from fastapi import Depends

from app.enums import EventType
from app.helpers.event import Event
from app.middlewares import verify_locale
from app.models.schema.person import RootPersonSchema
from app.responses.person import PersonResponse

router = APIRouter()


@router.get('/{locale}/person',
            dependencies=[Depends(verify_locale)],
            response_model=RootPersonSchema,
            response_model_exclude_none=True)
async def get_person(locale: str,
                     seed: str = None,
                     count: int = 1,
                     age: int | None = None,
                     email: str | None = None,
                     first_name: str | None = None,
                     full_name: str | None = None,
                     height: int | None = None,
                     identifier: str | None = None,
                     last_name: str | None = None,
                     nationality: str | None = None,
                     occupation: str | None = None,
                     political_views: str | None = None,
                     telephone: str | None = None,
                     title: str | None = None,
                     university: str | None = None,
                     username: str | None = None,
                     weight: str | None = None,
                     work_experience: int | None = None,
                     patronymic: str | None = None,
                     inn: str | None = None,
                     kpp: str | None = None,
                     bic: str | None = None,
                     ogrn: str | None = None,
                     passport: str | None = None
                     ):

    if not seed:
        seed = secrets.token_hex(16)

    person_response: PersonResponse = PersonResponse(locale=locale,
                                                     seed=seed,
                                                     age=age,
                                                     email=email,
                                                     first_name=first_name,
                                                     full_name=full_name,
                                                     height=height,
                                                     identifier=identifier,
                                                     last_name=last_name,
                                                     nationality=nationality,
                                                     occupation=occupation,
                                                     political_views=political_views,
                                                     telephone=telephone,
                                                     title=title,
                                                     university=university,
                                                     username=username,
                                                     weight=weight,
                                                     work_experience=work_experience,
                                                     patronymic=patronymic,
                                                     inn=inn,
                                                     kpp=kpp,
                                                     bic=bic,
                                                     ogrn=ogrn,
                                                     passport=passport)

    responses = []
    if count >= 1:
        for _ in range(count):
            responses.append(person_response.generate())

    await Event.send_event(event_type=EventType.PERSON, language=locale)
    return RootPersonSchema(result=responses, seed=seed)
