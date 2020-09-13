#!/usr/bin/env python
import uvicorn

from app.main import app  # noqa: F401
# noinspection PyUnresolvedReferences

if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8000, workers=1, reload=True)
