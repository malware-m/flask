
# login page
# Accep credentials
# session store
# redirect welcome page
# logout 


# python -m venv venv
# venv\script\activate

from flask import Flask,request, redirect, url_for,session,Response
app = Flask(__name__)
app.secret_key="supersecret"  # help to use sessions securly and log session 
# if secret key not use flask no allow to use session

# home login Page
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
     username = request.form.get("username")
     password = request.form.get("password")

     if username == "malware" and password == "malware":
        session["user"]=username  # saved user session data 
        return redirect(url_for("home")) # we cant define a route inside a function and url_for redirect to page
       
     else:
        return Response("Invalid credentials",mimetype="text/plain") # Tell browser what kind of content sent in return
         # response help to customize this more or we can also use only return
   
    return '''<h2>Login Page</h2><form method="POST">username:<input type="text" name="username"><br><form method="POST">password:<input type="text" name="password"><br><input type="submit" value="login"></form>
           '''

# Welcome page after login
@app.route("/home")
def home():
   if "user" in session:  # if user data is in session
       # return data in formated string
      return f'''       
      <h2>Weclome , {session["user"]}!</h2> 
      <a href={url_for ('logout')}>Logout</a>
'''
   return redirect(url_for("login"))

@app.route("/logout")
def logout():
   session.pop("user",None)   # remove session key from user and if user not in session None will prevent us
   return redirect(url_for("login"))