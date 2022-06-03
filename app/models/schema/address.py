#!/usr/bin/env python
from pydantic import BaseModel


class AddressSchema(BaseModel):
    address: str
    calling_code: int
    city: str
    continent: str
    coordinates: dict[str, float]
    country: str
    country_code: str
    state: str
    street_name: str
    street_number: int
    street_suffix: str
    zip_code: str


class RootAddressSchema(BaseModel):
    result: list[AddressSchema] = []
