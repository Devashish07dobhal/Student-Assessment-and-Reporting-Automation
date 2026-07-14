"""
chart_generator.py

Generates visual analytics charts for the
AI Student Assessment System.
"""

from pathlib import Path
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self, dataframe):

        self.df = dataframe

        self.output_dir = Path("charts")
        self.output_dir.mkdir(exist_ok=True)

    # ---------------------------------------------
    # Save helper
    # ---------------------------------------------

    def save_chart(self):

        plt.tight_layout()

        plt.savefig(
            self.output_dir / self.filename,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # ---------------------------------------------
    # Grade Distribution
    # ---------------------------------------------

    def grade_distribution(self):

        plt.figure(figsize=(8, 5))

        from config.grading import GRADE_ORDER

        grade_count = (

            self.df["Grade"]

            .value_counts()

            .reindex(GRADE_ORDER, fill_value=0)

        )

        plt.bar(

            grade_count.index,

            grade_count.values

        )

        plt.title("Grade Distribution")

        plt.xlabel("Grade")

        plt.ylabel("Number of Students")

        self.filename = "grade_distribution.png"

        self.save_chart()

    # ---------------------------------------------
    # Top 10 Students
    # ---------------------------------------------

    def top_students(self):

        top = self.df.sort_values(
            "Total_Marks",
            ascending=False
        ).head(10)

        plt.figure(figsize=(10,5))

        plt.bar(
            top["Name"],
            top["Total_Marks"]
        )

        plt.xticks(rotation=45)

        plt.title("Top 10 Students")

        plt.ylabel("Marks")

        self.filename = "top10_students.png"

        self.save_chart()

    # ---------------------------------------------
    # Percentage Distribution
    # ---------------------------------------------

    def percentage_distribution(self):

        plt.figure(figsize=(8,5))

        plt.hist(
            self.df["Percentage"],
            bins=10
        )

        plt.title("Percentage Distribution")

        plt.xlabel("Percentage")

        plt.ylabel("Students")

        self.filename = "percentage_distribution.png"

        self.save_chart()

    # ---------------------------------------------
    # Quiz-wise Average
    # ---------------------------------------------

# ---------------------------------------------
# Assessment-wise Average
# ---------------------------------------------

    def assessment_average(self):
        excluded_columns = {

            "Name",
            "Email",
            "Total_Marks",
            "Percentage",
            "Grade",
            "Rank"

        }

        assessment_columns = [

            col

            for col in self.df.columns

            if col not in excluded_columns

        ]

        averages = [

            self.df[col].mean()

            for col in assessment_columns

        ]

        plt.figure(figsize=(10,5))

        plt.bar(

            assessment_columns,

            averages

        )

        plt.xticks(rotation=30, ha="right")

        plt.title("Assessment-wise Average Marks")

        plt.xlabel("Assessments")

        plt.ylabel("Average Marks")

        self.filename = "assessment_average.png"

        self.save_chart()

    # ---------------------------------------------
    # Generate All
    # ---------------------------------------------

    def generate(self):

        print("\nGenerating Charts...")

        self.grade_distribution()

        self.top_students()

        self.percentage_distribution()

        self.assessment_average()

        print("Charts Generated Successfully.")