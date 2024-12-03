from app import db, create_app
from app.models import Company

app = create_app()

def seed_data():
    """Seed the database with initial data."""
    with app.app_context():
        # Clear existing data
        db.session.query(Company).delete()

        # Create company instances with realistic data
        companies = [
            Company(
                title='Company A',
                electricity=800,
                natural_gas=120,
                fuel=200,
                waste=1500,
                recycled_percent=0.3,
                business_travels=1000,
                fuel_efficiency=0.25
            ),
            Company(
                title='Company B',
                electricity=500,
                natural_gas=80,
                fuel=100,
                waste=800,
                recycled_percent=0.20,
                business_travels=500,
                fuel_efficiency=0.30
            ),
            Company(
                title='Company C',
                electricity=1200,
                natural_gas=150,
                fuel=300,
                waste=2000,
                recycled_percent=0.40,
                business_travels=1500,
                fuel_efficiency=0.20
            ),
            Company(
                title='Company D',
                electricity=600,
                natural_gas=60,
                fuel=50,
                waste=1000,
                recycled_percent=0.50,
                business_travels=3000,
                fuel_efficiency=0.35
            )
        ]

        # Calculate and populate calculated fields
        for company in companies:
            company.calculate_carbon_footprints()  # This will set energy_usage, waste_generation, business_travel, and total

        # Bulk save the objects to the database
        db.session.bulk_save_objects(companies)
        db.session.commit()
        print("Database has been seeded with initial data.")

if __name__ == "__main__":
    seed_data()
