# app/seed.py

from app import db, create_app
from app.models import Company

app = create_app()

with app.app_context():
    # Create multiple company entries
    companies = [
        Company(title='Company A', electricity=10, natural_gas=20, fuel=30, waste=40, recycled_percent=50,
                business_travels=60, fuel_efficiency=70),
        Company(title='Company B', electricity=5, natural_gas=10, fuel=15, waste=20, recycled_percent=25,
                business_travels=30, fuel_efficiency=35)
    ]

    # Add the companies to the session in bulk and commit
    db.session.bulk_save_objects(companies)
    db.session.commit()

    print("Database seeded successfully!")
