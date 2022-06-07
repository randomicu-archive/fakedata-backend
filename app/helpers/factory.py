#!/usr/bin/env python
import functools
import random

from mimesis import Address
from mimesis import Person
from mimesis.builtins import RussiaSpecProvider

from app.enums import Locale
from app.enums import ProviderType


class Factory:

    @staticmethod
    @functools.lru_cache
    def get_provider(provider_type: ProviderType, seed: str = None, locale: Locale = Locale.EN):

        _locale: str = locale.value

        match provider_type.value:
            case ProviderType.ADDRESS.value:
                return Address(_locale, seed=seed)
            case ProviderType.PERSON.value:
                return Person(_locale, seed=seed)
            case ProviderType.REGIONAL_RU.value:
                return RussiaSpecProvider(seed=seed)

    @staticmethod
    @functools.lru_cache
    def get_gender_code(seed):
        random.seed(seed)
        return random.choice([1, 2])
