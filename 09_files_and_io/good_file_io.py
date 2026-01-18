from pathlib import Path


def read_config(path: Path) -> str:
    """
    Read configuration file content safely.

    Args:
        path: Path to the config file.

    Returns:
        File content as string.

    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If path is not a file.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    return path.read_text(encoding="utf-8")
