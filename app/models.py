from . import db


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    electricity = db.Column(db.Integer, nullable=False)
    natural_gas = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.Integer, nullable=False)
    waste = db.Column(db.Integer, nullable=False)
    recycled_percent = db.Column(db.Integer, nullable=False)
    business_travels = db.Column(db.Integer, nullable=False)
    fuel_efficiency = db.Column(db.Integer, nullable=False)
    energy_usage = db.Column(db.Float, nullable=False)

    def calculate_energy_usage(self) -> float:
        self.energy_usage = ((self.electricity * 12 * 0.0005)
                             + (self.natural_gas * 12 * 0.0053)
                             + (self.fuel * 12 * 2.32))
        return self.energy_usage

    def calculate_waste_generation(self) -> float:
        return 0

    def calculate_business_travel(self) -> float:
        return 0

    def calculate_carbon_footprints(self) -> float:
        total = self.calculate_energy_usage() + self.calculate_waste_generation() + self.calculate_business_travel()
        return total

    def __repr__(self):
        return f"<Company {self.title}>"
