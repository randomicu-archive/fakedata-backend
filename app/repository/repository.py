#!/usr/bin/env python
import abc

import sqlalchemy


class Repository(abc.ABC):

    @property
    @abc.abstractmethod
    def table(self) -> sqlalchemy.Table:
        ...
