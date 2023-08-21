from basic import app, db, Puppy

## create ##

with app.app_context():
    my_puppy = Puppy('Rufus', 5)

    db.session.add(my_puppy)

    db.session.commit()

    ## READ ##
    #returns a list of the puppy object in the table

    all_puppies = Puppy.query.all()
    print(all_puppies)


    # SELECT BY ID
    puppy_one = Puppy.query.get(1)
    print(puppy_one.name)

    puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
    print(puppy_frankie.all())

    first_puppy = Puppy.query.get(1)

    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()


    second_pup = Puppy.query.get(2)
    db.session.delete(second_pup)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(all_puppies)