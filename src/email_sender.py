"""
email_sender.py

Sends grade cards to students.
"""

import os
import smtplib
import pandas as pd
from pathlib import Path

from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

from config.settings import (
    REPORT_DIR,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT,
)
from src.logger import log_info, log_error
from src.utils import sanitize_filename

load_dotenv()


class EmailSender:

    def __init__(self, dataframe):

        self.df = dataframe

        self.sender = (
            os.getenv("SENDER_EMAIL")
            or os.getenv("EMAIL_ADDRESS")
            or EMAIL_ADDRESS
        )
        self.password = (
            os.getenv("APP_PASSWORD")
            or os.getenv("EMAIL_PASSWORD")
            or EMAIL_PASSWORD
        )
        self.smtp_server = (
            os.getenv("SMTP_SERVER")
            or SMTP_SERVER
            or "smtp.gmail.com"
        )
        self.smtp_port = int(os.getenv("SMTP_PORT", SMTP_PORT or 465))

        self.gradecard_dir = REPORT_DIR / "gradecards"

        self.log = []

    # -----------------------------------------------------

    def send_email(self, row):

        receiver = row["Email"]

        pdf_file = self.gradecard_dir / (
            sanitize_filename(row["Name"]) + ".pdf"
        )

        if not self.sender or not self.password:

            error_msg = (
                "Email credentials are not configured. "
                "Set SENDER_EMAIL/APP_PASSWORD or EMAIL_ADDRESS/EMAIL_PASSWORD in your environment or .env file."
            )

            log_error(error_msg)

            self.log.append({
                "Name": row["Name"],
                "Email": receiver,
                "Status": error_msg
            })

            return

        if not pdf_file.exists():

            log_error(f"PDF not found for {row['Name']}")

            self.log.append({
                "Name": row["Name"],
                "Email": receiver,
                "Status": "PDF Missing"
            })

            return

        msg = EmailMessage()

        msg["Subject"] = "Student Grade Card"

        msg["From"] = self.sender

        msg["To"] = receiver

        # -----------------------------------------
        # Load HTML Email Template
        # -----------------------------------------

        template_path = Path("templates/email_template.html")

        html = template_path.read_text(encoding="utf-8")

        html = html.replace("{{NAME}}", str(row["Name"]))

        html = html.replace("{{TOTAL}}", str(row["Total_Marks"]))

        html = html.replace("{{PERCENTAGE}}", str(row["Percentage"]))

        html = html.replace("{{GRADE}}", str(row["Grade"]))

        html = html.replace("{{RANK}}", str(row["Rank"]))
        
        # -----------------------------------------
        # Replace Assessment Marks
        # -----------------------------------------

        assessment_html = ""

        assessment_columns = [

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

        for column in assessment_columns:

            assessment_html += f"""
            <tr>
                <td>{column}</td>
                <td>{row[column]}</td>
            </tr>
            """

        html = html.replace(
            "{{ASSESSMENT_ROWS}}",
            assessment_html
        )

       # Plain text fallback
        msg.set_content(
            f"""
        Dear {row['Name']},

        Please find your grade card attached.

        Regards,
        AI Student Assessment System
        """
        )

        # HTML version
        msg.add_alternative(
            html,
            subtype="html"
        )

        with open(pdf_file, "rb") as file:

                    msg.add_attachment(
                        file.read(),
                        maintype="application",
                        subtype="pdf",
                        filename=pdf_file.name
                    )
        try:

                    with smtplib.SMTP_SSL(
                        self.smtp_server,
                        self.smtp_port
                    ) as server:

                        server.login(
                            self.sender,
                            self.password
                        )

                        server.send_message(msg)

                    log_info(f"Email sent to {receiver}")

                    self.log.append({
                        "Name": row["Name"],
                        "Email": receiver,
                        "Status": "Success"
                    })

        except Exception as e:

                    print("\n" + "=" * 60)
                    print("FAILED")
                    print("Student :", row["Name"])
                    print("Email   :", receiver)
                    print("Error   :", repr(e))
                    print("=" * 60)

                    log_error(f"Failed: {receiver} | {repr(e)}")

                    self.log.append({
                        "Name": row["Name"],
                        "Email": receiver,
                        "Status": repr(e)
                    })

    # -----------------------------------------------------

    def send_all(self):

        log_info("Sending emails...")

        for _, row in self.df.iterrows():

            self.send_email(row)

        pd.DataFrame(self.log).to_csv(

            "logs/email_log.csv",

            index=False

        )

        log_info("Email sending completed.")