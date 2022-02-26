import os

from backend.config import config as application_config


def get_environment_configs():
    """
    To set application config based on environment
    :return cfg: class instance holding all configs
    """

    cfg = application_config.DevConfig

    return cfg
