import pandas as pd
from typing import Tuple

from test_graph.preprocessing.text_utils import clean_trials_pubmed_case, to_lowercase, handle_encoding_error


def clean_case(drugs: pd.DataFrame, trials: pd.DataFrame, pubmed: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    pubmed_clean, trials_clean = clean_trials_pubmed_case(
        pubmed), clean_trials_pubmed_case(trials)
    drugs_clean = drugs.pipe(to_lowercase, col="drug")
    return drugs_clean, trials_clean, pubmed_clean


def clean_trials_encoding_error(trials: pd.DataFrame) -> pd.DataFrame:
    """deal with specific clinical trials encoding issue

    :param trials: clinical trials data
    :type trials: pd.DataFrame
    :return: cleaned clinical trials data
    :rtype: pd.DataFrame
    """
    return trials.assign(journal=trials["journal"].apply(lambda x: handle_encoding_error(x)))


def run_text_cleaning(drugs: pd.DataFrame, trials: pd.DataFrame, pubmed: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    drugs_clean, trials_clean, pubmed_clean = clean_case(drugs, trials, pubmed)
    return drugs_clean, clean_trials_encoding_error(trials_clean), pubmed_clean
