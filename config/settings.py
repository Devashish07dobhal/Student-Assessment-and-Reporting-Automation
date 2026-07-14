"""
Project Settings

Contains all configurable values used
throughout the project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ==========================
# PROJECT INFORMATION
# ==========================

PROJECT_NAME = "AI Student Assessment System"

VERSION = "1.0.0"

AUTHOR = "Devashish Dobhal"

# ==========================
# ROOT DIRECTORY
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# DATA DIRECTORIES
# ==========================

DATA_DIR = BASE_DIR / "data"

QUIZ_DIR = DATA_DIR / "quizzes"

STUDENT_DIR = DATA_DIR / "students"

# ==========================
# OUTPUT DIRECTORIES
# ==========================

REPORT_DIR = BASE_DIR / "reports"

GRADECARD_DIR = REPORT_DIR / "gradecards"

CHART_DIR = BASE_DIR / "charts"

LOG_DIR = BASE_DIR / "logs"

# ==========================
# REPORT FILES
# ==========================

FINAL_REPORT = REPORT_DIR / "Final_Student_Report.xlsx"

STATISTICS_REPORT = REPORT_DIR / "statistics.xlsx"

# ==========================
# EMAIL SETTINGS
# ==========================

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS") or os.getenv("SENDER_EMAIL")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") or os.getenv("APP_PASSWORD")

SMTP_SERVER = os.getenv("SMTP_SERVER") or "smtp.gmail.com"

SMTP_PORT = int(os.getenv("SMTP_PORT", 465))

# ==========================
# PDF SETTINGS
# ==========================

COLLEGE_NAME = "Lloyd Institute of Engineering & Technology"

REPORT_TITLE = "Student Grade Card"

PDF_AUTHOR = AUTHOR

# ==========================
# CREATE OUTPUT FOLDERS
# ==========================

GRADECARD_DIR.mkdir(parents=True, exist_ok=True)

REPORT_DIR.mkdir(parents=True, exist_ok=True)

CHART_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR.mkdir(parents=True, exist_ok=True)

# ==========================
# OTHER DIRECTORIES
# ==========================

ASSETS_DIR = BASE_DIR / "assets"

TEMPLATE_DIR = BASE_DIR / "templates"

DOCS_DIR = BASE_DIR / "docs"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)

DOCS_DIR.mkdir(parents=True, exist_ok=True)

COLLEGE_LOCATION = "Greater Noida, Uttar Pradesh"

DEPARTMENT = "Artificial Intelligence & Machine Learning"

ACADEMIC_SESSION = "2026-27"
TOP_STUDENTS_REPORT = REPORT_DIR / "Top_Students.xlsx"

EMAIL_LOG = LOG_DIR / "email_log.csv"

APPLICATION_LOG = LOG_DIR / "application.log"