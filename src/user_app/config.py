import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    env: str
    log_level: str


def load_config() -> AppConfig:
    """
    Load and validate application configuration.

    Environment rules:
    - dev      → DEBUG
    - staging  → INFO
    - prod     → INFO
    """
    load_dotenv()

    env = os.getenv("APP_ENV", "dev").lower()

    allowed_envs = {"dev", "staging", "prod"}
    if env not in allowed_envs:
        raise ValueError(f"Invalid APP_ENV value: {env}")

    log_level = "DEBUG" if env == "dev" else "INFO"

    return AppConfig(env=env, log_level=log_level)
