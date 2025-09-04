
# This file is brain of Flask

from flask import Flask, request   # to use flask features
app=Flask(__name__)  # tell flask this is main file

@app.route("/")      # @app mean flask app and its root decorator
def home():          # simple function
    return "Hello malware this is my first flask app"


@app.route("/contact")      # @app mean flask app and its root decorator
def contact():          # simple function
    return "Hello malware this is contact page"


@app.route("/about")      # @app mean flask app and its root decorator
def about():          # simple function
    return "Hello malware this is about page"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        return "You return data"
    else:
        return "You are viewing form"
