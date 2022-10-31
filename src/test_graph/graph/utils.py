from typing import Dict, Any

import pandas as pd


def find_mention(df: pd.DataFrame, drug_str: str) -> pd.DataFrame:
    return df[df["title"].str.contains(drug_str)]


def get_article_infos(mention_subset: pd.DataFrame) -> Dict[Any, str]:
    return mention_subset[["title", "date"]].to_dict()


def get_journal_infos(mention_subset_pubmed: pd.DataFrame, mention_subset_trials: pd.DataFrame) -> Dict[Any, str]:
    subset = pd.concat([mention_subset_pubmed, mention_subset_trials])
    return subset[["journal", "date"]].groupby(["journal", "date"]).size().to_frame("size").reset_index().to_dict()
