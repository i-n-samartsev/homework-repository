from homework3.task03 import make_filter


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_positive():
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]


def test_negative_key_out():
    assert make_filter(n="polly", type="bird").apply(sample_data) != [
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]


def test_negative_all_key_read():
    assert make_filter(name="py", type="bird").apply(sample_data) != [
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]
