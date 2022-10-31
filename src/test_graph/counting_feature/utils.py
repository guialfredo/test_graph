from typing import List, Dict, Any

import pandas as pd


def get_unique_journals(df: pd.DataFrame) -> List[str]:
    return list(df.journal.unique())


def get_drug_ids_from_graph(data: Dict[str, Any]) -> List[str]:
    return list(data.keys())
