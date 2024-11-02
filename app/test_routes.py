import unittest
from flask import url_for
from app import create_app, db
from app.models import Company

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test app and database."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SERVER_NAME'] = 'localhost'
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down the test database."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_index_post(self):
        """Test POST request to create a new company."""
        data = {
            'title': 'Test Company',
            'electricity': 100,
            'natural_gas': 50,
            'fuel': 20,
            'waste': 10,
            'recycled_percent': 30,
            'business_travels': 5,
            'fuel_efficiency': 15
        }
        with self.app.test_request_context():
            response = self.client.post(url_for('main.index'), data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Company', response.data)

    def test_companies_get_all(self):
        """Test GET request to retrieve all companies."""
        company = Company(
            title='Company A', electricity=10, natural_gas=20, fuel=30,
            waste=40, recycled_percent=50, business_travels=60,
            fuel_efficiency=70, energy_usage=3.0, waste_generation=2.0,
            business_travel=1.0, total=10.0
        )
        db.session.add(company)
        db.session.commit()

        with self.app.test_request_context():
            response = self.client.get(url_for('main.companies'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Company A', response.data)

    def test_companies_get_single(self):
        """Test GET request to retrieve a single company's details."""
        company = Company(
            title='Company B', electricity=15, natural_gas=10, fuel=25,
            waste=20, recycled_percent=30, business_travels=50,
            fuel_efficiency=60, energy_usage=2.5, waste_generation=1.5,
            business_travel=0.8, total=7.8
        )
        db.session.add(company)
        db.session.commit()

        with self.app.test_request_context():
            response = self.client.get(url_for('main.companies', company_id=company.id))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Company B', response.data)

    def test_delete_company(self):
        """Test deleting a company by ID."""
        company = Company(
            title='Company C', electricity=5, natural_gas=10, fuel=15,
            waste=20, recycled_percent=25, business_travels=10,
            fuel_efficiency=35, energy_usage=1.2, waste_generation=0.8,
            business_travel=0.5, total=2.5
        )
        db.session.add(company)
        db.session.commit()

        with self.app.test_request_context():
            response = self.client.get(url_for('main.delete_company', company_id=company.id), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertNotIn(b'Company C', response.data)

if __name__ == '__main__':
    unittest.main()
