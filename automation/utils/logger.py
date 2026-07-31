from __future__ import annotations

import logging
from pathlib import Path


def get_logger(
    name: str,
    log_directory: str | Path = "automation/logs",
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Create or return a configured Project Orion logger.

    Logs are written to both the terminal and automation/logs/validation.log.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    log_directory = Path(log_directory)
    log_directory.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        log_directory / "validation.log",
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
