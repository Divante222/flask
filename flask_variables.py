from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    some_variable = "Jose"
    return render_template('flask_variables.html', my_variable =some_variable)

@app.route('/index_list')
def index_list():
    user_logged_in = True
    name = "Jose"
    letters = list(name)
    pup_dictionary = {'pup_name':'Sammy'}
    mylist = [1,2,3,4,5]

    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('flask_variables_2.html',user_logged_in = user_logged_in, puppies = puppies, mylist= mylist, name =name, letters = letters, 
                           pup_dictionary= pup_dictionary)


# 
if __name__ == "__main__":
    app.run(debug=True)