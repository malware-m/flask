from flask_sqlalchemy import SQLALchemy # import sqlalchemy
db=SQLALchemy()      # create objects
db.init_app(app)     # pass in create_app

