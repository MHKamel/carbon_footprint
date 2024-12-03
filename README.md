# carbon_footprint
# Carbon Footprint Monitoring Tool

## Introduction
This project is a web-based application that helps organizations track and reduce their carbon footprint. Users can input data related to their activities, and the tool generates reports with detailed analysis and suggestions for reduction.

## Features
- **Data Input:** Input data for energy usage, waste generation, and business travel.
- **Report Generation:** Generate PDF reports summarizing the carbon footprint.
- **Visualizations:** View charts and graphs to understand carbon footprint breakdown.

## Prerequisites
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Database Setup
Create and seed the database:
```bash
python -m app.create_db
python -m app.seed
```

## Running the Application
Start the application:
```bash
python run.py
```

## Running the Tests
Run the unit tests:
```bash
python -m unittest discover
```

## References
- Sample Project
- Flask WTForms
- WTForms Documentation
- Using SQLite with Flask

---
