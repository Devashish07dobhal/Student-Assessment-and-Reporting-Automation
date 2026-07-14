import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
from config.grading import GRADE_ORDER

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Student Assessment System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

report_path = Path("reports/Final_Student_Report.xlsx")

if not report_path.exists():
    st.error("❌ Final Student Report not found.")
    st.stop()

df = pd.read_excel(report_path)

# Hide email for dashboard
if "Email" in df.columns:
    dashboard_df = df.drop(columns=["Email"])
else:
    dashboard_df = df.copy()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.image("assets/liet_logo.jpeg", width=120)

st.sidebar.title("AI Student Assessment")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍🎓 Students",
        "📊 Analytics",
        "📈 Charts",
        "📄 Reports",
        "⚙ About"
    ]
)

# -------------------------------------------------------
# Dashboard
# -------------------------------------------------------

if page == "🏠 Dashboard":

    st.title("🎓 AI Student Assessment System")

    st.caption(
        "Lloyd Institute of Engineering & Technology | Artificial Intelligence & Machine Learning"
    )

    st.markdown("---")

    total_students = len(df)

    highest_marks = df["Total_Marks"].max()

    average_marks = round(df["Total_Marks"].mean(), 2)

    average_percentage = round(df["Percentage"].mean(), 2)

    highest_percentage = df["Percentage"].max()

    a_plus_students = (df["Grade"] == "A+").sum()

    rank1 = df.loc[df["Rank"] == 1, "Name"].iloc[0]

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Students",
        total_students
    )

    c2.metric(
        "Highest Marks",
        highest_marks
    )

    c3.metric(
        "Average Marks",
        average_marks
    )

    c4.metric(
        "Average %",
        f"{average_percentage}%"
    )

    c5.metric(
        "A+ Students",
        a_plus_students
    )

    st.markdown("---")

    left, right = st.columns([2.4,1])

    with left:

        st.subheader("📋 Student Assessment Report")

        st.dataframe(

            dashboard_df,

            use_container_width=True,

            hide_index=True,

            height=520

        )

    with right:

        st.subheader("🏆 Class Highlights")

        st.success(f"Rank 1 : {rank1}")

        st.info(f"Highest Percentage : {highest_percentage}%")

        st.info(f"Average Percentage : {average_percentage}%")

        st.metric(

            "Total Assessments",

            len([

                c for c in df.columns

                if c not in [

                    "Name",

                    "Email",

                    "Total_Marks",

                    "Percentage",

                    "Grade",

                    "Rank"

                ]

            ])

        )

        st.markdown("---")

        st.subheader("System Status")

        st.success("Assessment Completed")

        st.success("Reports Generated")

        st.success("Grade Cards Ready")

        st.success("Charts Available")

    st.markdown("---")

    st.caption(
        "AI Student Assessment System • Dashboard v1.0"
    )



# -------------------------------------------------------
# Students Page
# -------------------------------------------------------

