from user_app.logging_config import setup_logging
from user_app.services.user_service import UserService


def main() -> None:
    setup_logging()

    service = UserService('{"name": "Amit", "age": 20}')
    result = service.process()
    print(result)


if __name__ == "__main__":
    main()
