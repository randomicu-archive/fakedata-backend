#!/usr/bin/env python
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import ENUM

from app.db import metadata
from app.enums import EventType

event_table = Table(
    'event',
    metadata,
    Column('event_id', Integer, primary_key=True),
    Column('created_at', DateTime, nullable=False, default=func.now()),
    Column('language', String, nullable=False),
    Column('event_type', ENUM(EventType, name='event_type'), nullable=False)
)
