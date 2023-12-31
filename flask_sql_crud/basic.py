import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install flask-migrate

#grabs the whole filepath, this works on all operating systems
basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ ==> basic.py

app = Flask(__name__)

#sets the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')

#if there is an update you dont have to track all the changes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#setting up sql database
db = SQLAlchemy(app)


Migrate(app, db)


#########################################


class Puppy(db.Model):

    #manual tablename overwrite
    __tablename__ = 'puppies'


# primary key sets primary key column
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    

    def __repr__(self):
        # sets up a string representation of the instance of the row
        return f"Puppy {self.name} is {self.age} year/s old"

