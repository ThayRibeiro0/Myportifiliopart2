from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template("base.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/experiences')
def experiences():
    return render_template("experiences.html")

@views.route('/skills')
def skills():
    return render_template("skills.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")