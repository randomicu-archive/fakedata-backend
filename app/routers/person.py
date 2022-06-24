#!/usr/bin/env python
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
                     height: float | None = None,
                     identifier: str | None = None,
                     last_name: str | None = None,
                     nationality: str | None = None,
                     occupation: str | None = None,
                     political_views: str | None = None,
                     telephone: str | None = None,
                     title: str | None = None,
                     university: str | None = None,
                     username: str | None = None,
                     weight: float | None = None,
                     work_experience: float | None = None,
                     patronymic: str | None = None,
                     inn: str | None = None,
                     kpp: str | None = None,
                     bic: str | None = None,
                     ogrn: str | None = None,
                     passport: str | None = None
                     ):
    person_response: PersonResponse = PersonResponse(locale=locale,
                                                     seed=seed,
                                                     count=count,
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

    response = person_response.generate()
    provider_seed = person_response.seed

    await Event.send_event(event_type=EventType.person, language=locale)
    return RootPersonSchema(result=response, seed=provider_seed)
