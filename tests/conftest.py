#!/usr/bin/env python

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    yield TestClient(app)
