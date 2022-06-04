#!/usr/bin/env python
from app.db import database
from app.enums import EventType
from app.models.db.event import event_table


class Event:
    @staticmethod
    async def send_event(event_type: EventType, language: str = 'en'):
        query = event_table.insert().values(
            event_type=event_type.value,
            language=language
        )
        return await database.execute(query=query)
