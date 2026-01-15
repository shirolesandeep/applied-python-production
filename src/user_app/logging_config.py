import logging


def setup_logging() -> None:
    """
    Configure application-wide logging.

    This must be called ONCE at the entry point.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
