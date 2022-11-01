import pandas as pd
import re

def to_lowercase(df: pd.DataFrame, col: str) -> pd.DataFrame:
    df[col] = df[col].str.lower()
    return df


def clean_trials_pubmed_case(df: pd.DataFrame) -> pd.DataFrame:
    return df.pipe(to_lowercase, col="journal").pipe(
        to_lowercase, col="title")


def handle_encoding_error(s):
    """util for dealing with encoding errors

    :param s: input str
    :type s: str
    :return: cleaned str
    :rtype: str
    """
    if isinstance(s, str):
        return re.sub(r"\\x\w\d+", "", s)
    else:
        return s