elif page == "👨‍🎓 Students":

    st.title("👨‍🎓 Student Profile")

    st.markdown("---")

    # Search Student

    selected = st.selectbox(

        "Select Student",

        sorted(df["Name"].unique())

    )

    student = df[df["Name"] == selected].iloc[0]

    # ------------------------------
    # Profile Metrics
    # ------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Marks",
        student["Total_Marks"]
    )

    c2.metric(
        "Percentage",
        f"{student['Percentage']}%"
    )

    c3.metric(
        "Grade",
        student["Grade"]
    )

    c4.metric(
        "Rank",
        int(student["Rank"])
    )

    st.markdown("---")

    left, right = st.columns([2,1])

    # ==================================
    # Assessment Marks
    # ==================================

    with left:

        st.subheader("Assessment Marks")

        assessment_columns = [

            col

            for col in dashboard_df.columns

            if col not in [

                "Name",

                "Total_Marks",

                "Percentage",

                "Grade",

                "Rank"

            ]

        ]

        marks = pd.DataFrame({

            "Assessment": assessment_columns,

            "Marks": [

                student[col]

                for col in assessment_columns

            ]

        })

        st.dataframe(

            marks,

            use_container_width=True,

            hide_index=True

        )

        fig = px.bar(

            marks,

            x="Assessment",

            y="Marks",

            text="Marks",

            title="Assessment Performance"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ==================================
    # Performance Summary
    # ==================================

    with right:

        st.subheader("Performance")

        st.progress(

            float(student["Percentage"]) / 100

        )

        st.write(

            f"Overall Score: **{student['Percentage']}%**"

        )

        st.markdown("---")

        if student["Grade"] == "A+":

            st.success("Outstanding Performance")

        elif student["Grade"] == "A":

            st.success("Excellent Performance")

        elif student["Grade"] == "B":

            st.info("Very Good Performance")

        elif student["Grade"] == "C":

            st.warning("Good Performance")

        elif student["Grade"] == "D":

            st.warning("Needs Improvement")

        else:

            st.error("At Risk")

        st.markdown("---")

        st.write("### Student Information")

        st.write(f"**Name:** {student['Name']}")

        st.write(f"**Rank:** {student['Rank']}")

        st.write(f"**Grade:** {student['Grade']}")

        st.write(f"**Percentage:** {student['Percentage']}%")

        st.write(f"**Total Marks:** {student['Total_Marks']}")


# -------------------------------------------------------
# Analytics
# -------------------------------------------------------

elif page == "📊 Analytics":

    st.title("📊 Student Performance Analytics")

    st.markdown("---")

    # =====================================
    # Statistics Cards
    # =====================================

    total_students = len(df)

    average_marks = round(df["Total_Marks"].mean(),2)

    highest_marks = df["Total_Marks"].max()

    lowest_marks = df["Total_Marks"].min()

    average_percentage = round(df["Percentage"].mean(),2)

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Students", total_students)

    c2.metric("Highest", highest_marks)

    c3.metric("Lowest", lowest_marks)

    c4.metric("Average Marks", average_marks)

    c5.metric("Average %", f"{average_percentage}%")

    st.markdown("---")

    # =====================================
    # Charts
    # =====================================

    left,right = st.columns(2)

    with left:

        st.subheader("Grade Distribution")

        grade_count = (

            df["Grade"]

            .value_counts()

            .reindex(GRADE_ORDER, fill_value=0)

        )

        grade_df = pd.DataFrame({

            "Grade": grade_count.index,

            "Students": grade_count.values

        })

        fig = px.bar(

            grade_df,

            x="Grade",

            y="Students",

            color="Grade",

            text="Students",

            title="Grade Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        st.subheader("Percentage Distribution")

        fig = px.histogram(

            df,

            x="Percentage",

            nbins=10,

            color_discrete_sequence=["royalblue"],

            title="Percentage Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # =====================================
    # Box Plot
    # =====================================

    st.subheader("Marks Spread")

    fig = px.box(

        df,

        y="Total_Marks",

        points="all",

        title="Distribution of Student Marks"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # Top Students
    # =====================================

    st.subheader("🏆 Top 10 Students")

    top_students = (

        df

        .sort_values(

            "Total_Marks",

            ascending=False

        )

        .head(10)

        .drop(columns=["Email"])

    )

    st.dataframe(

        top_students,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # Class Insights
    # =====================================

    st.subheader("📋 Class Insights")

    highest_student = df.loc[

        df["Total_Marks"].idxmax()

    ]

    lowest_student = df.loc[

        df["Total_Marks"].idxmin()

    ]

    col1,col2 = st.columns(2)

    with col1:

        st.success(

            f"🏆 Highest Scorer : {highest_student['Name']}"

        )

        st.write(

            f"Marks : **{highest_student['Total_Marks']}**"

        )

        st.write(

            f"Percentage : **{highest_student['Percentage']}%**"

        )

        st.write(

            f"Grade : **{highest_student['Grade']}**"

        )

    with col2:

        st.warning(

            f"Lowest Scorer : {lowest_student['Name']}"

        )

        st.write(

            f"Marks : **{lowest_student['Total_Marks']}**"

        )

        st.write(

            f"Percentage : **{lowest_student['Percentage']}%**"

        )

        st.write(

            f"Grade : **{lowest_student['Grade']}**"

        )

    st.markdown("---")

    st.info(

        f"""
Class Summary

• Total Students : {total_students}

• Average Percentage : {average_percentage}%

• Highest Marks : {highest_marks}

• Lowest Marks : {lowest_marks}

• Grades Awarded : {len(grade_count[grade_count>0])}
"""
    )

# -------------------------------------------------------
# Charts Dashboard
# -------------------------------------------------------

elif page == "📈 Charts":

    st.title("📈 Visual Analytics Dashboard")

    st.markdown("---")

    # =====================================
    # Detect Assessment Columns
    # =====================================

    assessment_columns = [

        col

        for col in df.columns

        if col not in [

            "Name",
            "Email",
            "Total_Marks",
            "Percentage",
            "Grade",
            "Rank"

        ]

    ]

    # =====================================
    # Assessment Average
    # =====================================

    averages = pd.DataFrame({

        "Assessment": assessment_columns,

        "Average Marks": [

            round(df[col].mean(),2)

            for col in assessment_columns

        ]

    })

    fig = px.bar(

        averages,

        x="Assessment",

        y="Average Marks",

        color="Average Marks",

        text="Average Marks",

        title="Average Marks in Each Assessment"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # Student Percentage Ranking
    # =====================================

    ranking = (

        df

        .sort_values(

            "Percentage",

            ascending=False

        )

        .head(15)

    )

    fig = px.bar(

        ranking,

        x="Name",

        y="Percentage",

        color="Grade",

        text="Percentage",

        title="Top 15 Students by Percentage"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # Grade Distribution Pie Chart
    # =====================================

    left,right = st.columns(2)

    with left:

        grade_count = (

            df["Grade"]

            .value_counts()

            .reindex(GRADE_ORDER, fill_value=0)

        )

        pie_df = pd.DataFrame({

            "Grade": grade_count.index,

            "Students": grade_count.values

        })

        fig = px.pie(

            pie_df,

            names="Grade",

            values="Students",

            title="Grade Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================
    # Grade-wise Average
    # =====================================

    with right:

        grade_average = (

            df

            .groupby("Grade")["Percentage"]

            .mean()

            .reindex(GRADE_ORDER)

            .reset_index()

        )

        fig = px.bar(

            grade_average,

            x="Grade",

            y="Percentage",

            color="Grade",

            text="Percentage",

            title="Average Percentage by Grade"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # =====================================
    # Scatter Plot
    # =====================================

    fig = px.scatter(

        df,

        x="Rank",

        y="Percentage",

        color="Grade",

        hover_name="Name",

        size="Total_Marks",

        title="Rank vs Percentage"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# -------------------------------------------------------
# Reports
# -------------------------------------------------------

elif page == "📄 Reports":

    st.title("📄 Reports & Downloads")

    st.markdown("---")

    report_dir = Path("reports")
    gradecard_dir = report_dir / "gradecards"
    chart_dir = Path("charts")

    # =====================================
    # Excel Reports
    # =====================================

    st.subheader("📊 Excel Reports")

    report_files = [

        "Final_Student_Report.xlsx",
        "statistics.xlsx",
        "Top_Students.xlsx"

    ]

    cols = st.columns(3)

    for i, report in enumerate(report_files):

        path = report_dir / report

        with cols[i]:

            st.info(report)

            if path.exists():

                st.success("Available")

                with open(path, "rb") as file:

                    st.download_button(

                        "⬇ Download",

                        data=file,

                        file_name=report,

                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                        use_container_width=True

                    )

            else:

                st.error("Not Found")

    st.markdown("---")

    # =====================================
    # Grade Cards
    # =====================================

    st.subheader("🎓 Student Grade Cards")

    pdfs = sorted(

        gradecard_dir.glob("*.pdf")

    )

    if pdfs:

        selected_pdf = st.selectbox(

            "Select Student",

            pdfs,

            format_func=lambda x: x.stem.replace("_"," ")

        )

        st.success(selected_pdf.name)

        with open(selected_pdf,"rb") as file:

            st.download_button(

                "⬇ Download Grade Card",

                data=file,

                file_name=selected_pdf.name,

                mime="application/pdf",

                use_container_width=True

            )

    else:

        st.warning("No Grade Cards Found")

    st.markdown("---")

    # =====================================
    # Generated Charts
    # =====================================

    st.subheader("📈 Generated Charts")

    charts = sorted(

        chart_dir.glob("*.png")

    )

    if charts:

        selected_chart = st.selectbox(

            "Select Chart",

            charts,

            format_func=lambda x: x.name

        )

        st.image(

            selected_chart,

            use_container_width=True

        )

        with open(selected_chart,"rb") as file:

            st.download_button(

                "⬇ Download Chart",

                data=file,

                file_name=selected_chart.name,

                mime="image/png",

                use_container_width=True

            )

    else:

        st.warning("No Charts Available")

    st.markdown("---")

# =====================================
# Report Summary
# =====================================

    st.subheader("📋 Generated Files")

    excel_count = len(

        list(report_dir.glob("*.xlsx"))

    )

    pdf_count = len(

        list(gradecard_dir.glob("*.pdf"))

    )

    chart_count = len(

        list(chart_dir.glob("*.png"))

    )

    c1,c2,c3 = st.columns(3)

    c1.metric(

        "Excel Reports",

        excel_count

    )

    c2.metric(

        "Grade Cards",

        pdf_count

    )

    c3.metric(

        "Charts",

        chart_count
    )

# -------------------------------------------------------
# About
# -------------------------------------------------------

elif page == "⚙ About":

    st.title("⚙ About the Project")

    st.markdown("---")

    left, right = st.columns([1,3])

    with left:

        st.image(
            "assets/liet_logo.jpeg",
            width=180
        )

    with right:

        st.header("AI Student Assessment System")

        st.write(
            """
A complete automation platform developed to simplify
student assessment management.

The system automatically processes quiz data,
calculates marks, assigns grades and ranks,
generates Excel reports, creates professional PDF
grade cards, visualizes student performance through
interactive charts, and optionally emails grade cards
to students.
            """
        )

    st.markdown("---")

    # ===========================================
    # Features
    # ===========================================

    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✔ Automatic CSV Processing")

        st.success("✔ Data Validation")

        st.success("✔ Data Cleaning")

        st.success("✔ Student Ranking")

        st.success("✔ Grade Calculation")

        st.success("✔ Excel Report Generation")

    with col2:

        st.success("✔ PDF Grade Cards")

        st.success("✔ Interactive Dashboard")

        st.success("✔ Analytics & Charts")

        st.success("✔ Email Automation")

        st.success("✔ Logging System")

        st.success("✔ Modular Architecture")

    st.markdown("---")

    # ===========================================
    # Technology Stack
    # ===========================================

    st.subheader("🛠 Technology Stack")

    tech = pd.DataFrame({

        "Technology":[

            "Python",

            "Pandas",

            "Matplotlib",

            "Plotly",

            "Streamlit",

            "OpenPyXL",

            "ReportLab",

            "SMTP",

            "Git",

            "GitHub"

        ],

        "Purpose":[

            "Programming Language",

            "Data Processing",

            "Static Charts",

            "Interactive Charts",

            "Dashboard",

            "Excel Reports",

            "PDF Generation",

            "Email Service",

            "Version Control",

            "Repository Hosting"

        ]

    })

    st.dataframe(

        tech,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ===========================================
    # Project Statistics
    # ===========================================

    st.subheader("📊 Project Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Modules",
        "15+"
    )

    c2.metric(
        "Charts",
        "5"
    )

    c3.metric(
        "Reports",
        "3"
    )

    c4.metric(
        "Dashboard Pages",
        "6"
    )

    st.markdown("---")

    # ===========================================
    # Folder Structure
    # ===========================================

    st.subheader("📂 Project Structure")

    st.code(
"""
AI-Student-Assessment-System/
│
├── assets/
├── charts/
├── config/
├── dashboard/
├── data/
├── docs/
├── logs/
├── reports/
├── src/
├── templates/
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
""",
        language="text"
    )

    st.markdown("---")

    # ===========================================
    # Developer
    # ===========================================

    st.subheader("👨‍💻 Developer")

    st.info(
        """
**Devashish Dobhal**

B.Tech Artificial Intelligence & Machine Learning

Lloyd Institute of Engineering & Technology

This project was developed as a complete AI-based
student assessment automation system using Python
and Streamlit.

The project demonstrates software engineering,
data analytics, automation, report generation,
dashboard development, and data visualization.
        """
    )

    st.markdown("---")

    st.caption("Version 1.0.0 | AI Student Assessment System")