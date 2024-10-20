# app/routes.py

from flask import Blueprint, render_template, redirect, url_for
from .forms import CompanyForm
from .models import Company
from . import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=('GET', 'POST'))
def index():
    form = CompanyForm()

    if form.validate_on_submit():
        # Create a new company record
        new_company = Company(
            title=form.title.data,
            electricity=form.electricity.data,
            natural_gas=form.natural_gas.data,
            fuel=form.fuel.data,
            waste=form.waste.data,
            recycled_percent=form.recycled_percent.data,
            business_travels=form.business_travels.data,
            fuel_efficiency=form.fuel_efficiency.data
        )

        # Add the new company to the database
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('index.html', form=form)


@main_bp.route('/companies/')
def companies():
    # Load companies from the database
    companies_list = Company.query.all()
    return render_template('companies.html', companies_list=companies_list)
