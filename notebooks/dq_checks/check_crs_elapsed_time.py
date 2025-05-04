import pandas as pd
 
 
def hhmm_to_minutes_safe(val):
    """
    Convert HHMM to minutes since midnight.
    Handles strings, floats, NaNs, etc.
    """
    try:
        if pd.isna(val):
            return None
        val_str = str(val).strip()
        if not val_str.isdigit():
            return None
        val_int = int(val_str)
        hours = val_int // 100
        minutes = val_int % 100
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return hours * 60 + minutes
    except:
        return None
    return None
 
def check_crs_elapsed_time(df):
    df = df.copy()
 
    # Ensure CRSElapsedTime is numeric
    df['CRSElapsedTime'] = pd.to_numeric(df['CRSElapsedTime'], errors='coerce')
 
    # Drop rows with missing CRS times or elapsed time
    df = df.dropna(subset=['CRSDepTime', 'CRSArrTime', 'CRSElapsedTime'])
 
    # Convert to minutes
    df['DepMinutes'] = df['CRSDepTime'].apply(hhmm_to_minutes_safe)
    df['ArrMinutes'] = df['CRSArrTime'].apply(hhmm_to_minutes_safe)
 
    # Drop rows where conversion failed
    df = df.dropna(subset=['DepMinutes', 'ArrMinutes'])
 
    # Calculate elapsed time
    df['CalculatedElapsed'] = df['ArrMinutes'] - df['DepMinutes']
    df.loc[df['CalculatedElapsed'] < 0, 'CalculatedElapsed'] += 24 * 60  # overnight adjustment
 
    # Force to integer
    df['CalculatedElapsed'] = df['CalculatedElapsed'].astype(int)
 
    # Strict 1:1 match
    invalid_rows = df[df['CalculatedElapsed'] != df['CRSElapsedTime']]
 
    # Status
    status = "Passed" if invalid_rows.empty else "Failed"
 
    return status, invalid_rows[['CRSDepTime', 'CRSArrTime', 'CRSElapsedTime', 'CalculatedElapsed']]