import logging.config 
import os
import yaml 

_logger = logging.getLogger(__name__)

def configure_logging(log_config: str):
    """Configure logging from YAML file"""
    if log_config:
        if os.path.exists(log_config):
            with open(log_config, "rt") as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
        else:
            _logger.warning(f"Log configuration file not found {log_config}")