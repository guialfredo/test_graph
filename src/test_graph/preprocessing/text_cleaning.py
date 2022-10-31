import pandas as pd
from typing import Tuple


def to_lowercase(df: pd.DataFrame, col: str) -> pd.DataFrame:
    df[col] = df[col].str.lower()
    return df


def clean_trials_pubmed_case(df: pd.DataFrame) -> pd.DataFrame:
    return df.pipe(to_lowercase, col="journal").pipe(
        to_lowercase, col="title")


def clean_case(drugs: pd.DataFrame, trials: pd.DataFrame, pubmed: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    pubmed_clean, trials_clean = clean_trials_pubmed_case(
        pubmed), clean_trials_pubmed_case(trials)
    drugs_clean = drugs.pipe(to_lowercase, col="drug")
    return drugs_clean, trials_clean, pubmed_clean
