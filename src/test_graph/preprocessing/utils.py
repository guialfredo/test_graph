import pandas as pd

def handle_id_col(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(id = range(1, len(df)+1))