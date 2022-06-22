#!/usr/bin/env python
from typing import Generator

import pytest
from starlette.testclient import TestClient

from app.config import get_settings
from app.main import app


def get_test_db():
    settings = get_settings()
    return settings.database_url


@pytest.fixture(scope='session')
def client() -> Generator[TestClient, None, None]:
    yield TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def setup_test_db() -> Generator[str | None, None, None]:
    yield get_test_db()
