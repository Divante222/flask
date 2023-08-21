import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from basic import app, db, Puppy 
from basic import yes



#  CREATES ALL THE TABLES Model --> Db Table

with app.app_context():
    db.create_all()



    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    print(sam.id)
    print(frank.id)


    db.session.add_all([sam, frank])
    db.session.commit()
#can add it this way individually
# db.session.add(frank)

    print(sam.id)
    print(frank.id)
