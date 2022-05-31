#!/usr/bin/env python
import abc


class Response(abc.ABC):

    @abc.abstractmethod
    def generate(self):
        ...
