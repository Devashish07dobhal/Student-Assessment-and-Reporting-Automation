# User Manual

## Introduction

The AI Student Assessment System automates the student evaluation process by generating reports, grade cards, charts, and analytics.

---

## Main Menu

After running `main.py`, select one of the following options:

1. Complete Assessment
2. Generate Excel Reports
3. Generate PDF Grade Cards
4. Generate Charts
5. Send Emails
6. View Analytics
7. Exit

---

## Dashboard

Run:

```bash
streamlit run dashboard/app.py
```

The dashboard includes:

* Dashboard
* Students
* Analytics
* Charts
* Reports
* About

---

## Reports

Generated reports are stored in:

```text
reports/
```

PDF Grade Cards:

```text
reports/gradecards/
```

Charts:

```text
charts/
```

---

## Notes

* Student email addresses are hidden from the dashboard.
* Reports are generated automatically after assessment.
* Logs are stored inside the `logs` folder.
