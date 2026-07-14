"""
logger.py

Logging utility for the
AI Student Assessment System.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from config.settings import LOG_DIR

# ==========================================================
# Create Log Folder
# ==========================================================

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "application.log"

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger("AIStudentAssessment")

logger.setLevel(logging.INFO)
logger.propagate = False

# Prevent duplicate handlers if imported multiple times
if not logger.handlers:

    # ---------- File Handler ----------

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2 * 1024 * 1024,   # 2 MB
        backupCount=5,
        encoding="utf-8"
    )

    # ---------- Console Handler ----------

    console_handler = logging.StreamHandler()

    # ---------- Formatter ----------

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# ==========================================================
# Helper Functions
# ==========================================================

def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_exception(message):
    logger.exception(message)