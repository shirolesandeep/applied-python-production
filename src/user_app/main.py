from .config import load_config
from .logging_config import setup_logging
from .services.user_service import UserService


def main() -> None:
    config = load_config()
    setup_logging(config.log_level)

    service = UserService('{"name": "Amit", "age": 20}')
    result = service.process(verbose=config.enable_verbose_output)
    print(result)


if __name__ == "__main__":
    main()
