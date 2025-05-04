import pandas as pd
 
def check_missing_values(value):
    if pd.isna(value):
        return True
    if isinstance(value, str) and value.strip().lower() in {'null', 'nan', 'none'}:
        return True
    return False
 
def check_completeness_by_records(df):
    # Apply missing value check across the DataFrame
    missing_mask = df.map(check_missing_values)
 
    # Identify any rows with at least one missing value
    invalid_rows = df[missing_mask.any(axis=1)]
 
    status = "Passed" if invalid_rows.empty else "Failed"
 
    return status, invalid_rows