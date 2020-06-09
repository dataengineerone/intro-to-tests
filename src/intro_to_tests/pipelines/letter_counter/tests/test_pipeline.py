
from kedro.runner import SequentialRunner

from ..pipeline import create_pipeline


def test_letter_counter_pipeline(basic_catalog):
    runner = SequentialRunner()
    output_name = 'outputs'

    pipeline = create_pipeline(inputs='basic_data', outputs=output_name)

    pipeline_output = runner.run(pipeline, basic_catalog)

    assert pipeline_output[output_name] == {
        'J': 1,
        'O': 1,
        'H': 1,
        'N': 1,
        'M': 1,
        'I': 2,
        'K': 1,
        'E': 1,
        'D': 2,
        'A': 1,
        'V': 1,
    }
