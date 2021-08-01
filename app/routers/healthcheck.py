#!/usr/bin/env python
from fastapi import APIRouter

from app import __version__
from app.models.schema.healthcheck import HealthcheckSchema


router = APIRouter()


@router.get('/healthcheck')
async def get_status():
    data = {
        'version': __version__,
        'status': 'UP'
    }

    return HealthcheckSchema(**data)
