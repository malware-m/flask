
from flask import Flask
from flask_sqlalchemy import SQLALchemy

db=SQLALchemy()  # create a DB object

def create_app(): # create fun and 
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///site.db' # set configuration and path to database

    db.init_app(app)
    return app