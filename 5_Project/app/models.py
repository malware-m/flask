
# Model Represent the table in database
from app import  db  # import sqlalchemy DB object that create in db.__init__(py)

class Task(db.Model): # convert this class into real DB task
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(15), default="Pending")

    
