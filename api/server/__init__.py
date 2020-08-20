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

@bp.route("/manifest.json")
def manifest():
    return send_from_directory('./build/static', 'manifest.json')


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory('./build/static', 'favicon.ico')

@bp.route('/blue.png')
def b():
    if os.path.exists(config["common"]["STATIC_PATH"] + '/blue.png'):
        print("HERE", color='red')
    if os.path.exists('./build/static/blue.png'):
        print("HERE", color='red')
    if os.path.exists('../build/static/blue.png'):
        print("HERE", color='red')
    if os.path.exists('../client/build/static/blue.png'):
        print("HERE", color='red')

    return send_from_directory('./build/static', 'blue.png')

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def serve(path):
    print(config["common"]["IMAGE_PATH"] + '/' + path)
    if path != "" and os.path.exists(config["common"]["STATIC_PATH"] + '/' + path):
        return send_from_directory(config["common"]["STATIC_PATH"], path)
    elif path != "" and os.path.exists('./static/' + path):
        return send_from_directory('./static', path)
    else:
        return send_from_directory(config["common"]["TEMPLATE_PATH"], 'index.html')

# @bp.route('/')
# def index():
#     return send_from_directory(config["common"]["TEMPLATE_PATH"], 'index.html')
