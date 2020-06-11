from typing import Dict

from pandas import DataFrame
import great_expectations as ge


def check_iris_data(df: DataFrame):
    gdf = ge.from_pandas(df)
    result = gdf.expect_column_values_to_be_in_set(
        "species", ["setosa", "virginica", "versicolor"], mostly=0.99
    )

    if not result.success:
        raise Exception("iris data is no good")

    return df
