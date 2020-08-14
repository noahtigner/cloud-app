import functools
import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from flask_cors import cross_origin
from werkzeug.security import check_password_hash, generate_password_hash
import jwt

from api.db import db_query
import api.portfolio
from api.util import config

bp = Blueprint("auth", __name__, url_prefix="/auth")

################################################################################################################################
### Decorators   
###

def token_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        # token = session.get('token')
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            print(token)
        
        if not token:
            print("NOTHING HERE")
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, config["common"]["SECRET_KEY"])
            g.user = db_query(f"""SELECT * FROM "user" WHERE id='{data['user_id']}' """, unique=True)
        except:
            return jsonify({'message': 'token is invalid'})

        return view(*args, **kwargs)
    return wrapped_view

################################################################################################################################
### Routes   
###

@bp.route("/api-login", methods=['POST'])
@cross_origin()
def api_login():
    # print(request.__dict__)
    data = request.get_json(force=True)
    if not ('username' in data and 'password' in data):
        return {'success': False}, 400

    username = data['username']
    password = data['password']

    user = db_query(f"""SELECT * FROM "user" WHERE username='{username}' """, unique=True)
    
    error = None
    if user is None:
        error = 'Incorrect username'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password'

    if error is None:
        session.clear()
        session['user_id'] = user['id']

        token = jwt.encode({'user_id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config["common"]["SECRET_KEY"])

        response = {'success': True}, 200, {'x-access-tokens': token.decode('UTF-8'), 'Content-Type': 'application/json', 'access-control-expose-headers': '*'}
        # response.headers['x-access-tokens'] = token.decode('UTF-8')
        return response

    return {
        'success': False,
        'message': error
    }, 400

@bp.route('/api-register', methods=['POST'])
@cross_origin()
def api_register():
    data = request.get_json(force=True)
    # print(data)
    if not ('username' in data and 'password' in data):
        return {
        'success': False,
        'message': "missing username or password"
    }, 400

    username = data['username']
    password = data['password']

    error = None

    if not username:
        error = 'username is required'
    elif not password:
        error = 'password is required'
    elif db_query(f"""SELECT * FROM "user" WHERE username='{username}' """, unique=True) is not None:
        error = 'Username \'{}\' is taken'.format(username)

    if error is None:
        db_query(
            f"""
            INSERT INTO "user" (username, password) 
            VALUES ('{username}', '{generate_password_hash(password)}')
            """
        )
        return {
            'success': True,
            'message': 'proceed to login'
        }, 200

    return {
        'success': False,
        'message': error
    }, 400

