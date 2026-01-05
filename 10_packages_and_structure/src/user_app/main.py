from user_app.services.user_service import UserService


def main() -> None:
    service = UserService('{"name": "Amit", "age": 20}')
    print(service.process())


if __name__ == "__main__":
    main()
