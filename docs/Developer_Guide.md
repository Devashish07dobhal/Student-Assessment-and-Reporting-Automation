# Developer Guide

## Project Architecture

The project follows a modular architecture.

```text
src/
├── loader.py
├── validator.py
├── cleaner.py
├── merger.py
├── calculator.py
├── analytics.py
├── report_generator.py
├── pdf_generator.py
├── chart_generator.py
├── email_sender.py
├── logger.py
└── pipeline.py
```

---

## Workflow

1. Load quiz data
2. Validate datasets
3. Clean data
4. Merge assessments
5. Calculate grades
6. Generate analytics
7. Create reports
8. Generate PDFs
9. Generate charts
10. Send emails

---

## Configuration

Located in:

```text
config/
```

Contains:

* settings.py
* grading.py

---

## Dashboard

Dashboard is developed using Streamlit.

Entry file:

```text
dashboard/app.py
```

---

## Logging

All application logs are stored in:

```text
logs/application.log
```
