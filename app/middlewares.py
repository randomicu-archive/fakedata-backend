#!/usr/bin/env python
from http import HTTPStatus

from app.enums import Locale
from fastapi import HTTPException
from starlette.requests import Request


async def verify_locale(request: Request):
    """
    Used as middleware for the requests to check if requested URL path is in allowed set
    """

    allowed_locales: list[str] = [_.value for _ in Locale]

    if (request.path_params['lang'] and request.path_params['lang']) not in allowed_locales:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Incorrect locale')
