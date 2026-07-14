"""
validator.py

Validates quiz data before processing.
"""

import pandas as pd

from src.utils import validate_email
from src.logger import (
    log_info,
    log_warning,
    log_error
)


class DataValidator:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # -----------------------------------------------------

    def check_missing_names(self):

        missing = self.df["Name"].isnull().sum()

        if missing > 0:

            log_warning(f"{missing} missing student names found.")

        return missing

    # -----------------------------------------------------

    def check_missing_emails(self):

        missing = self.df["Email"].isnull().sum()

        if missing > 0:

            log_warning(f"{missing} missing emails found.")

        return missing

    # -----------------------------------------------------

    def check_missing_scores(self, score_column):

        missing = self.df[score_column].isnull().sum()

        if missing > 0:

            log_warning(f"{missing} missing scores in {score_column}")

        return missing

    # -----------------------------------------------------

    def check_duplicate_students(self):

        duplicates = self.df.duplicated(
            subset=["Name"],
            keep=False
        )

        count = duplicates.sum()

        if count > 0:

            log_warning(f"{count} duplicate student names found.")

        return count

    # -----------------------------------------------------

    def check_duplicate_emails(self):

        duplicates = self.df.duplicated(
        subset=["Name","Email"],
        keep=False
    )

        count = duplicates.sum()

        if count > 0:

            log_warning(f"{count} duplicate emails found.")

        return count

    # -----------------------------------------------------

    def check_invalid_emails(self):

        invalid = self.df[

        self.df["Email"].notna()

        &

        ~self.df["Email"].apply(validate_email)

    ]

        count = len(invalid)

        if count > 0:

            log_warning(f"{count} invalid email addresses.")

        return count

    # -----------------------------------------------------

    def validate(self, score_column=None):
        if score_column is None:

            if "Total score" in self.df.columns:

                score_column = "Total score"

            else:

                score_column = self.df.columns[-1]

        log_info("Starting data validation...")

        results = {

            "missing_names":
                self.check_missing_names(),

            "missing_emails":
                self.check_missing_emails(),

            "missing_scores":
                self.check_missing_scores(score_column),

            "duplicate_students":
                self.check_duplicate_students(),

            "duplicate_emails":
                self.check_duplicate_emails(),

            "invalid_emails":
                self.check_invalid_emails()

        }

        log_info("Validation completed.")

        return results