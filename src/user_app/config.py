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
    enable_verbose_output: bool


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
    Configuration precedence (LOW → HIGH):

    1. Code defaults
    2. YAML config
    3. Environment variables
    """
    # Load .env for local development
    load_dotenv()

    # -------------------------
    # Environment
    # -------------------------
    env = os.getenv("APP_ENV", "dev").lower()
    if env not in {"dev", "staging", "prod"}:
        raise ValueError(f"Invalid APP_ENV value: {env}")

    # -------------------------
    # YAML config
    # -------------------------
    raw_config = _load_yaml_config()

    yaml_log_level = raw_config.get("logging", {}).get("level")
    yaml_timeout = raw_config.get("app", {}).get("timeout_seconds", 30)

    features = raw_config.get("features", {})
    yaml_enable_metrics = features.get("enable_metrics", False)
    yaml_enable_verbose = features.get("enable_verbose_output", False)

    # -------------------------
    # Log level precedence
    # -------------------------
    log_level = os.getenv("LOG_LEVEL") or yaml_log_level
    if not log_level:
        log_level = "DEBUG" if env == "dev" else "INFO"

    return AppConfig(
        env=env,
        log_level=str(log_level).upper(),
        timeout_seconds=int(yaml_timeout),
        enable_metrics=bool(yaml_enable_metrics),
        enable_verbose_output=bool(yaml_enable_verbose),
    )
