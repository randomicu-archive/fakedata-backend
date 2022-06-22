#!/usr/bin/env python
from app.enums import EventType
from app.repository.event import EventRepository


class Event:
    repo = EventRepository()

    @staticmethod
    async def send_event(event_type: EventType, language: str = 'en'):
        await Event.repo.save(event_type=event_type, language=language)
