"""
report_generator.py

Generates Excel reports.
"""

from pathlib import Path
import pandas as pd

from config.settings import REPORT_DIR
from src.logger import log_info


class ReportGenerator:

    def __init__(self, final_df, analytics):

        self.final_df = final_df
        self.analytics = analytics

        REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    # =====================================================

    def save_final_report(self):

        path = REPORT_DIR / "Final_Student_Report.xlsx"

        self.final_df.to_excel(
            path,
            index=False
        )

        log_info("Final Student Report generated.")

    # =====================================================

    def save_statistics(self):

        summary = self.analytics.summary()

        stats = pd.DataFrame(

            summary.items(),

            columns=["Metric", "Value"]

        )

        path = REPORT_DIR / "statistics.xlsx"

        stats.to_excel(

            path,

            index=False

        )

        log_info("Statistics report generated.")

    # =====================================================

    def save_top_students(self):

        top_students = self.analytics.top_students()

        path = REPORT_DIR / "Top_Students.xlsx"

        top_students.to_excel(

            path,

            index=False

        )

        log_info("Top students report generated.")

    # =====================================================

    def generate_reports(self):

        log_info("Generating Excel reports...")

        self.save_final_report()

        self.save_statistics()

        self.save_top_students()

        log_info("All reports generated successfully.")