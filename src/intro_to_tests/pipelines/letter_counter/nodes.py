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


def count_letters(df: DataFrame):
    letter_counts = {}
    for _, row in df.iterrows():
        for _, col_value in row.items():
            if type(col_value) is str:
                for ch in col_value:
                    letter_counts[ch] = letter_counts.get(ch, 0) + 1
    return letter_counts
