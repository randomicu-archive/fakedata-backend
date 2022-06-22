#!/usr/bin/env python
from enum import auto
from enum import Enum
from enum import unique


class EventType(str, Enum):
    address = 'address'
    person = 'person'
    random_sentence = 'random_sentence'
    random_sentences = 'random_sentences'
    sentence_limits = 'sentence_limits'
    lorem_limits = 'lorem_limits'
    lorem_bytes = 'lorem_bytes'
    lorem_words = 'lorem_words'
    lorem_paragraphs = 'lorem_paragraphs'
    lorem_paragraphs_break = 'lorem_paragraphs_break'
    lorem_lists = 'lorem_lists'
    uuid = 'uuid'


@unique
class ProviderType(Enum):
    ADDRESS = auto()
    PERSON = auto()
    REGIONAL_RU = auto()


class Locale(Enum):
    EN = 'en'
    RU = 'ru'


class Environment(Enum):
    DEV = 'dev'
    CI = 'ci'
    PRODUCTION = 'production'
