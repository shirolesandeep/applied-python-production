import json
import logging
from typing import Dict


class UserService:
    """Service responsible for user-related processing."""

    def __init__(self, raw_data: str, logger: logging.Logger) -> None:
        self.raw_data = raw_data
        self.user: Dict[str, object] = {}
        self.logger = logger

    def parse_user(self) -> None:
        self.logger.debug("Parsing user JSON")
        self.user = json.loads(self.raw_data)

    def is_adult(self) -> bool:
        age = self.user.get("age")
        if not isinstance(age, int):
            self.logger.error("Invalid age value: %s", age)
            raise ValueError("User age must be an integer")

        self.logger.info("User age validated: %s", age)
        return age >= 18

    def process(self, verbose: bool = False) -> str:
        self.logger.info("Starting user processing")
        self.parse_user()

        if verbose:
            self.logger.info("Verbose mode enabled: user data = %s", self.user)

        result = "User is adult" if self.is_adult() else "User is minor"
        self.logger.info("Processing result: %s", result)
        return result
