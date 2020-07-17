import sys
from flask import (
    Blueprint, render_template, request, url_for
)

from nzt.db import db_query

bp = Blueprint('portfolio', __name__)

@bp.route('/')
def index():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    db_query(
        'UPDATE visits SET count=count+1 WHERE ip=? ',
        (ip,)
    )
    db_query(
        'INSERT OR IGNORE INTO visits (ip, count) VALUES (?, ?) ',
        (ip, 0,)
    )

    return render_template('index.html')