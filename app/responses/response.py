#!/usr/bin/env python
import abc


class Response(abc.ABC):

    @abc.abstractmethod
    def generate(self):
        ...

    @abc.abstractmethod
    def _generate_schema(self):
        ...
