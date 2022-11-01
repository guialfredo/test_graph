from typing import Dict, Any

import pandas as pd


def find_mention(df: pd.DataFrame, drug_str: str) -> pd.DataFrame:
    """get subset of data that mentions drug

    :param df: pubmed or clinical trials data
    :type df: pd.DataFrame
    :param drug_str: name of considered drug
    :type drug_str: str
    :return: subset of data that mentions drug
    :rtype: pd.DataFrame
    """
    return df[df["title"].str.contains(drug_str)]


def get_article_infos(mention_subset: pd.DataFrame) -> Dict[Any, str]:
    """get article infos as dict from subset data

    :param mention_subset: subset of data mentioning some drug
    :type mention_subset: pd.DataFrame
    :return: article infos as dict
    :rtype: Dict[Any, str]
    """
    return mention_subset[["title", "date"]].to_dict()


def get_journal_infos(mention_subset_pubmed: pd.DataFrame, mention_subset_trials: pd.DataFrame) -> Dict[Any, str]:
    """get journal infos as dict from both pubmed and clinical trials subsets

    :param mention_subset_pubmed: pubmed data subset mentioning some drug
    :type mention_subset_pubmed: pd.DataFrame
    :param mention_subset_trials: clinical trials subset mentioning some drug
    :type mention_subset_trials: pd.DataFrame
    :return: infos on journals mentioning some drug
    :rtype: Dict[Any, str]
    """
    subset = pd.concat([mention_subset_pubmed, mention_subset_trials])
    return subset[["journal", "date"]].groupby(["journal", "date"]).size().to_frame("size").reset_index().to_dict()
