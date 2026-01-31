import pytest

from src.user_app.services.user_service import UserService
from src.user_app.errors import InvalidUserAgeError
from tests.fake_logger import FakeLogger


def test_invalid_age_raises_domain_error():
    logger = FakeLogger()
    service = UserService(
        raw_data='{"name": "Amit", "age": "twenty"}',
        logger=logger,
    )

    with pytest.raises(InvalidUserAgeError):
        service.process()
