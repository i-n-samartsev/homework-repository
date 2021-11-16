import os

import homework2.task1


def test_get_longest_diverse_words():
    assert homework2.task1.get_longest_diverse_words(
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
        homework2.task1.get_rarest_char(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == "›"
    )


def test_count_punctuation_chars():
    assert (
        homework2.task1.count_punctuation_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == 3916
    )


def test_count_non_ascii_chars():
    assert (
        homework2.task1.count_non_ascii_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == 2237
    )


def test_get_most_common_non_ascii_char():
    assert (
        homework2.task1.get_most_common_non_ascii_char(
            os.getcwd() + "/homework2/" + "test_task1_data.txt"
        )
        == "ä"
    )
