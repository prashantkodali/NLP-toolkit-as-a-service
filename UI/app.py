#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, flash, url_for, jsonify
#from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
import requests

from werkzeug.security import generate_password_hash, check_password_hash
#from models_db import User


from nltk.tokenize import word_tokenize

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')

@app.route('/about',methods = ['GET','POST'])
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/logged_in',methods = ['GET','POST'])
def logged_in():
    return render_template('pages/loginSuccess.home.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)

    # if form.validate_on_submit():
    #     #flash('Login requested for user {}, remember_me={}'.format(form.name.data, form.remember_me.data))
    #     return redirect('pages/loginSuccess.home.html')

    return render_template('forms/login.html', form=form)
	

@app.route('/register', methods = ['GET', 'POST'])
def register():

    if request.method == 'GET':
        form = RegisterForm(request.form)
        return render_template('forms/register.html', form=form)

    elif request.method == 'POST':

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('auth.signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        print('User created')

        # return redirect(url_for('auth.login'))


        return render_template('forms/login.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)
	
@app.route('/logout',methods=['POST'])
def logout():
    return render_template('pages/placeholder.home.html')


#---------------------------------------------------------------------------------#
# Service Calls 
#---------------------------------------------------------------------------------#
@app.route('/tokenizer_page',methods = ['GET','POST'])
def tokenizer_page():
    # form = TokenizerForm(request.form)
    # text =
    return render_template('pages/tokenize.html')


@app.route('/tokenize_call',methods = ['GET','POST'])
def tokenize_call():
    text = request.form['text']
    td = {'text':text }
    response = requests.post("http://192.168.1.6:5000/ntlktokenize", json = td)

    print(response.json())

    return response.json()
    # return 'Tokenized text: {}'.format(word_tokenize(text))





# Error handlers.



@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
