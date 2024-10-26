from app import db, create_app
from app.models import Company

app = create_app()

def seed_data():
    """Seed the database with initial data."""
    with app.app_context():
        companies = [
            Company(title='Company A', electricity=10, natural_gas=20, fuel=30, waste=40, recycled_percent=50, business_travels=60, fuel_efficiency=70, energy_usage=3.0, waste_generation=2.0, business_travel=1.0, total=10.0),
            Company(title='Company B', electricity=5, natural_gas=10, fuel=15, waste=20, recycled_percent=25, business_travels=30, fuel_efficiency=35, energy_usage=1.5, waste_generation=1.0, business_travel=0.5 , total=5.0)
        ]
        db.session.bulk_save_objects(companies)
        db.session.commit()
        print("Database has been seeded with initial data.")

if __name__ == "__main__":
    seed_data()