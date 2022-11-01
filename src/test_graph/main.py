import logging
import logging.config

import pandas as pd
import os

from test_graph.load.loader import load_data, dump_graph_data
from test_graph.preprocessing.preprocess import run_preprocess
from test_graph.graph.compute import get_graph
from test_graph.conf_utils import configure_logging

configure_logging("logging.yaml")
_logger = logging.getLogger(__name__)


def run(path_drugs: str, path_trials: str, path_pubmed: str, path_graph: str):
    drugs, trials, pubmed = load_data(path_drugs, path_trials, path_pubmed)
    _logger.info("Data loaded")
    drugs, trials, pubmed = run_preprocess(drugs, trials, pubmed)
    _logger.info("Data processed")
    graph = get_graph(drugs, pubmed, trials)
    _logger.info("Graph computed")
    dump_graph_data(graph, path_graph)
    _logger.info("Graph dumped to JSON")


if __name__ == "__main__":
    path_drugs, path_trials, path_pubmed, path_graph = "data/drugs.csv", "data/clinical_trials.csv", "data/pubmed.csv", "output/graph.json"
    run(path_drugs, path_trials, path_pubmed, path_graph)
