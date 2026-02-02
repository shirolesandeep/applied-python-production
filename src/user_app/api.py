from fastapi import FastAPI
from pydantic import BaseModel

from src.user_app.services.user_service import UserService
from src.user_app.dependencies import get_logger
from src.user_app.api_errors import map_domain_error


app = FastAPI(title="User Processing API")


class UserRequest(BaseModel):
    name: str
    age: int


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
        # Centralized, clean domain → HTTP error mapping
        raise map_domain_error(exc)
