#!/usr/bin/env python
import logging
from functools import lru_cache

from pydantic import BaseSettings
from pydantic import PostgresDsn

from app.enums import Environment


log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    database_url: PostgresDsn = None
    environment: Environment

    class Config:
        env_prefix = 'FAKEDATA_'


class CISettings(Settings):
    environment: Environment = Environment.CI
    database_url: PostgresDsn = 'postgresql+asyncpg://postgres:password@localhost/fakedata'


class DevSettings(Settings):
    environment: Environment = Environment.DEV
    database_url: PostgresDsn = 'postgresql+asyncpg://postgres:password@172.19.0.10/fakedata'


class ProdSettings(Settings):
    environment: Environment = Environment.PRODUCTION
    database_url: PostgresDsn


class FactorySettings:
    def __init__(self, environment):
        self.environment = environment

    def get_env(self):
        environments = {
            'dev': DevSettings,
            'ci': CISettings,
            'production': ProdSettings
        }
        settings = environments[self.environment.value]
        return settings()


@lru_cache
def get_settings() -> Settings:
    env = Settings().environment
    log.info('Loading settings for the environment: %s', env.value)
    return FactorySettings(environment=env).get_env()
