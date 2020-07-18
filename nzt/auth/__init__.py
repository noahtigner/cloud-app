import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from nzt.db import db_query
import nzt.portfolio

bp = Blueprint("auth", __name__, url_prefix="/auth")

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

@bp.route('/login', methods=('GET', 'POST'))
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
            return redirect(url_for('portfolio.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("portfolio.index"))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db_query(f"""SELECT * FROM "user" WHERE id='{user_id}' """, unique=True)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view