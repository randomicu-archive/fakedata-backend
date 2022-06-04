#!/usr/bin/env python
from enum import auto
from enum import Enum
from enum import unique


@unique
class EventType(Enum):
    ADDRESS = 'address'
    PERSON = 'person'
    RANDOM_SENTENCE = 'random_sentence'
    RANDOM_SENTENCES = 'random_sentences'
    SENTENCE_LIMITS = 'sentence_limits'
    LOREM_LIMITS = 'lorem_limits'
    LOREM_BYTES = 'lorem_bytes'
    LOREM_WORDS = 'lorem_words'
    LOREM_PARAGRAPHS = 'lorem_paragraphs'
    LOREM_PARAGRAPHS_BREAK = 'lorem_paragraphs_break'
    LOREM_LISTS = 'lorem_lists'
    UUID = 'uuid'


@unique
class ProviderType(Enum):
    ADDRESS = auto()
    PERSON = auto()
    REGIONAL_RU = auto()


@unique
class Locale(Enum):
    EN = 'en'
    RU = 'ru'
