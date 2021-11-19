from homework3.task03 import make_filter, Filter.apply


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_positive(input_data, output_data):
    assert make_filter(name="polly", type="bird").apply(sample_data) == {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
    }
