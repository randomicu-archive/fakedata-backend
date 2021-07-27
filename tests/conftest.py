#!/usr/bin/env python
import os
from typing import Generator

import pytest
from starlette.testclient import TestClient

from app.main import app


# TODO: add settings override or add configuration app for ci environment
def get_test_database():
    if os.environ.get('CI'):
        return os.getenv('FAKEDATA_DATABASE_URL')
    else:
        return os.getenv('FAKEDATA_TEST_DATABASE_URL')


TEST_DATABASE_URL = get_test_database()


@pytest.fixture(scope='session')
def client() -> Generator[TestClient, None, None]:
    yield TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def setup_test_db():
    yield TEST_DATABASE_URL
