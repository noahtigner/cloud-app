import os, sys
from flask import (
    Flask, render_template, url_for, current_app, g
)
# from config import Config

def create_app():
    application = Flask(__name__)

    application.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(application.instance_path, "app.sqlite"),
        # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(application.instance_path, 'example.db'),
        # SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    # print(application.config['SQLALCHEMY_DATABASE_URI'], file=sys.stderr)
    # ensure the instance folder exists
    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    # db = SQLAlchemy(application)

    # class ExampleTable(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    
    # db.create_all()


    # Register blueprints & initialize db
    with application.app_context():
        from . import portfolio, db, auth, api
        
        db.init_app(application)
        application.register_blueprint(portfolio.bp)
        application.register_blueprint(auth.bp)
        application.register_blueprint(api.bp)

    return application

