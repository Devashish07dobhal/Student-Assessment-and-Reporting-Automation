"""
pdf_generator.py

Generates professional PDF grade cards
for every student.
"""
import qrcode
import tempfile
from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from config.settings import REPORT_DIR
from src.logger import log_info
from src.utils import sanitize_filename


class PDFGenerator:

    def __init__(self, dataframe):

        self.df = dataframe

        self.output_dir = REPORT_DIR / "gradecards"

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.styles = getSampleStyleSheet()

    # --------------------------------------------------
    # Custom Styles
    # ----------------------------------------------------

        self.title_style = ParagraphStyle(
            "TitleStyle",
            parent=self.styles["Title"],
            alignment=TA_CENTER,
            fontSize=22,
            textColor=colors.darkblue,
            spaceAfter=10
        )

        self.heading_style = ParagraphStyle(
            "HeadingStyle",
            parent=self.styles["Heading2"],
            alignment=TA_CENTER,
            fontSize=14,
            textColor=colors.darkblue
        )

        self.normal_style = ParagraphStyle(
            "NormalStyle",
            parent=self.styles["BodyText"],
            fontSize=11,
            leading=18
        )

        self.footer_style = ParagraphStyle(
            "Footer",
            parent=self.styles["BodyText"],
            alignment=TA_CENTER,
            textColor=colors.grey,
            fontSize=9
        )
        self.center_style = ParagraphStyle(
            "CenterStyle",
            parent=self.styles["BodyText"],
            alignment=TA_CENTER,
            fontSize=11
        )
    def get_grade_color(self, grade):

        colors_map = {
            "A+": colors.green,
            "A": colors.darkgreen,
            "B+": colors.blue,
            "B": colors.darkblue,
            "C": colors.orange,
            "D": colors.red,
            "F": colors.red
        }

        return colors_map.get(grade, colors.black)
    def get_remark(self, grade):

        remarks = {
            "A+": "Outstanding Performance",
            "A": "Excellent Performance",
            "B+": "Very Good",
            "B": "Good",
            "C": "Satisfactory",
            "D": "Needs Improvement",
            "F": "Failed"
        }
        return remarks.get(grade, "No Remarks")
    def generate_qr(self, row):

        qr_data = f"""Name : {row['Name']}
        Email : {row['Email']}
        Total Marks : {row['Total_Marks']}
        Percentage : {row['Percentage']}
        Grade : {row['Grade']}
        Rank : {row['Rank']}
        """

        qr = qrcode.make(qr_data)

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        qr.save(temp_file.name)

        return temp_file.name
        
    def build_header(self, elements):

        logo_path = Path("assets/liet_logo.jpeg")

        if logo_path.exists():

            logo = Image(
                str(logo_path),
                width=1 * inch,
                height=1 * inch
            )

            logo.hAlign = "CENTER"

            elements.append(logo)

        elements.append(
            Paragraph(
                "<b>LLOYD INSTITUTE OF ENGINEERING & TECHNOLOGY</b>",
                self.title_style
            )
        )

        elements.append(
            Paragraph(
                "Affiliated to Dr. A.P.J Abdul Kalam Technical University",
                self.heading_style
            )
        )

        elements.append(
            Paragraph(
                "Greater Noida, Uttar Pradesh",
                self.center_style
            )
        )

        elements.append(
            Paragraph(
                "Department of Artificial Intelligence & Machine Learning",
                self.heading_style
            )
        )

        elements.append(Spacer(1,10))

        heading = Table(
            [["STUDENT GRADE CARD"]],
            colWidths=[450]
        )

        heading.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#003366")),
            ("TEXTCOLOR",(0,0),(-1,-1),colors.white),
            ("ALIGN",(0,0),(-1,-1),"CENTER"),
            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
            ("FONTSIZE",(0,0),(-1,-1),16),
            ("BOTTOMPADDING",(0,0),(-1,-1),10),
            ("TOPPADDING",(0,0),(-1,-1),10)

        ]))

        elements.append(heading)

        elements.append(Spacer(1,20))

    # --------------------------------------------------

    def create_gradecard(self, row):

        filename = self.output_dir / (
            sanitize_filename(row["Name"]) + ".pdf"
        )

        doc = SimpleDocTemplate(str(filename))

        elements = []

        # Header
        self.build_header(elements)

        # Student Information

        student_table = Table([

    ["Student Name", row["Name"]],

    ["Department", "Artificial Intelligence & Machine Learning"],

    ["Generated On", datetime.now().strftime("%d-%m-%Y")]

], colWidths=[180,280])

        student_table.setStyle(TableStyle([

    ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#D9EAF7")),

    ("BACKGROUND",(1,0),(1,-1),colors.whitesmoke),

    ("TEXTCOLOR",(0,0),(0,-1),colors.darkblue),

    ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

    ("GRID",(0,0),(-1,-1),1,colors.grey),

    ("BOTTOMPADDING",(0,0),(-1,-1),8),

]))

        elements.append(student_table)

        elements.append(Spacer(1, 20))

        # Quiz Table

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

        table_data = [["Quiz", "Marks"]]

        for quiz in quiz_columns:

            table_data.append([quiz, row[quiz]])

        table_data.extend([

            ["Total Marks", row["Total_Marks"]],

            ["Percentage", f"{row['Percentage']} %"],

            ["Grade", row["Grade"]],

            ["Rank", row["Rank"]]

        ])

        table = Table(table_data)

        table.setStyle(TableStyle([

    ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#003366")),

    ("TEXTCOLOR",(0,0),(-1,0),colors.white),

    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

    ("GRID",(0,0),(-1,-1),1,colors.black),

    ("ALIGN",(0,0),(-1,-1),"CENTER"),

    ("BOTTOMPADDING",(0,0),(-1,0),10),

    ("BACKGROUND",(0,1),(-1,-1),colors.beige)

]))

        elements.append(table)

        elements.append(Spacer(1, 20))
        grade_box = Table(
            [[f"GRADE : {row['Grade']}"]],
            colWidths=[170]
        )

        grade_box.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),self.get_grade_color(row["Grade"])),

            ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("FONTSIZE",(0,0),(-1,-1),16),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10)

        ]))

        elements.append(grade_box)

        elements.append(Spacer(1,15))
        # Performance

        remark = self.get_remark(row["Grade"])
    
        elements.append(

            Paragraph(
    f"<b>Performance :</b> {remark}",

                self.styles["Heading2"]

            )

        )

        elements.append(Spacer(1, 20))
        percentage = float(row["Percentage"])

        filled = min(25, int(percentage / 4))

        bar = "█" * filled + "░" * (25-filled)

        elements.append(

            Paragraph(

                f"<b>Overall Performance</b><br/><font color='green'>{bar}</font><br/>{percentage:.2f}%",

                self.normal_style

            )

        )

        elements.append(Spacer(1,20))
       

        

        # Footer
        elements.append(
            Paragraph(
                "______________________________",
                self.normal_style
        )
    )

        elements.append(
            Paragraph(
                "<b>Faculty Coordinator</b>",
                self.normal_style
        )
    )

        elements.append(
            Paragraph(
                    "Department of Artificial Intelligence & Machine Learning",
                    self.normal_style
        )
    )

        elements.append(Spacer(1,15))

        elements.append(
            Paragraph(

        f"Generated on : {datetime.now().strftime('%d %B %Y')}",

        self.styles["Italic"]

    )
        )

        elements.append(
            Paragraph(
                "This is a computer-generated grade card. No signature is required.",
                self.footer_style
            )
        )
# -----------------------------------
#           QR Code
# -----------------------------------

        qr_path = self.generate_qr(row)

        qr_image = Image(
            qr_path,
            width=1.2 * inch,
            height=1.2 * inch
        )

        qr_image.hAlign = "CENTER"

        elements.append(Spacer(1, 15))
        elements.append(qr_image)
        elements.append(

    Paragraph(

        "Scan for Student Details",

        self.footer_style

    )

)    
        doc.build(elements)

        log_info(f"PDF generated for {row['Name']}")

    # --------------------------------------------------

    def generate(self):

        log_info("Generating Grade Cards...")

        for _, row in self.df.iterrows():

            self.create_gradecard(row)

        log_info("All Grade Cards Generated Successfully.")