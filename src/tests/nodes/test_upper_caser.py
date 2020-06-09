import pandas as pd

from intro_to_tests.nodes import upper_caser


def test_upper_caser_is_upper_casing_things():
    basic_data = pd.DataFrame({
        'names': [
            'john',
            'mike',
            'david',
        ]
    })

    output = upper_caser(basic_data)

    assert output.equals(pd.DataFrame({
        'names': [
            'JOHN',
            'MIKE',
            'DAVID'
        ]
    }))
