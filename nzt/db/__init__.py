import sys
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext
    
def init_app(application):
    application.teardown_appcontext(db_close)
    db_init()

def db_get():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def db_init():
    db = db_get()


    exists = db_query("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ("user",))
    if not exists:
        with current_app.open_resource("../schema.sql") as f:
            db.executescript(f.read().decode("utf8"))
        print("Creating DB", file=sys.stderr)   

    # try:
    #     db.execute(
    #                 'INSERT INTO user (username, password) VALUES (?, ?)',
    #                 ("Noah", "pass123")
    #             )
    #     db.execute(
    #             'INSERT INTO user (username, password) VALUES (?, ?)',
    #             ("James", "pass123")
    #         )
    #     db.commit()
    # except Exception:
    #     pass

    # try:
        
    #     users = db_query('SELECT * FROM user')
    #     print(users[-1]['password'], file=sys.stderr)
    #     users = db_query('SELECT * FROM user WHERE id=?', (1,))
    #     print(users[0]['password'], file=sys.stderr)

    #     if users is None:
    #         print("ERROR\n\n", file=sys.stderr)
    # except sqlite3.OperationalError:
    #     print("ERROR\n\n", file=sys.stderr)

def db_close(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def db_query(statement, params=None, unique=False):
    db = db_get()
    c = db.cursor()

    if params and unique:
        results = c.execute(statement, params).fetchone()
    elif params:
        results = c.execute(statement, params).fetchall()
    elif unique:
        results = c.execute(statement).fetchone()
    else:
        results = c.execute(statement).fetchall()
    db.commit()
    
    return results