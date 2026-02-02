from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

from src.user_app.services.user_service import UserService
from src.user_app.dependencies import get_logger
from src.user_app.api_errors import map_domain_error


app = FastAPI(title="User Processing API")


class UserRequest(BaseModel):
    """
    API contract for user processing.
    This model enforces STRUCTURAL + BASIC BUSINESS constraints.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="User full name",
        examples=["Amit"],
    )

    age: int = Field(
        ...,
        ge=0,
        le=120,
        description="User age in years",
        examples=[25],
    )

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name must not be blank")
        return value


@app.post("/users/process")
def process_user(request: UserRequest):
    logger = get_logger("src.user_app.api")

    service = UserService(
        raw_data=request.model_dump_json(),
        logger=logger,
    )

    try:
        result = service.process()
        return {"result": result}

    except Exception as exc:
        raise map_domain_error(exc)
