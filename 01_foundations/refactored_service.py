import json
from typing import Dict


class UserService:
    """
    Service responsible for user-related processing.

    This class is import-safe:
    - No code executes on import
    - All execution is explicit
    """

    def __init__(self, raw_data: str) -> None:
        self.raw_data = raw_data
        self.user: Dict[str, object] = {}

    def parse_user(self) -> None:
        """Parse raw JSON user data safely."""
        try:
            self.user = json.loads(self.raw_data)
        except json.JSONDecodeError as exc:
            raise ValueError("Invalid user JSON data") from exc

    def is_adult(self) -> bool:
        """Check if user is an adult."""
        age = self.user.get("age")
        if not isinstance(age, int):
            raise ValueError("User age must be an integer")
        return age >= 18

    def process(self) -> str:
        """
        Orchestrate user processing.

        Returns:
            A human-readable result string.
        """
        self.parse_user()
        return "User is adult" if self.is_adult() else "User is minor"


if __name__ == "__main__":
    # This block runs ONLY when this file is executed directly
    service = UserService(
        raw_data='{"name": "Sandeep", "age": 38, "active": true}'
    )
    result = service.process()
    print(result)
