import logging.config
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path)

pytest_plugins = [
    "src.fixtures",
    "src.actions.base",
    "src.actions.wait",
    "src.actions.find",
    "src.actions.action_chains"
]


def pytest_addoption(parser):
    parser.addini("headless", "Run browser in headless mode")
