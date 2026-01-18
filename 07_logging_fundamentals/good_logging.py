import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


def load_config(path: str) -> dict:
    logger.info("Loading config from path: %s", path)

    if not path:
        logger.error("Config path is empty")
        raise ValueError("path must not be empty")

    logger.info("Config loaded successfully")
    return {"env": "dev"}
