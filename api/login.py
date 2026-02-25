import logging
import logging.config
import yaml
import os
from pathlib import Path


def setup_logging():
    current_dir = Path(__file__).resolve().parent
    default_path = current_dir.parent / "logging_config.yaml"

    default_level = logging.INFO

    path = os.getenv("LOGGING_CONFIG", default_path)
    if os.path.exists(path):
        with open(path, "r") as stream:
            config = yaml.safe_load(stream)

            log_dir = Path('logs')
            log_dir.mkdir(exist_ok=True)

            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()
logger = logging.getLogger(__name__)