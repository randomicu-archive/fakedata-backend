#!/usr/bin/env python
from app.enums import Locale
from app.enums import ProviderType
from app.helpers.factory import ProviderFactory
from app.models.schema.address import AddressSchema
from app.responses.response import Response


class AddressResponse(Response):
    def __init__(self, locale: str, **kwargs):
        self.locale = Locale[locale.upper()]
        self.provider = ProviderFactory.get(ProviderType.ADDRESS, locale=self.locale)
        self.address = kwargs['address']
        self.calling_code = kwargs['calling_code']
        self.city = kwargs['city']
        self.continent = kwargs['continent']
        self.country = kwargs['country']
        self.country_code = kwargs['country_code']
        self.state = kwargs['state']
        self.street_name = kwargs['street_name']
        self.street_number = kwargs['street_number']
        self.street_suffix = kwargs['street_suffix']
        self.zip_code = kwargs['zip_code']

    def generate(self):
        return AddressSchema(
            address=self.address or self.provider.address(),
            calling_code=self.calling_code or self.provider.calling_code(),
            city=self.city or self.provider.city(),
            continent=self.continent or self.provider.continent(),
            coordinates=self.provider.coordinates(),
            country=self.country or self.provider.country(),
            country_code=self.country_code or self.provider.country_code(),
            latitude=self.provider.latitude(),
            longitude=self.provider.longitude(),
            state=self.state or self.provider.state(),
            street_name=self.street_name or self.provider.street_name(),
            street_number=self.street_number or self.provider.street_number(),
            street_suffix=self.street_suffix or self.provider.street_suffix(),
            zip_code=self.zip_code or self.provider.zip_code()
        )
