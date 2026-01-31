import pytest

from src.user_app.services.user_service import UserService
from tests.fake_logger import FakeLogger


def test_adult_user_returns_adult():
    logger = FakeLogger()
    service = UserService(
        raw_data='{"name": "Amit", "age": 25}',
        logger=logger,
    )

    result = service.process()
    assert result == "User is adult"


def test_minor_user_returns_minor():
    logger = FakeLogger()
    service = UserService(
        raw_data='{"name": "Amit", "age": 15}',
        logger=logger,
    )

    result = service.process()
    assert result == "User is minor"


def test_invalid_age_raises_error():
    logger = FakeLogger()
    service = UserService(
        raw_data='{"name": "Amit", "age": "twenty"}',
        logger=logger,
    )

    with pytest.raises(ValueError):
        service.process()


def test_verbose_logs_user_data():
    logger = FakeLogger()
    service = UserService(
        raw_data='{"name": "Amit", "age": 25}',
        logger=logger,
    )

    service.process(verbose=True)

    assert any(
        "Verbose mode enabled" in message
        for _, message in logger.messages
    )
