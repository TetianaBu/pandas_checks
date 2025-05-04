import pandas as pd


def check_cancellation_code_consistency(df):
    # Identify invalid rows
    invalid_rows = df[
        ((df['Cancelled'] == '0') & (df['CancellationCode'].notnull()) & (df['CancellationCode'] != "")) |
        ((df['Cancelled'] == '1') & (~df['CancellationCode'].isin(['A', 'B', 'C'])))
    ]
 
    status = "Passed" if invalid_rows.empty else "Failed"
    return status, invalid_rows[['Cancelled', 'CancellationCode']]