from flask import Flask     # import flask
from flask_sqlalchemy import SQLAlchemy # Library import to talk with database

# create obj DB globally
db=SQLAlchemy()

def create_app():  # create app
    app=Flask(__name__)   # import flask to create instance for flask app

    app.config["SECRET_KEY"]="malwarekey" # add secret key
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db' # SQL alchemy configuration
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # Track the User modification
    
    db.__init__(app) # connect db obj with app to use db.names etc

    from app.routes.auth import auth_bp # import auth blueprints
    from app.routes.task import task_bp # import auth blueprints

    app.register_blueprint(auth_bp)      # register auth blueprints and pass it 
    app.register_blueprint(task_bp)      # register task blueprints and pass it

    return app     # return the app to set in run.py 

