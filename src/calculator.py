"""
calculator.py

Calculates total marks,
percentage,
grades,
and rank.
"""

from config.grading import (
    TOTAL_MAX_MARKS,
    GRADE_BOUNDARIES
)

from src.logger import log_info


class GradeCalculator:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # -----------------------------------------------------

    def calculate_total_marks(self):

        quiz_columns = [

        col

        for col in self.df.columns

        if col not in [
            "Name",
            "Email",
            "Total_Marks",
            "Percentage",
            "Grade",
            "Rank"
        ]

    ]

        self.df["Total_Marks"] = self.df[quiz_columns].sum(axis=1)

        log_info("Total marks calculated.")

    # -----------------------------------------------------

    def calculate_percentage(self):

        self.df["Percentage"] = round(
            
    (self.df["Total_Marks"] / TOTAL_MAX_MARKS) * 100,
    2
    )

        log_info("Percentage calculated.")

    # -----------------------------------------------------

    def assign_grades(self):

        grades = []

        for percentage in self.df["Percentage"]:

            if percentage >= GRADE_BOUNDARIES["A+"]:
                grades.append("A+")

            elif percentage >= GRADE_BOUNDARIES["A"]:
                grades.append("A")

            elif percentage >= GRADE_BOUNDARIES["B"]:
                grades.append("B")

            elif percentage >= GRADE_BOUNDARIES["C"]:
                grades.append("C")

            elif percentage >= GRADE_BOUNDARIES["D"]:
                grades.append("D")

            else:
                grades.append("F")

        self.df["Grade"] = grades

        log_info("Grades assigned.")

    # -----------------------------------------------------

    def calculate_rank(self):

        self.df["Rank"] = (

            self.df["Total_Marks"]

            .rank(

                ascending=False,

                method="dense"

            )

            .astype(int)

        )

        log_info("Ranks calculated.")

    # -----------------------------------------------------

    def calculate(self):

        log_info("Starting calculations...")

        self.calculate_total_marks()

        self.calculate_percentage()

        self.assign_grades()

        self.calculate_rank()

        log_info("Calculations completed.")

        return self.df