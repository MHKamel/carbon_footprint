from flask import Blueprint, render_template, redirect, url_for
from .forms import CompanyForm
from . import db
from .models import Company

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
        # Calculate and update the company with the energy usage
        new_company.calculate_carbon_footprints()

        # Add the new company to the database
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for("main.companies", company_id=new_company.id))

    return render_template('index.html', form=form)


@main_bp.route("/companies", defaults={'company_id': None})
@main_bp.route("/companies/<int:company_id>")
def companies(company_id):
    if company_id:
        # Display a single company's details
        company = Company.query.get_or_404(company_id)
        return render_template("company_detail.html", company=company)
    else:
        # Display a list of all companies
        companies_list = Company.query.all()
        return render_template("companies.html", companies_list=companies_list)

@main_bp.route("/delete_company/<int:company_id>", methods=["GET"])
def delete_company(company_id):
    company = Company.query.get_or_404(company_id)
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('main.companies'))