# app/models.py

from . import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    electricity = db.Column(db.Integer, nullable=False)
    natural_gas = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.Integer, nullable=False)
    waste = db.Column(db.Integer, nullable=False)
    recycled_percent = db.Column(db.Integer, nullable=False)
    business_travels = db.Column(db.Integer, nullable=False)
    fuel_efficiency = db.Column(db.Integer, nullable=False)
