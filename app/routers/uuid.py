#!/usr/bin/env python
from fastapi import APIRouter

from app.enums import EventType
from app.helpers.event import Event
from app.models.schema.uuid import RootUuidSchema
from app.responses.uuid import UuidResponse

router = APIRouter()


@router.get('/uuid', response_model=RootUuidSchema)
async def get_uuid(uppercase: bool = False, version: int = 4, count: int = 1):
    uuid_response = UuidResponse(count=count, uppercase=uppercase, version=version)
    response = uuid_response.generate()

    await Event.send_event(event_type=EventType.uuid)
    return RootUuidSchema(result=response)
