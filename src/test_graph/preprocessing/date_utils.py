from typing import Tuple

import pandas as pd


def to_datetime(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    df = df.assign(date=pd.to_datetime(df[date_col]))
    return df.assign(date=df["date"].astype(str))


def run_date_cleaning(drugs: pd.DataFrame, trials: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return to_datetime(drugs), to_datetime(trials)
