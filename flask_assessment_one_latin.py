from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1] =='y':
        return f"<h1>Hi {name}! Your puppylatin name is {name}iful</h1>"
    else: 
        return f"<h1>Hi {name}! Your puppylatin name is {name}y</h1>"

@app.route('/rendered_template')
def test_html():
    return render_template('assesment_two.html')
    

if __name__ == '__main__':
    app.run(debug = True)