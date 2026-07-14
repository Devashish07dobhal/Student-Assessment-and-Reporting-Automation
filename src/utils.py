"""
utils.py

Reusable helper functions for the
AI Student Assessment System.
"""

import re
from pathlib import Path
from datetime import datetime


# ==========================================================
# Extract Marks
# ==========================================================

def extract_marks(value):
    """
    Converts marks like:

    '12 / 15'
    '15.00 / 20'
    18

    into numeric values.
    """

    try:

        if isinstance(value, str):

            value = value.strip()

            if "/" in value:
                return float(value.split("/")[0])

            return float(value)

        return float(value)

    except (ValueError, TypeError):

        return 0.0


# ==========================================================
# Calculate Percentage
# ==========================================================

def calculate_percentage(obtained, maximum):

    if maximum == 0:
        return 0

    return round((obtained / maximum) * 100, 2)


# ==========================================================
# Sanitize Filename
# ==========================================================

def sanitize_filename(name):

    """
    Removes illegal filename characters.

    Example:

    Rahul Kumar

    becomes

    Rahul_Kumar
    """

    name = str(name).strip()

    name = re.sub(r"[^\w\s-]", "", name)

    name = "_".join(name.split())

    return name


# ==========================================================
# Validate Email
# ==========================================================

def validate_email(email):

    """
    Returns True if email is valid.
    """

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.match(pattern, str(email).strip()))


# ==========================================================
# Find Maximum Marks
# ==========================================================

def find_max_marks(score_column):

    """
    Example values

    12 / 15

    15 / 20

    Returns

    35
    """

    total = 0

    for score in score_column:

        if isinstance(score, str) and "/" in score:

            try:

                maximum = float(score.split("/")[1])

                total += maximum

            except Exception:

                pass

    return total


# ==========================================================
# Current Timestamp
# ==========================================================

def get_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================================================
# Create Directory
# ==========================================================

def create_directory(path):

    Path(path).mkdir(parents=True, exist_ok=True)


# ==========================================================
# Print Section Header
# ==========================================================

def print_header(title):

    print("\n" + "=" * 60)

    print(title.upper())

    print("=" * 60)