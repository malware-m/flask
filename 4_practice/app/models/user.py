

# OVerview of models creation
'''

class user(db.model):
    id =db.id
    name =db.name
    address=db.address

'''

'''
Model (every class is table and variable become colum)
databtypes (what type of data in colums )
Relationship (how they link with eachother)


'''

from flask_sqlalchemy import SQLALchemy
db=SQLALchemy()

class user(db.model):  # create table in class
    id=db.column(db.Integer,primary_ley=True) # save integerdata
    name=db.column(db.string(20),nullable=False)
    email=db.column(db.string(40),UNIQUE=True)
    posts=db.relationship('post',backhref='author',lazy=True) # One to many relationship and connect this modal with other table.


# to search in databse etc
'''

user.query.all()
.filter_by()   

'''