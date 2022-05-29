#!/usr/bin/env python
from enum import auto
from enum import Enum
from enum import unique


@unique
class EventType(Enum):
    address = auto()
    person = auto()
    random_sentence = auto()
    random_sentences = auto()
    sentence_limits = auto()
    lorem_limits = auto()
    lorem_bytes = auto()
    lorem_words = auto()
    lorem_paragraphs = auto()
    lorem_paragraphs_break = auto()
    lorem_lists = auto()
    uuid = auto()
