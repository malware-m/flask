

# file that launch flask app

from app import create_app
app=create_app()   # call fun and take app object

 # file only execute when it run not when it import
if __name__=="__main__":
    app.run(debug=true)  # start with debug mode enable

