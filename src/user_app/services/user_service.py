import json
import logging
from typing import Dict

logger = logging.getLogger(__name__)


class UserService:
    """Service responsible for user-related processing."""

    def __init__(self, raw_data: str) -> None:
        self.raw_data = raw_data
        self.user: Dict[str, object] = {}

    def parse_user(self) -> None:
        logger.debug("Parsing user JSON")
        self.user = json.loads(self.raw_data)

    def is_adult(self) -> bool:
        age = self.user.get("age")
        if not isinstance(age, int):
            logger.error("Invalid age value: %s", age)
            raise ValueError("User age must be an integer")

        logger.info("User age validated: %s", age)
        return age >= 18

    def process(self) -> str:
        logger.info("Starting user processing")
        self.parse_user()
        result = "User is adult" if self.is_adult() else "User is minor"
        logger.info("Processing result: %s", result)
        return result
