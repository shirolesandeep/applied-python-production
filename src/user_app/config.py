import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    env: str
    log_level: str
    timeout_seconds: int
    enable_metrics: bool


def _load_yaml_config() -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    YAML provides structured, non-secret defaults.
    """
    config_path = Path("config/app_config.yaml")

    if not config_path.exists():
        raise FileNotFoundError("Missing config/app_config.yaml")

    with config_path.open() as f:
        return yaml.safe_load(f) or {}


def load_config() -> AppConfig:
    """
    Load configuration with EXPLICIT precedence:

    1. Code defaults (lowest priority)
    2. YAML config file
    3. Environment variables (highest priority)

    This function FAILS FAST on invalid configuration.
    """
    # Load .env for local development (does NOT override OS env)
    load_dotenv()

    # -------------------------
    # Environment (dev/staging/prod)
    # -------------------------
    env = os.getenv("APP_ENV", "dev").lower()

    allowed_envs = {"dev", "staging", "prod"}
    if env not in allowed_envs:
        raise ValueError(f"Invalid APP_ENV value: {env}")

    # -------------------------
    # Load YAML defaults
    # -------------------------
    raw_config = _load_yaml_config()

    # ---- YAML values ----
    yaml_log_level = raw_config.get("logging", {}).get("level")
    yaml_timeout = raw_config.get("app", {}).get("timeout_seconds", 30)
    yaml_metrics = raw_config.get("features", {}).get("enable_metrics", False)

    # -------------------------
    # Log level precedence (IMPORTANT)
    # -------------------------
    # 1. ENV override
    # 2. YAML value
    # 3. Environment-based default
    log_level = os.getenv("LOG_LEVEL")

    if not log_level:
        log_level = yaml_log_level

    if not log_level:
        log_level = "DEBUG" if env == "dev" else "INFO"

    # -------------------------
    # Final validated config
    # -------------------------
    return AppConfig(
        env=env,
        log_level=str(log_level).upper(),
        timeout_seconds=int(yaml_timeout),
        enable_metrics=bool(yaml_metrics),
    )
