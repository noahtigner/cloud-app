import os, sys
from flask import (
    Flask, render_template, url_for, current_app, g
)

from . import util
from .util.utilities import set_output
from .util.utilities import my_print as print


def create_app():
    util.load_config("config.json")
    
    application = Flask(__name__, template_folder=util.config["common"]["TEMPLATE_PATH"], static_folder=util.config["common"]["STATIC_PATH"]) 

    application.config.from_mapping(
        SECRET_KEY=util.config["common"]["SECRET_KEY"]
    )

    set_output(sys.stderr)

    # Register blueprints & initialize db
    with application.app_context():
        from . import server, portfolio, db, auth, api
        
        db.init_app(application)
        application.register_blueprint(server.bp)
        application.register_blueprint(portfolio.bp)
        application.register_blueprint(auth.bp)
        application.register_blueprint(api.bp)

    return application

