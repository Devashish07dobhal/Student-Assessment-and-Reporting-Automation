"""
cleaner.py

Cleans quiz data before merging and calculations.
"""

import pandas as pd

from src.utils import extract_marks
from src.logger import log_info


class DataCleaner:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # ---------------------------------------------------------
    # Clean Student Names
    # ---------------------------------------------------------

    def clean_names(self):

        self.df["Name"] = (
            self.df["Name"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        log_info("Student names cleaned.")

    # ---------------------------------------------------------
    # Clean Emails
    # ---------------------------------------------------------

    def clean_emails(self):

        self.df["Email"] = (
            self.df["Email"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        log_info("Emails cleaned.")

    # ---------------------------------------------------------
    # Clean Marks
    # ---------------------------------------------------------

    def clean_marks(self, score_column="Total score"):

        self.df[score_column] = self.df[score_column].apply(extract_marks)

        log_info(f"{score_column} cleaned.")

    # ---------------------------------------------------------
    # Remove Duplicate Students
    # ---------------------------------------------------------

    def remove_duplicates(self):

        before = len(self.df)

        self.df = self.df.drop_duplicates(
            subset=["Name", "Email"]
        )

        after = len(self.df)

        removed = before - after

        log_info(f"{removed} duplicate rows removed.")

    # ---------------------------------------------------------
    # Fill Missing Values
    # ---------------------------------------------------------

    def fill_missing(self):

        self.df["Name"] = self.df["Name"].fillna("Unknown")
        self.df["Email"] = self.df["Email"].fillna("Not Available")

        log_info("Missing values handled.")

    # ---------------------------------------------------------
    # Clean Everything
    # ---------------------------------------------------------

    def clean(self):

        log_info("Starting data cleaning...")

        self.clean_names()

        self.clean_emails()

        self.fill_missing()

        self.clean_marks()

        self.remove_duplicates()

        log_info("Data cleaning completed.")

        return self.df