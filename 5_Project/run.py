
# DB will create here
# This file is engine of whole program
import sys
print(sys.path)


from app import create_app, db
from app.models import Task   # Flask will know which table create in DB

app=create_app()

with app.app_context():  # Tell flask which currently app is running
    db.create_all()      # tell flask loot at models(like task) and id DB file not exist create it

if __name__== '__main__':   # run this code if it running directly 
    app.run(debug=True)    # start development server and show errors

    