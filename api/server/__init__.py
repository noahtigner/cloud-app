import sys, os
from flask import (
    Blueprint, render_template, request, url_for, send_from_directory, redirect
)
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from api.db import db_query
from api.util import config

bp = Blueprint('server', __name__)

# @bp.route('/')
# def index():
#     ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

#     db_query(
#         f""" 
#         INSERT INTO "visits" (ip, count) 
#         VALUES('{ip}', {1})  
#         ON CONFLICT (ip) DO
#             UPDATE SET count=visits.count+1 WHERE visits.ip='{ip}' 
#         """
#     )

    # return render_template('index.html')
    # return render_template('index.html')

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(config["common"]["STATIC_PATH"] + '/' + path):
        return send_from_directory(config["common"]["STATIC_PATH"], path)
    else:
        return send_from_directory(config["common"]["TEMPLATE_PATH"], 'index.html')

