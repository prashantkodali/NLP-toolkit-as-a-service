'''
Blueprint for routes related to home pages and other pages of the frontend.
'''

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .forms import *
from .models_db import Service

main = Blueprint('main', __name__)


def getservices():

    servicesall = Service.query.all()

    services = []

    for service in servicesall:
        services.append([service.service_page_call, service.service_name])

    return services

@main.route('/')
def home():
    return render_template('pages/placeholder.home.html')

@main.route('/loggedin')
@login_required
def loginSuccess():
    services = getservices()
    if current_user.user_type == 'User':
        return render_template('pages/loginSuccess.home.html', services = services)
    elif current_user.user_type == 'Admin':
        return render_template('pages/loginSuccess.Admin.home.html', services = services)


@main.route('/loggedinAdmin')
@login_required
def loginSuccessAdmin():
    return render_template('pages/loginSuccess.Admin.home.html')

@main.route('/addservice')
def addservice():
    form = AddServiceForm(request.form)
    return render_template('forms/service_entry.html', form = form)

@main.route('/addservice', methods = ['POST'])
def addservice_post():

    serviceName = request.form.get('serviceName')
    serviceAuthor = request.form.get('serviceAuthor')
    servicePageCall = request.form.get('servicePageCall')
    serviceServiceCall = request.form.get('serviceServiceCall')
    serviceAPIEndpoint = request.form.get('serviceAPIEndpoint')
    serviceTags = request.form.get('serviceTags')

    service = Service.query.filter_by(service_name = serviceName).first()
    if service:
        flash("Service name already exists please enter different service name.")
        return redirect(url_for('main.addservice'))

    service = Service.query.filter_by(service_page_call = servicePageCall).first()
    if service:
        flash("Service page URL call already exists please enter different service page call.")
        return redirect(url_for('main.addservice'))

    service = Service.query.filter_by(service_service_call = serviceServiceCall).first()
    if service:
        flash("Service call URL already exists please enter different service URL call.")
        return redirect(url_for('main.addservice'))

    service = Service.query.filter_by(service_api_endpoint = serviceAPIEndpoint).first()
    if service:
        flash("Service API endpoint already exists please enter different service API endpoint.")
        return redirect(url_for('main.addservice'))

    new_service = Service(service_name = serviceName, \
                          service_author = serviceAuthor, \
                          service_page_call = servicePageCall,\
                          service_service_call = serviceServiceCall,\
                          service_api_endpoint = serviceAPIEndpoint,\
                          service_tags = serviceTags)

    db.session.add(new_service)
    db.session.commit()

    flash("Service added to database. Please add necessary HTML pages and methods to service.py.")

    # form = AddServiceForm(request.form)
    return redirect(url_for('main.addservice'))
    # return render_template('forms/service_entry.html', form = form, flash = flash_message)

@main.route('/about',methods = ['GET','POST'])
def about():
    return render_template('pages/placeholder.about.html')
