#!/usr/bin/env python
import logging

from app.db import database
from app.enums import EventType
from app.models.db.event import event_table
from app.repository.repository import Repository

log = logging.getLogger('uvicorn')


class EventRepository(Repository):

    @property
    def table(self):
        return event_table

    async def save(self, event_type: EventType, language: str = 'en'):
        log.info('Saving event to the database: %s', event_type.value)
        data = {
            'event_type': event_type.value,
            'language': language
        }
        query = self.table.insert()

        return await database.execute(query=query, values=data)

    # todo: use this method
    async def find_by_id(self, event_id):
        query = self.table.select().filter(self.table.c.event_id == event_id)
        return await database.fetch_one(query)

    # todo: use this method
    async def find_all(self):
        query = self.table.select()
        return await database.fetch_all(query)
