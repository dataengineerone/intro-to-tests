import pandas as pd

from ..nodes import upper_caser, count_letters


def test_upper_caser_is_upper_casing_things(basic_data):

    output = upper_caser(basic_data)

    assert output.equals(pd.DataFrame({
        'names': [
            'JOHN',
            'MIKE',
            'DAVID'
        ]
    }))


def test_counter_is_counting_things(basic_data):

    output = count_letters(basic_data)
    assert output == {
        'j': 1,
        'o': 1,
        'h': 1,
        'n': 1,
        'm': 1,
        'i': 2,
        'k': 1,
        'e': 1,
        'd': 2,
        'a': 1,
        'v': 1,
    }
