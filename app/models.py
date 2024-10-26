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
    waste_generation = db.Column(db.Float, nullable=False)
    business_travel = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def calculate_energy_usage(self) -> float:
        self.energy_usage = ((self.electricity * 12 * 0.0005)
                             + (self.natural_gas * 12 * 0.0053)
                             + (self.fuel * 12 * 2.32))
        return self.energy_usage

    def calculate_waste_generation(self) -> float:
        self.waste_generation = ((self.waste * 12) * (0.57 - self.recycled_percent))
        return self.waste_generation

    def calculate_business_travel(self) -> float:
        self.business_travel = (self.business_travels * (1 / self.fuel_efficiency) * 2.31)
        return self.business_travel

    def calculate_carbon_footprints(self) -> float:
        self.total = self.calculate_energy_usage() + self.calculate_waste_generation() + self.calculate_business_travel()
        return self.total

    def __repr__(self):
        return f"<Company {self.title}>"
