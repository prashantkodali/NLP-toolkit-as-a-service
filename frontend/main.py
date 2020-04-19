from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('pages/placeholder.home.html')

@main.route('/about',methods = ['GET','POST'])
def about():
    return render_template('pages/placeholder.about.html')
