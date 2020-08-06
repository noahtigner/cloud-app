import functools
import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
import jwt

from nzt.db import db_query
import nzt.portfolio
from nzt.util import config

bp = Blueprint("auth", __name__, url_prefix="/auth")

################################################################################################################################
### Decorators   
###

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

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
            # current_user = Users.query.filter_by(public_id=data['user_id']).first()
            g.user = db_query(f"""SELECT * FROM "user" WHERE id='{data['user_id']}' """, unique=True)
            session['user_id'] = g.user['id']
            # session['token'] = token
        except:
            return jsonify({'message': 'token is invalid'})

        return view(*args, **kwargs)
    return wrapped_view

################################################################################################################################
### Helpers   
###

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db_query(f"""SELECT * FROM "user" WHERE id='{user_id}' """, unique=True)

################################################################################################################################
### Routes   
###

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db_query(f"""SELECT * FROM "user" WHERE username='{username}' """, unique=True) is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db_query(
                f"""
                INSERT INTO "user" (username, password) 
                VALUES ('{username}', '{generate_password_hash(password)}')
                """
            )
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = db_query(f"""SELECT * FROM "user" WHERE username='{username}' """, unique=True)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']

            token = jwt.encode({'user_id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config["common"]["SECRET_KEY"])

            response = redirect(url_for('portfolio.index'))
            response.headers['x-access-tokens'] = token.decode('UTF-8')
            return response

        flash(error)

    return render_template('auth/login.html')

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("portfolio.index"))

@bp.route("/token")
def get_token():
    error = None

    username = request.args.get('username', None)
    password = request.args.get('password', None)

    user = db_query(f"""SELECT * FROM "user" WHERE username='{username}' """, unique=True)

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']

        token = jwt.encode({'user_id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config["common"]["SECRET_KEY"])

        return {'token' : token.decode('UTF-8')}

    flash(error)
    print(error)

    return render_template('auth/login.html')
