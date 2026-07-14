"""
pipeline.py

Workflow manager for AI Student Assessment System
"""

from src.loader import load_all_quizzes
from src.validator import DataValidator
from src.cleaner import DataCleaner
from src.merger import DataMerger
from src.calculator import GradeCalculator
from src.analytics import StudentAnalytics
from src.report_generator import ReportGenerator
from src.pdf_generator import PDFGenerator
from src.chart_generator import ChartGenerator
from src.email_sender import EmailSender


from src.logger import log_info


# ==========================================================
# Common Pipeline
# ==========================================================

def prepare_data():

    log_info("Preparing assessment data...")

    quizzes = load_all_quizzes()

    cleaned_quizzes = {}

    for quiz_name, quiz_df in quizzes.items():

        log_info(f"Processing assessment: {quiz_name}")

        validator = DataValidator(quiz_df)

        validation_result = validator.validate()

        print(f"\nValidation Report ({quiz_name})")
        print(validation_result)

        log_info(str(validation_result))

        cleaner = DataCleaner(quiz_df)

        cleaned_quizzes[quiz_name] = cleaner.clean()

    log_info(f"{len(cleaned_quizzes)} assessment files processed successfully.")

    merger = DataMerger(cleaned_quizzes)

    merged_df = merger.merge()

    calculator = GradeCalculator(merged_df)

    final_df = calculator.calculate()

    analytics = StudentAnalytics(final_df)

    log_info("Data preparation completed successfully.")

    return final_df, analytics


# ==========================================================
# Complete Assessment
# ==========================================================

def run_complete_pipeline():
    
    log_info("Starting Complete Assessment Pipeline...")

    final_df, analytics = prepare_data()

    ReportGenerator(final_df, analytics).generate_reports()

    ChartGenerator(final_df).generate()

    PDFGenerator(final_df).generate()

    choice = input("\nSend Emails? (y/n): ").strip().lower()

    if choice == "y":

        EmailSender(final_df).send_all()

    elif choice == "n":

        log_info("Email sending skipped by user.")

    else:

        print("Invalid choice. Email sending skipped.")

        log_info("Invalid email option selected.")

    print("\n✓ Complete Assessment Finished")

    log_info("Complete Assessment Pipeline Finished.")


# ==========================================================
# Excel Reports
# ==========================================================

def generate_reports():

    log_info("Generating Excel Reports...")

    final_df, analytics = prepare_data()

    ReportGenerator(final_df, analytics).generate_reports()

    print("\n✓ Reports Generated")

    log_info("Excel Reports Generated Successfully.")


# ==========================================================
# PDF Grade Cards
# ==========================================================

def generate_pdfs():

    log_info("Generating PDF Grade Cards...")

    final_df, _ = prepare_data()

    PDFGenerator(final_df).generate()

    print("\n✓ PDF Grade Cards Generated")

    log_info("PDF Grade Cards Generated Successfully.")


# ==========================================================
# Charts
# ==========================================================

def generate_charts():

    log_info("Generating Charts...")

    final_df, _ = prepare_data()

    ChartGenerator(final_df).generate()

    print("\n✓ Charts Generated")

    log_info("Charts Generated Successfully.")


# ==========================================================
# Send Emails
# ==========================================================

def send_emails():

    log_info("Sending Student Emails...")

    final_df, _ = prepare_data()

    EmailSender(final_df).send_all()

    print("\n✓ Emails Sent")

    log_info("All Emails Sent Successfully.")


# ==========================================================
# Analytics
# ==========================================================

def show_analytics():

    log_info("Generating Analytics Summary...")

    final_df, analytics = prepare_data()

    summary = analytics.summary()

    print("\n" + "=" * 50)
    print("CLASS SUMMARY")
    print("=" * 50)

    for key, value in summary.items():

        print(f"{key:<25}: {value}")

    print("=" * 50)

    log_info("Analytics Summary Displayed Successfully.")
