#!/usr/bin/env python
from pydantic import BaseModel


class HealthcheckSchema(BaseModel):
    version: str
    status: str
