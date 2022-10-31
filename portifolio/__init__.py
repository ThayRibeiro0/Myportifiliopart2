from flask import Flask, url_for

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = 'kjhdsjkhdkjdklfl jhdfhjfdjkf'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

