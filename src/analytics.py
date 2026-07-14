"""
analytics.py

Generates analytics from the final
student assessment report.
"""

import pandas as pd
from config.grading import GRADE_ORDER
from src.logger import log_info


class StudentAnalytics:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # -----------------------------------------------------

    def total_students(self):

        return len(self.df)

    # -----------------------------------------------------

    def highest_marks(self):

        return self.df["Total_Marks"].max()

    # -----------------------------------------------------

    def lowest_marks(self):

        return self.df["Total_Marks"].min()

    # -----------------------------------------------------

    def average_marks(self):

        return round(self.df["Total_Marks"].mean(), 2)

    # -----------------------------------------------------

    def average_percentage(self):

        return round(self.df["Percentage"].mean(), 2)

    # -----------------------------------------------------

    def highest_scorer(self):

        return self.df.loc[
            self.df["Total_Marks"].idxmax(),
            ["Name", "Total_Marks"]
        ]

    # -----------------------------------------------------

    def lowest_scorer(self):

        return self.df.loc[
            self.df["Total_Marks"].idxmin(),
            ["Name", "Total_Marks"]
        ]

    # -----------------------------------------------------

    def grade_distribution(self):

       # Academic order instead of alphabetical order
                grade_distribution = (

                        self.df["Grade"]

                        .value_counts()

                        .reindex(GRADE_ORDER, fill_value=0)

                    )

    # -----------------------------------------------------

    def top_students(self, n=10):

        return self.df.sort_values(
            by="Total_Marks",
            ascending=False
        ).head(n)

    # -----------------------------------------------------

    def summary(self):

        log_info("Generating analytics...")

        report = {

            "Total Students": self.total_students(),

            "Highest Marks": self.highest_marks(),

            "Lowest Marks": self.lowest_marks(),

            "Average Marks": self.average_marks(),

            "Average Percentage": self.average_percentage()

        }

        return report