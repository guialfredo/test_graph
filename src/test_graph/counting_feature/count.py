from typing import Dict, Any, List

from test_graph.counting_feature.utils import get_unique_journals, get_drug_ids_from_graph

import pandas as pd


def get_journal_unique_list(data: Dict[str, Any], drug_codes: List[str]) -> List[str]:
    """get list of unique journals mentioned for all drugs

    :param data: graph data
    :type data: Dict[str, Any]
    :param drug_codes: drug IDs
    :type drug_codes: List[str]
    :return: concatenated list of unique journals mention for each drug
    :rtype: str
    """
    init_drug_unique_journals = get_unique_journals(
        pd.DataFrame(data[drug_codes[0]]["journal"]))
    for code in drug_codes[1:]:
        current_drug_info = pd.DataFrame(data[code]["journal"])
        current_drug_unique_journals = get_unique_journals(current_drug_info)
        init_drug_unique_journals = init_drug_unique_journals + current_drug_unique_journals
    return init_drug_unique_journals

def get_journal_with_max_drugs_from_list(unique_journals_list: List[str]) -> str:
    return max(unique_journals_list, key=unique_journals_list.count)


def run_count_journal_with_max_drugs(data: Dict[str, Any]) -> str:
    drug_codes = get_drug_ids_from_graph(data)
    unique_journals_list = get_journal_unique_list(data, drug_codes)
    return get_journal_with_max_drugs_from_list(unique_journals_list)
