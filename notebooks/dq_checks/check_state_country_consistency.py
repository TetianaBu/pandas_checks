import pandas as pd


def check_state_country_consistency(df):
    # Valid US state codes
    valid_us_states = {
        'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA',
        'HI','ID','IL','IN','IA','KS','KY','LA','ME','MD',
        'MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
        'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC',
        'SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',
        'DC'
    }
 
    # Define condition: when country is US, state must be valid US state
    def is_valid(row):
        state = row['state']
        country = row['country']
        if country == 'USA':
            return state in valid_us_states
        else:
            return isinstance(state, str) and (len(state) == 2 or state == "NA")
 
    # Apply the rule
    invalid_rows = df[~df.apply(is_valid, axis=1)]
 
    status = "Passed" if invalid_rows.empty else "Failed"
    return status, invalid_rows[['state', 'country']]