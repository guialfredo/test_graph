from typing import Tuple, Dict, Any
import json

import pandas as pd

def load_data(path_drugs: str, path_trials: str, path_pubmed: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    drugs = pd.read_csv(path_drugs)
    trials = pd.read_csv(path_trials).rename(columns={"scientific_title":"title"})
    pubmed = pd.read_csv(path_pubmed)
    return drugs, trials, pubmed 


def load_graph_data(path_graph : str) -> Dict[str, Any]:
    with open(path_graph) as json_file:
        data = json.load(json_file)
    return data


def dump_graph_data(data: Dict[str, Any], path_graph: str):
    with open(path_graph, 'w') as fp:
        json.dump(data, fp)