import os

from homework2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words(
        os.getcwd() + "/homework2/" + "test_task1_data.txt"
    ) == [
        "Kollektivschuldiger,",
        "Werkstättenlandschaft",
        "Schicksalsfiguren;",
        "Machtbewußtsein,",
        "politisch-strategischen",
        "Bevölkerungsabschub,",
        "unmißverständliche",
        "Zwingherrschaft.",
        "Gewissenserforschung,",
        "Selbstverständlich",
    ]


def test_get_rarest_char():
    assert (
        get_rarest_char(os.getcwd() + "/homework2/" + "test_task1_data.txt")
        == ")"
    )


def test_count_punctuation_chars():
    assert (
        count_punctuation_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == 3916
    )


def test_count_non_ascii_chars():
    assert (
        count_non_ascii_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == 2237
    )


def test_get_most_common_non_ascii_char():
    assert (
        get_most_common_non_ascii_char(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == "ä"
    )
