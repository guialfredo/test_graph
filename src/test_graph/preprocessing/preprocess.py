from typing import Tuple

import pandas as pd

from test_graph.preprocessing.date_utils import to_datetime
from test_graph.preprocessing.text_cleaning import clean_case


def run_preprocess(drugs, trials, pubmed) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    trials = to_datetime(trials)
    pubmed = to_datetime(pubmed)
    return clean_case(drugs, trials, pubmed)
