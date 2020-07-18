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
        f""" 
        INSERT INTO "visits" (ip, count) 
        VALUES('{ip}', {1})  
        ON CONFLICT (ip) DO
            UPDATE SET count=visits.count+1 WHERE visits.ip='{ip}' 
        """
    )

    return render_template('index.html')