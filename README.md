# Randomicu-fakedata

random.icu companion service with internal API for data generation from Mimesis providers.

## Available providers

1. Address
2. Person

## Development

Run `uvicorn` in development mode on 8000 port (with autoreload) from repo root:

`PYTHONPATH=$(pwd) uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000`

In some cases PyCharm could not run docker-compose services. Fix is [here](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000174084-docker-compose-does-not-work-on-ubuntu-using-default-settings).

## Deployment

Deploy notes.

## Testing

Run this command from repo root to run all tests:

`PYTHONPATH=$(pwd) pytest -s tests`
