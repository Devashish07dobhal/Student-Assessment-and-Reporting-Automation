# System Architecture

## Overview

The AI Student Assessment System processes student assessment data through a sequence of modules.

```text
Quiz CSV Files
       │
       ▼
Loader
       │
       ▼
Validator
       │
       ▼
Cleaner
       │
       ▼
Merger
       │
       ▼
Grade Calculator
       │
       ▼
Analytics
       │
 ┌─────┼───────────────┐
 ▼     ▼               ▼
Reports PDFs         Charts
       │
       ▼
Email Sender
       │
       ▼
Dashboard
```

---

## Components

### Data Layer

* Quiz CSV files
* Student master list

### Processing Layer

* Validation
* Cleaning
* Merging
* Grade Calculation

### Output Layer

* Excel Reports
* PDF Grade Cards
* Charts
* Dashboard
* Email Notifications

---

## Technologies

* Python
* Pandas
* Matplotlib
* Plotly
* Streamlit
* ReportLab
* OpenPyXL
* Python-dotenv
