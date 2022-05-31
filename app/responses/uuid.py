#!/usr/bin/env python
import uuid

from app.models.schema.uuid import NestedUuidSchema
from app.models.schema.uuid import UuidSchema
from app.responses.response import Response


class UuidResponse(Response):
    def __init__(self, uppercase: bool, version: int):
        self.uppercase = uppercase
        self.version = version

    def generate(self) -> UuidSchema:
        random_uuid: str = str(uuid.uuid4())
        _uuid: str = random_uuid if not self.uppercase else random_uuid.upper()
        nested_uuid_schema: NestedUuidSchema = NestedUuidSchema(uuid=_uuid, version=self.version)

        return UuidSchema(uuid=nested_uuid_schema, uppercase=self.uppercase)
