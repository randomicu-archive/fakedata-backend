#!/usr/local/bin python
from fastapi import APIRouter
from fastapi import HTTPException

from app.enums import EventType
from app.helpers.send_event import send_event
from app.models.schema.uuid import UUIDSchema
from app.providers.uuid import get_data

router = APIRouter()


@router.get('/uuid', response_model=UUIDSchema)
async def get_uuid(uppercase: bool = False, version: int = 4):

    if version != 4:
        raise HTTPException(status_code=400,
                            detail='Unsupported uuid version. '
                                   'Use version `4` as path param')

    data = get_data(uppercase=uppercase, version=version)

    await send_event(event_type=EventType.uuid)

    return UUIDSchema(**data)
