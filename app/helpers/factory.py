#!/usr/bin/env python
import functools

from mimesis import Address
from mimesis import Person
from mimesis.builtins import RussiaSpecProvider

from app.enums import Locale
from app.enums import ProviderType


class ProviderFactory:

    @staticmethod
    @functools.lru_cache
    def get(provider_type: ProviderType, locale: Locale = Locale.EN):

        _locale: str = locale.value

        match provider_type.value:
            case ProviderType.ADDRESS.value:
                return Address(_locale)
            case ProviderType.PERSON.value:
                return Person(_locale)
            case ProviderType.REGIONAL_RU.value:
                return RussiaSpecProvider()
