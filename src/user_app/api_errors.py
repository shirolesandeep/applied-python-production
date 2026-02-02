from fastapi import HTTPException

from src.user_app.errors import (
    InvalidUserAgeError,
    InvalidUserDataError,
)


def map_domain_error(exc: Exception) -> HTTPException:
    if isinstance(exc, InvalidUserAgeError):
        return HTTPException(status_code=400, detail=str(exc))

    if isinstance(exc, InvalidUserDataError):
        return HTTPException(status_code=422, detail="Invalid user data")

    return HTTPException(status_code=500, detail="Internal server error")
