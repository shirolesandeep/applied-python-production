class UserAppError(Exception):
    """Base class for all user_app domain errors."""


class InvalidUserDataError(UserAppError):
    """Raised when user JSON data is invalid."""


class InvalidUserAgeError(UserAppError):
    """Raised when user age is missing or invalid."""
