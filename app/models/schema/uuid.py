#!/usr/bin/env python
from pydantic import BaseModel


class _InternalSchemaUUID(BaseModel):
    uuid: str
    version: int = 4


class UUIDSchema(BaseModel):
    uuid: _InternalSchemaUUID
    uppercase: bool
