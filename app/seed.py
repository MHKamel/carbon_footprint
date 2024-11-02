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
                electricity=800,          # kWh
                natural_gas=120,         # Therms
                fuel=200,                # Gallons of fuel
                waste=1500,              # Pounds of waste
                recycled_percent=0.3,      # 30% recycled
                business_travels=1000,     # 10 trips
                fuel_efficiency=0.25       # 25 mpg
            ),
            Company(
                title='Company B',
                electricity=500,          # kWh
                natural_gas=80,          # Therms
                fuel=100,                # Gallons of fuel
                waste=800,               # Pounds of waste
                recycled_percent=0.20,      # 20% recycled
                business_travels=500,      # 5 trips
                fuel_efficiency=0.30       # 30 mpg
            ),
            Company(
                title='Company C',
                electricity=1200,         # kWh
                natural_gas=150,         # Therms
                fuel=300,                # Gallons of fuel
                waste=2000,              # Pounds of waste
                recycled_percent=0.40,      # 40% recycled
                business_travels=1500,     # 15 trips
                fuel_efficiency=0.20       # 20 mpg
            ),
            Company(
                title='Company D',
                electricity=600,          # kWh
                natural_gas=60,          # Therms
                fuel=50,                 # Gallons of fuel
                waste=1000,              # Pounds of waste
                recycled_percent=0.50,      # 50% recycled
                business_travels=3000,      # 3 trips
                fuel_efficiency=0.35       # 35 mpg
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
