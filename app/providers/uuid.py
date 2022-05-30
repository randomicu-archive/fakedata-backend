#!/usr/bin/env python
import uuid


def get_data(uppercase: bool, version: int):
    random_uid = str(uuid.uuid4())

    data = {
        'uuid': {
            'uuid': random_uid if not uppercase else random_uid.upper(),
            'version': version,
        },
        'uppercase': uppercase
    }

    return data
