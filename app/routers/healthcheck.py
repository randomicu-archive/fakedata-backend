#!/usr/bin/env python
from fastapi import APIRouter

from app import __version__
from app.models.schema.healthcheck import HealthcheckSchema


router = APIRouter()


@router.get('/health')
async def get_health():
    data = {
        'version': __version__,
        'status': 'UP'
    }

    return HealthcheckSchema(**data)
