import re
from math import ceil


def word_count(text: str) -> int:
    """
    Returns the total number of words.
    """
    return len(text.split())


def character_count(text: str) -> int:
    """
    Returns total number of characters.
    """
    return len(text)


def sentence_count(text: str) -> int:
    """
    Counts sentences using punctuation.
    """
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def paragraph_count(text: str) -> int:
    """
    Counts paragraphs.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def average_words_per_sentence(text: str) -> float:
    """
    Calculates average sentence length.
    """
    sentences = sentence_count(text)

    if sentences == 0:
        return 0

    return round(word_count(text) / sentences, 2)


def reading_time(text: str) -> int:
    """
    Estimates reading time in minutes.
    Assumes 200 words per minute.
    """
    words = word_count(text)

    return max(1, ceil(words / 200))


def readability_score(text: str) -> float:
    """
    Very simple readability heuristic.

    Higher score = easier to read.
    """

    avg = average_words_per_sentence(text)

    if avg <= 12:
        return 10.0

    if avg <= 16:
        return 9.0

    if avg <= 20:
        return 8.0

    if avg <= 25:
        return 7.0

    if avg <= 30:
        return 6.0

    return 5.0


def content_statistics(text: str):
    """
    Returns all locally calculated metrics.
    """

    return {

        "word_count": word_count(text),

        "character_count": character_count(text),

        "sentence_count": sentence_count(text),

        "paragraph_count": paragraph_count(text),

        "average_words_per_sentence":
            average_words_per_sentence(text),

        "estimated_reading_time_minutes":
            reading_time(text),

        "readability_score":
            readability_score(text)
    }