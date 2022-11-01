from typing import Dict, Any

import pandas as pd

from test_graph.graph.utils import find_mention, get_journal_infos, get_article_infos


def create_dict_infos(pubmed: pd.DataFrame, trials: pd.DataFrame, drug_str: str) -> Dict[str, Any]:
    """performs all steps required to compute one drug relationships within the graph :
    1. Find pubmed articles that mention the drug
    2. Find clinical trials aticles that mention the drug
    3. Get all infos as dict from journals mentioning the drug, whether from pubmed or trials data
    4. Get all infos as dict from articles mentioning the drug
    5. Store info in a dict with keys pubmed_articles, journal, trials


    :param pubmed: pubmed dataframe
    :type pubmed: pd.DataFrame
    :param trials: clinical trials dataframe
    :type trials: pd.DataFrame
    :param drug_str: current drug code
    :type drug_str: str
    :return: graph of relationships for current drug
    :rtype: Dict[str, Any]
    """
    sub_pubmed = find_mention(pubmed, drug_str)
    sub_trials = find_mention(trials, drug_str)
    pubmed_articles, trials_articles = get_article_infos(
        sub_pubmed), get_article_infos(sub_trials)
    journal_infos = get_journal_infos(sub_pubmed, sub_trials)
    return dict(pubmed_articles=pubmed_articles, journal=journal_infos, trials=trials_articles)


def get_graph(drugs: pd.DataFrame, pubmed: pd.DataFrame, trials: pd.DataFrame) -> Dict[str, Any]:
    """loops over all drug codes to compute the whole graph
    Should ideally be parallelized 

    :param drugs: drugs dataframe
    :type drugs: pd.DataFrame
    :param pubmed: pubmed dataframe
    :type pubmed: pd.DataFrame
    :param trials: clinical trials dataframe
    :type trials: pd.DataFrame
    :return: complete graph of relationships for all drugs
    :rtype: Dict[str, Any]
    """
    graph_dict = dict()
    for i in range(len(drugs)):
        infos = drugs.iloc[i]
        atccode = infos["atccode"]
        drug_str = infos["drug"]
        graph_dict[atccode] = create_dict_infos(pubmed, trials, drug_str)
    return graph_dict
