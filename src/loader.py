"""
loader.py

Loads quiz CSV files and the master student list.
"""

from pathlib import Path
import pandas as pd

from config.settings import QUIZ_DIR, STUDENT_DIR
from src.logger import log_info, log_error

# ==========================================================
# Required Quiz Columns
# ==========================================================

REQUIRED_QUIZ_COLUMNS = [
    "Name",
    "Email",
    "Total score"
]
# ==========================================================
# Required Columns
# ==========================================================



REQUIRED_MASTER_COLUMNS = [
    "Name",
    "Email"
]


# ==========================================================
# Load Single Quiz
# ==========================================================

def load_quiz(file_path: Path) -> pd.DataFrame:
    """
    Load one quiz CSV file.

    Parameters
    ----------
    file_path : Path

    Returns
    -------
    DataFrame
    """

    try:

        df = pd.read_csv(file_path)

        missing = [
            col for col in REQUIRED_QUIZ_COLUMNS
            if col not in df.columns
        ]

        if missing:
            raise ValueError(
                f"{file_path.name} missing columns: {missing}"
            )

        log_info(f"Loaded {file_path.name}")

        return df

    except Exception as e:

        log_error(f"Failed loading {file_path.name}")

        raise e


# ==========================================================
# Load All Quiz Files
# ==========================================================

def load_all_quizzes():
    """
    Automatically load every quiz CSV file
    inside data/quizzes/.

    Returns
    -------
    dict
        {
            "day1_module1": DataFrame,
            "day2_module2": DataFrame,
            ...
        }
    """

    quiz_files = sorted(

    QUIZ_DIR.glob("*.csv"),

    key=lambda x: x.stem.lower()

)

    if not quiz_files:
        raise FileNotFoundError("No quiz CSV files found.")

    quizzes = {}

    for file in quiz_files:

        quizzes[file.stem] = load_quiz(file)

    log_info(f"{len(quizzes)} quiz files loaded.")

    return quizzes

# ==========================================================
# Load Student Master List
# ==========================================================

def load_student_master():
    """
    Load Master Student List Excel file.
    """

    files = list(STUDENT_DIR.glob("*.xlsx"))

    if not files:

        raise FileNotFoundError(
            "Master Student List not found."
        )

    master = pd.read_excel(files[0])

    missing = [
        col for col in REQUIRED_MASTER_COLUMNS
        if col not in master.columns
    ]

    if missing:

        raise ValueError(
            f"Missing columns in Master Student List: {missing}"
        )

    log_info("Master Student List loaded.")

    return master


# ==========================================================
# Display Loaded Files
# ==========================================================

def show_loaded_files():

    print("\nQuiz Files Found:\n")

    for file in sorted(QUIZ_DIR.glob("*.csv")):

        print(file.name)

    print()

    for file in STUDENT_DIR.glob("*.xlsx"):

        print("Master List :", file.name)