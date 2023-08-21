from models import db, Puppy, Owner, Toy, app



with app.app_context():
    #creating two puppies
    rufus = Puppy('Rufus')
    fido = Puppy('Fido')


    db.session.add(rufus)
    #add puppies to db
    db.session.add_all([rufus, fido])
    db.session.commit()

    print(Puppy.query.all())


    # grabbing the first pupy with rufus
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    # indexing works too
    # rufus = Puppy.query.filter_by(name='Rufus')[0]
    # rufus = Puppy.query.filter_by(name='Rufus').all()

    #crate owner object
    jose = Owner('Jose', rufus.id)

    #give rufus some toys
    toy1 = Toy('Chew Toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([jose,toy1,toy2])

    db.session.commit()

    #grab rufus after the additions
    rufus = Puppy.query.filter_by(name = 'Rufus').first()

    print(rufus)

    print(rufus.report_toys())

