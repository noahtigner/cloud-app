import time
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from nzt.db import db_query
from nzt.auth import login_required


bp = Blueprint('api', __name__, url_prefix="/api")

@bp.route('/time', methods=('GET', 'POST'))
def api_get_current_time():
    return {'time': time.time()}

@bp.route("/db", methods=("GET", "POST"))
@login_required
def api_get_db():
    users = [[item for item in row] for row in db_query("""SELECT * FROM "user" """)]
    visits = [[item for item in row] for row in db_query(""" SELECT * FROM "visits" """)]

    return {'users': users, 'visits': visits}