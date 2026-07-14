"""
merger.py

Merges all quiz DataFrames into one master DataFrame.
"""

import pandas as pd

from src.logger import log_info


class DataMerger:

    def __init__(self, quizzes: dict):

        self.quizzes = quizzes

    # ---------------------------------------------------------

    def merge(self):

        merged_df = None

        for index, (quiz_name, quiz_df) in enumerate(self.quizzes.items(), start=1):

            df = quiz_df.copy()

            # Rename Total score -> Quiz1, Quiz2, ...
            # Create column name from CSV filename
            column_name = (
                quiz_name
                    .replace("_", " ")
                    .replace("-", " ")
                    .title()
            )

            df = df.rename(
                columns={
                    "Total score": column_name
                }
            )

            # Keep only required columns
            df = df[
                 [
                    "Name",
                    "Email",
                    column_name
                    ]
                ]

            if merged_df is None:

                merged_df = df

            else:

                merged_df = pd.merge(

                    merged_df,

                    df,

                    on=["Name", "Email"],

                    how="outer"

                )

        # Replace missing marks with 0
        quiz_columns = [
            col
            for col in merged_df.columns
            if col not in ["Name", "Email"]

        ]

        merged_df[quiz_columns] = merged_df[quiz_columns].fillna(0)
        log_info("All quizzes merged successfully.")

        return merged_df