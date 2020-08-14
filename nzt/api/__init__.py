import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_cors import cross_origin

from nzt.db import db_query
from nzt.auth import token_required


bp = Blueprint('api', __name__, url_prefix="/api")
led_on = True

@bp.route('/', methods=['GET'])
def api_get_endpoints():
    return {
        'time':         'https://noahtigner.com/api/time',
        'db':           'https://noahtigner.com/api/db',
        'led_status':   'https://noahtigner.com/api/led_status',
        'led_toggle':   'https://noahtigner.com/api/led_toggle',
    }

@bp.route('/time', methods=['GET', 'POST'])
@token_required
def api_get_current_time():
    return {'time': time.time()}

@bp.route("/db", methods=["GET", "POST"])
def api_get_db():
    users = [[item for item in row] for row in db_query("""SELECT * FROM "user" """)]
    visits = [[item for item in row] for row in db_query(""" SELECT * FROM "visits" """)]

    return {'users': users, 'visits': visits}

@bp.route("/dash", methods=["GET", "POST"])
@token_required
def api_dash():
    return render_template('api/dash.html')

@bp.route("/led_status", methods=["GET", "POST"])
@token_required
def api_get_led_status():
    global led_on
    return {"led_on": led_on}

@bp.route("/led_toggle", methods=['GET', 'POST'])
# @token_required
def api_led_toggle():
    global led_on
    b = request.args.get('on', None)
    led_on = b if b is not None else False
    return {"led_on": led_on}

    

