from flask import Flask
#creating an application object with the name of the file being passed in
app = Flask(__name__)


#default page or index or home
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'


#second page information after the slash
@app.route('/information')
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "Upper Case: {}".format(name.upper())


@app.route('/puppy2/<name>')
def puppy_2(name):
    return "100th letter: {}".format(name[100])

#if I am running this script run my application
if __name__ == '__main__':
    app.run(debug=True)

