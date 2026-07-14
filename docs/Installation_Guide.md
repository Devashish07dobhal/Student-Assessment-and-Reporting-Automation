# Installation Guide

## Prerequisites

Before running the project, install:

* Python 3.11 or later
* Git (optional)
* Visual Studio Code (recommended)

---

## Clone the Repository

```bash
git clone https://github.com/your-username/AI-Student-Assessment-System.git
```

Navigate to the project directory:

```bash
cd AI-Student-Assessment-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Email (Optional)

Create a `.env` file in the project root.

Example:

```text
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
```

---

## Run the Project

Main Application:

```bash
python main.py
```

Dashboard:

```bash
streamlit run dashboard/app.py
```

---

## Generated Output

The project generates:

* Excel Reports
* PDF Grade Cards
* Charts
* Logs
* Dashboard Analytics
