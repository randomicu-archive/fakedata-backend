#!/usr/bin/env python
from databases import Database
from sqlalchemy import MetaData

from app.config import get_settings

settings = get_settings()
metadata = MetaData()

database = Database(settings.database_url)
