#!/usr/bin/env python
from http import HTTPStatus

from fastapi import APIRouter
from fastapi import HTTPException

from app.enums import EventType
from app.helpers.event import Event
from app.models.schema.uuid import RootUuidSchema
from app.models.schema.uuid import UuidSchema
from app.responses.uuid import UuidResponse

router = APIRouter()


@router.get('/uuid', response_model=RootUuidSchema)
async def get_uuids(uppercase: bool = False, version: int = 4, count: int = 1) -> RootUuidSchema | list[RootUuidSchema]:
    if version != 4:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='Unsupported uuid version. '
                                   'Use version `4` as a query param')

    responses: list[UuidSchema] = []

    if count > 1:
        for _ in range(count):
            response: UuidResponse = UuidResponse(uppercase=uppercase, version=version)
            responses.append(response.generate())

        return RootUuidSchema(result=responses)

    uuid_response: UuidResponse = UuidResponse(uppercase=uppercase, version=version)
    responses.append(uuid_response.generate())

    await Event.send_event(event_type=EventType.UUID)
    return RootUuidSchema(result=responses)
