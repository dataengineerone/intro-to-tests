from pandas import DataFrame


def upper_caser(df: DataFrame):

    output = []
    for _, row in df.iterrows():
        new_row = {}
        for col_name, col_value in row.items():
            new_value = col_value
            if type(col_value) is str:
                new_value = col_value.upper()
            new_row[col_name] = new_value

        output.append(new_row)

    return DataFrame(output)
