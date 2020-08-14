import sys
import psycopg2
import psycopg2.extras
from flask import current_app, g
from flask.cli import with_appcontext

from api.util import config

def init_app(application):
    application.teardown_appcontext(db_close)
    db_init()

def db_get():
    if 'db3' not in g:
        print("DATABASE: opening database connection")
        g.db3 = psycopg2.connect(**config["database"])
    else:
        print("DATABASE: accessing database connection")
    return g.db3

def db_init():
    print("DATABASE: initializing database control")
    db = db_get()
    db_create_tables()

def db_create_tables():
    print("DATABASE: creating tables")
    commands = (
        """
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS "visits" (
            ip VARCHAR(255) PRIMARY KEY NOT NULL,
            count INTEGER NOT NULL,
            latest TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    try:
        db = db_get()
        c = db.cursor()

        for command in commands:
            c.execute(command)

        c.close()
        db.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("DATABASE: ERROR: " + error, color="red")
        db.rollback()

def db_close(e=None):
    print("DATABASE: closing connection")
    db = g.pop("db3", None)

    if db is not None:
        db.close()

def db_query(statement, params=None, unique=False):
    print(f"DATABASE: executing statement: {statement}")
    results = []
    try:
        db = db_get()
        c = db.cursor(cursor_factory = psycopg2.extras.DictCursor)

        if params:
            c.execute(statement, params)
        else:
            c.execute(statement)

        db.commit()

        if unique:
            results = c.fetchone()
        else:
            results = [row for row in c.fetchall()]

    except (Exception, psycopg2.DatabaseError) as error:
        print("DATABASE: ERROR: " + error, color="red")
        db.rollback()
    finally:
        c.close()
        return results