from typing import Tuple

import pandas as pd

from test_graph.preprocessing.date_utils import to_datetime
from test_graph.preprocessing.text_cleaning import run_text_cleaning


def run_preprocess(drugs, trials, pubmed) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    trials = to_datetime(trials)
    pubmed = to_datetime(pubmed)
    return run_text_cleaning(drugs, trials, pubmed)
