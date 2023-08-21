from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
RadioField, SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    ## if you want to add validators they are in wtforms.validators
    breed = StringField('What breed are you', validators =[DataRequired()])
    neutered = BooleanField('Have you been neutered?')


    #note that the choices are pass in as a list containing tuple pairs (value, what the user sees)
    mood = RadioField('Please choose your mood: ', choices=[('mood_one', 'Happy'), ("mood_two", 'Excited')])

    # if you dont make this a unicode string you might get errors
    food_choice = SelectField(u'Pick your favorite food:', 
                              choices=[('chi', 'Chicken'), ('bf','Beef'),
                                       ('fish', 'Fish')])
    
    feedback = TextAreaField()
    submit = SubmitField('submit')


@app.route('/', methods = ['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    
    return render_template('index.html', form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(debug=True)



