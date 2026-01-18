from typing import Dict


def get_user_age(user: Dict[str, object]) -> int:
    """
    Extract the user's age from a user dictionary.

    Args:
        user: Dictionary containing user information.
              Must include an integer 'age' field.

    Returns:
        The user's age as an integer.

    Raises:
        KeyError: If 'age' key is missing.
        ValueError: If 'age' is not an integer.
    """
    age = user.get("age")

    if age is None:
        raise KeyError("user dictionary must contain 'age'")

    if not isinstance(age, int):
        raise ValueError("user age must be an integer")

    return age
