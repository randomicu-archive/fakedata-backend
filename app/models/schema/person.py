#!/usr/bin/env python
from pydantic import BaseModel


class PersonSchema(BaseModel):
    age: int | str
    email: str
    first_name: str
    full_name: str
    gender: str
    height: str
    identifier: str
    last_name: str
    nationality: str
    occupation: str
    password: str
    political_views: str
    telephone: str
    title: str
    university: str
    username: str
    weight: int
    work_experience: int
    patronymic: str | None = None
    inn: str | None = None
    kpp: str | None = None
    bic: str | None = None
    ogrn: str | None = None
    passport: str | None = None


class RootPersonSchema(BaseModel):
    result: list[PersonSchema] = []
