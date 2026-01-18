import os


class Settings:
    """Application configuration loaded from environment variables."""

    def __init__(self) -> None:
        self.env = os.getenv("APP_ENV", "dev")
        self.api_url = os.getenv("API_URL", "http://localhost:8000")
        self.timeout = int(os.getenv("TIMEOUT", "30"))


settings = Settings()
