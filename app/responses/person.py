#!/usr/bin/env python
import secrets

from mimesis import Person
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

from app.enums import Locale
from app.enums import ProviderType
from app.helpers.factory import Factory
from app.models.schema.person import PersonSchema
from app.responses.response import Response


class PersonResponse(Response):
    def __init__(self, locale: str, seed: str | None, **kwargs):
        self.locale: Locale = Locale[locale.upper()]
        self._seed = seed or secrets.token_hex(16)
        self.count = kwargs['count']
        self.provider: Person = Factory.get_provider(ProviderType.PERSON, seed=self.seed, locale=self.locale)
        self.gender_number: int = Factory.get_gender_code(seed=self.seed)
        self.gender: Gender = self._get_gender(self.gender_number)
        self.age: int = kwargs['age']
        self.email: str = kwargs['email']
        self.first_name: str = kwargs['first_name']
        self.full_name: str = kwargs['full_name']
        self.height: float = kwargs['height']
        self.identifier: str = kwargs['identifier']
        self.last_name: str = kwargs['last_name']
        self.nationality: str = kwargs['nationality']
        self.occupation: str = kwargs['occupation']
        self.political_views: str = kwargs['political_views']
        self.telephone: str = kwargs['telephone']
        self.title: str = kwargs['title']
        self.university: str = kwargs['university']
        self.username: str = kwargs['username']
        self.weight: float = kwargs['weight']
        self.work_experience: float = kwargs['work_experience']
        self.patronymic: str = kwargs['patronymic']
        self.inn: str = kwargs['inn']
        self.kpp: int = kwargs['kpp']
        self.bic: int = kwargs['bic']
        self.ogrn: int = kwargs['ogrn']
        self.passport: str = kwargs['passport']

    @property
    def seed(self):
        return self._seed

    def generate(self):
        self.provider.reseed(self.seed)

        schemas = []

        for _ in range(self.count):
            schema = self._generate_schema()
            schemas.append(schema)

        return schemas

    def _generate_schema(self):
        _first_name = self.first_name or self.provider.first_name(gender=self.gender)
        _last_name = self.last_name or self.provider.last_name(gender=self.gender)
        _full_name = f'{_first_name} {_last_name}'

        schema = PersonSchema(age=self.age or self.provider.age(),
                              email=self.email or self.provider.email(),
                              first_name=_first_name,
                              full_name=_full_name,
                              gender=self.gender.name.capitalize(),
                              height=self.height or self.provider.height(),
                              identifier=self.identifier or self.provider.identifier(),
                              last_name=_last_name,
                              nationality=self.nationality or self.provider.nationality(gender=self.gender),
                              occupation=self.occupation or self.provider.occupation(),
                              password=self.provider.password(),
                              political_views=self.political_views or self.provider.political_views(),
                              telephone=self.telephone or self.provider.telephone(),
                              title=self.title or self.provider.title(gender=self.gender),
                              university=self.university or self.provider.university(),
                              username=self.username or self.provider.username(),
                              weight=self.weight or self.provider.weight(),
                              work_experience=self.work_experience or self.provider.work_experience())

        is_regional: bool = self._check_if_regional()

        if is_regional:
            self._regional_schema_update(schema, full_name=schema.full_name)

        return schema

    def _check_if_regional(self) -> bool:
        return self.locale != Locale.EN

    def _get_gender(self, gender_code: int) -> Gender:
        match gender_code:
            case 1:
                return Gender.MALE
            case 2:
                return Gender.FEMALE

    def _regional_schema_update(self, schema, **kwargs) -> RussiaSpecProvider:
        ru_provider: RussiaSpecProvider = Factory.get_provider(ProviderType.REGIONAL_RU, seed=self.seed)
        ru_provider.reseed(seed=self.seed)

        _patronymic: str = self.patronymic or ru_provider.patronymic(self.gender)
        _full_name: str = f'{kwargs["full_name"]} {_patronymic}'

        schema.full_name = _full_name
        schema.patronymic = _patronymic
        schema.inn = self.inn or ru_provider.inn()
        schema.kpp = self.kpp or ru_provider.kpp()
        schema.bic = self.bic or ru_provider.bic()
        schema.ogrn = self.ogrn or ru_provider.ogrn()
        schema.passport = self.passport or ru_provider.series_and_number()

        return schema
