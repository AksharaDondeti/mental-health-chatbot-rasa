from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import requests

auth = Blueprint('auth', __name__)

@auth.route('/index')
def index():
    return render_template('index.html')  # Render your HTML template
@auth.route('/index', methods=['POST'])
def parse_user_input():
    user_input = request.form.get('user_input')  # Extract user input
    # Send user input to Rasa chatbot and get the response
    # (You'll need to implement this part)
    chatbot_response = get_rasa_response(user_input)
    return chatbot_response


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):

                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/Aboutus')
def about_us():
    return render_template("Aboutus.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


def get_rasa_response(user_input):
    rasa_endpoint = 'http://localhost:5005/webhooks/rest/webhook'
    payload = {'sender': 'user', 'message': user_input}
    response = requests.post(rasa_endpoint, json=payload)

    if response.status_code == 200:
        try:
            chatbot_response = response.json()
            if chatbot_response and len(chatbot_response) > 0:
                return chatbot_response[0]['text']
            else:
                return "Sorry i don't understand that?Anything else?"
        except (IndexError, KeyError):
            return "Error: Invalid response format from the chatbot"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return f"Error: Failed to connect to Rasa endpoint ({response.status_code})"
