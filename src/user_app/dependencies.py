import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger instance.
    Dependency factory.
    """
    return logging.getLogger(name)
