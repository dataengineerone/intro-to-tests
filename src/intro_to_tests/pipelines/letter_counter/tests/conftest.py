import pandas as pd
import pytest


@pytest.fixture(scope='module')
def basic_data():
    basic_name_data = pd.DataFrame({
        'names': [
            'john',
            'mike',
            'david',
        ]
    })
    return basic_name_data


@pytest.fixture(scope='module')
def basic_catalog(basic_data):
    from kedro.io import DataCatalog, MemoryDataSet
    catalog = DataCatalog({
        'basic_data': MemoryDataSet()
    })
    catalog.save('basic_data', basic_data)
    return catalog
