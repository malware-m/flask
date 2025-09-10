
from flask import Flask
from router.auth import auth_bp  # login blueprint

def create_app():
    app=Flask(__name__)  # its locally 
    app.secret.eky="secret_key"  # session secret key
    app.register_blueprint(auth_bp)  # register page blueprint
    return app