#!/usr/bin/env python
# This module is wrapper for Mimesis's address provider
# Map Mimesis languages like "locale": "country_code"
import functools

from mimesis import Address

MIMESIS_LANGUAGES = {
    'en': 'us',
    'ru': 'ru'
}


@functools.lru_cache()
def get_address_object(lang: str) -> Address:
    return Address(lang)


def get_data(address: Address, lang: str):
    return {
        'address': address.address(),
        'calling_code': address.calling_code(),
        'city': address.city(),
        'continent': address.continent(),
        'coordinates': address.coordinates(),
        'country': address.country(),
        'country_code': get_country_code(lang),
        'latitude': address.latitude(),
        'longitude': address.longitude(),
        'postal_code': address.postal_code(),
        'state': address.state(),
        'street_name': address.street_name(),
        'street_number': address.street_number(),
        'street_suffix': address.street_suffix(),
        'zip_code': address.zip_code()
    }


def get_country_code(language: str) -> str:
    return MIMESIS_LANGUAGES[language]
