#!/usr/bin/env python
from fastapi import APIRouter
from fastapi import Depends
from mimesis import Address

from app.enums import EventType
from app.middlewares import verify_mimesis_locales
from app.models.schema.address import AddressSchema
from app.responses.address import get_address_object
from app.responses.address import get_data
from app.helpers.event import Event

router = APIRouter()


@router.get('/{lang}/address',
            dependencies=[Depends(verify_mimesis_locales)])
async def get_address(lang: str):
    address: Address = get_address_object(lang)
    data = get_data(address, lang)

    await Event.send_event(event_type=EventType.address, language=lang)

    return AddressSchema(**data)
