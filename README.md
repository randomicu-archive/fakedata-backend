# fakedata-backend

|    CI Type     |                                                                                                 Status                                                                                                 |
|:--------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|     Tests      | [![Run tests](https://github.com/randomicu/fakedata-backend/actions/workflows/testing.yml/badge.svg)](https://github.com/randomicu/fakedata-backend/actions/workflows/testing.yml)                     |
| Image Building | [![Test image building](https://github.com/randomicu/fakedata-backend/actions/workflows/docker_build.yml/badge.svg)](https://github.com/randomicu/fakedata-backend/actions/workflows/docker_build.yml) |


random.icu companion service with internal API for data generation.

## Available providers

1. Address
2. Person

## Development

Run `uvicorn` in development mode on 8000 port (with autoreload) from repo root:

`PYTHONPATH=$(pwd) uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000`

In some cases PyCharm could not run docker-compose services. Fix is [here](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000174084-docker-compose-does-not-work-on-ubuntu-using-default-settings).

### Version management

Install tbump first: `pipx install tbump`

First, commit changes and run `tbump --no-push new_version`

Verify local tag and push it too: `git push origin new_version`

## Deployment

Deploy notes.

## Testing

Run this command from repo root to run all tests:

`PYTHONPATH=$(pwd) pytest -s tests`
