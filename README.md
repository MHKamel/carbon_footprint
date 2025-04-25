
# Carbon Footprint Monitoring Tool

## 🌍 Introduction
This project is a web-based application that helps organizations track and reduce their carbon footprint. Users can input data related to energy, waste, and travel to generate a report with breakdowns and suggestions for reduction.

## 🚀 Features
- **Data Input:** Forms for entering electricity, gas, fuel, waste, and travel data.
- **Calculations:** Computes energy usage, waste output, and travel emissions.
- **Visualizations:** Interactive charts to display company emission profiles.
- **Reports:** Detailed total carbon footprint per company.
- **CRUD:** Add, view, and delete companies.

---

## 📦 Prerequisites

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Database Setup

Create and seed the SQLite database:

```bash
python create_db.py
python seed.py
```

---

## ▶️ Running the Application

```bash
python run.py
```

Or, with Gunicorn (for production-like servers):

```bash
gunicorn run:app
```

---

## 🧪 Running Tests

```bash
python -m unittest discover
```

Your test suite includes:
- Adding companies
- Viewing single & multiple companies
- Deleting companies

---

## 🔁 CI/CD with GitHub Actions

This project uses GitHub Actions to:
- Auto-install dependencies
- Run tests on each push to `main`

Create `.github/workflows/test.yml` with:

```yaml
name: CI - Flask Test Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest flask-testing

      - name: Run tests
        run: |
          python -m unittest discover -s . -p "test_*.py"
```

---

## 🌐 Deploying on Render

1. Go to [https://render.com](https://render.com) and create a new Web Service
2. Connect your GitHub repo
3. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn run:app`
   - Add env var: `FLASK_ENV=production`
4. Deploy! It will rebuild automatically on `git push`.

---

## 📚 References
- Flask Docs: https://flask.palletsprojects.com/
- WTForms Docs: https://wtforms.readthedocs.io/
- Render Python Guide: https://render.com/docs/deploy-flask
- GitHub Actions for Python: https://docs.github.com/en/actions

---

## ✨ Demo (Optional)
> You can add your live Render app link here once deployed
