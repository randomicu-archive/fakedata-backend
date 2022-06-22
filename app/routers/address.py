#!/usr/bin/env python
import secrets

from fastapi import APIRouter
from fastapi import Depends

from app.enums import EventType
from app.helpers.event import Event
from app.middlewares import verify_locale
from app.models.schema.address import RootAddressSchema
from app.responses.address import AddressResponse

router = APIRouter()


@router.get('/{locale}/address',
            dependencies=[Depends(verify_locale)],
            response_model=RootAddressSchema,
            response_model_exclude_none=True)
async def get_address(locale: str,
                      seed: str | None = None,
                      count: int = 1,
                      address: str | None = None,
                      calling_code: int | None = None,
                      city: str | None = None,
                      continent: str | None = None,
                      country: str | None = None,
                      country_code: str | None = None,
                      state: str | None = None,
                      street_name: str | None = None,
                      street_number: str | None = None,
                      street_suffix: str | None = None,
                      zip_code: int | str | None = None
                      ):

    if not seed:
        seed = secrets.token_hex(16)

    address_response: AddressResponse = AddressResponse(locale=locale,
                                                        seed=seed,
                                                        address=address,
                                                        calling_code=calling_code,
                                                        city=city,
                                                        continent=continent,
                                                        country=country,
                                                        country_code=country_code,
                                                        state=state,
                                                        street_name=street_name,
                                                        street_number=street_number,
                                                        street_suffix=street_suffix,
                                                        zip_code=zip_code)

    responses = []
    if count >= 1:
        for _ in range(count):
            responses.append(address_response.generate())

    await Event.send_event(event_type=EventType.address, language=locale)
    return RootAddressSchema(result=responses, seed=seed)
