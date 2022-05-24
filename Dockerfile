FROM ghcr.io/randomicu/fakedata-backend-base:1.0.7 as builder-dev

RUN set -eux && \
    apt-get install --yes --no-install-recommends build-essential

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-dev

# Development image
FROM ghcr.io/randomicu/fakedata-backend-base:1.0.7

WORKDIR $PYSETUP_PATH
COPY --from=builder-dev $POETRY_HOME $POETRY_HOME
RUN true
COPY --from=builder-dev $PYSETUP_PATH $PYSETUP_PATH

RUN poetry install --no-root

WORKDIR /usr/src/randomicu-fakedata

COPY . ./
COPY ./deploy/start.sh ./start.sh

RUN chown -R fakedata:fakedata /usr/src/randomicu-fakedata

USER fakedata

CMD ["/usr/src/randomicu-fakedata/start.sh"]
