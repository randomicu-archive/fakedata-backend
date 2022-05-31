#!/usr/bin/env python
from pydantic import BaseModel


class NestedUuidSchema(BaseModel):
    uuid: str
    version: int


class UuidSchema(BaseModel):
    uuid: NestedUuidSchema
    uppercase: bool


class RootUuidSchema(BaseModel):
    result: list[UuidSchema] = []
