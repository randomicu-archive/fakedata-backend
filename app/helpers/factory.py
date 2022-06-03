#!/usr/bin/env python
import functools

from enums import ProviderType
from mimesis import Address


class ProviderFactory:

    @staticmethod
    @functools.lru_cache
    def get(provider_type: ProviderType, lang: str = 'en'):
        match provider_type:
            case ProviderType.address:
                return Address(lang)
