# Always use name attribute in input to make sure flask understand it like username
# Always define method
# Make sure route path match with action

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["GET","POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

  # if username == "malware" and password == "malware":
   #     return render_template("welcome.html", name=username) */
  # if you have more then one user

    valid_users={
        'admin':'123',
        'malware':'112233',
        'ahsan':'rocky',
    }
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html",name=username)
    else: 
        return "Invalid Credentials"

    