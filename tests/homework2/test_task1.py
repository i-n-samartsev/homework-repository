import os

import homework2.task1


def test_get_longest_diverse_words():
    assert homework2.task1.get_longest_diverse_words(
        os.getcwd() + "/homework2/" + "test_task1_data.txt", "unicode-escape"
    ) == [
        "unmißverständliche",
        "Kollektivschuldiger,",
        "résistance-Bewegungen,",
        "Schicksalsfiguren;",
        "Machtbewußtsein,",
        "politisch-strategischen",
        "Bevölkerungsabschub,",
        "Zwingherrschaft.",
        "Gewissenserforschung,",
        "Selbstverständlich",
    ]


def test_get_rarest_char():
    assert (
        homework2.task1.get_rarest_char(
            os.getcwd() + "/homework2/" + "test_task1_data.txt",
            "unicode-escape",
        )
        == "›"
    )


def test_count_punctuation_chars():
    assert (
        homework2.task1.count_punctuation_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt",
            "unicode-escape",
        )
        == 5125
    )


def test_count_non_ascii_chars():
    assert (
        homework2.task1.count_non_ascii_chars(
            os.getcwd() + "/homework2/" + "test_task1_data.txt",
            "unicode-escape",
        )
        == 2972
    )


def test_get_most_common_non_ascii_char():
    assert (
        homework2.task1.get_most_common_non_ascii_char(
            os.getcwd() + "/homework2/" + "test_task1_data.txt",
            "unicode-escape",
        )
        == "ä"
    )
