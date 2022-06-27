#!/usr/bin/env python
import uuid

from fastapi import HTTPException
from starlette import status

from app.models.schema.uuid import NestedUuidSchema
from app.models.schema.uuid import UuidSchema
from app.responses.response import Response


class UuidResponse(Response):
    def __init__(self, count: int, uppercase: bool, version: int):
        self.count = count
        self.uppercase = uppercase
        self.version = version

    def generate(self):
        if self.version != 4:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Unsupported uuid version. '
                                       'Use version `4` as a query param')

        return [self._generate_schema() for _ in range(self.count)]

    def _generate_schema(self):
        random_uuid: str = str(uuid.uuid4())
        _uuid: str = random_uuid if not self.uppercase else random_uuid.upper()
        nested_uuid_schema: NestedUuidSchema = NestedUuidSchema(uuid=_uuid, version=self.version)

        return UuidSchema(uuid=nested_uuid_schema, uppercase=self.uppercase)
