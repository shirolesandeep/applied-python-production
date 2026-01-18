from .config import load_config
from .logging_config import setup_logging
from .dependencies import get_logger
from .services.user_service import UserService


def main() -> None:
    config = load_config()
    setup_logging(config.log_level)

    logger = get_logger("src.user_app.services.user_service")

    service = UserService(
        raw_data='{"name": "Amit", "age": 20}',
        logger=logger,
    )

    result = service.process(verbose=config.enable_verbose_output)
    print(result)


if __name__ == "__main__":
    main()
