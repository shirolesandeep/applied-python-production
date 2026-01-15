from user_app.config import load_config
from user_app.logging_config import setup_logging
from user_app.services.user_service import UserService


def main() -> None:
    config = load_config()
    setup_logging(config.log_level)

    service = UserService('{"name": "Amit", "age": 20}')
    print(service.process())


if __name__ == "__main__":
    main()
