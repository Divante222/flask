from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    first_list = ['Must have an uppercase letter somewhere.',
                  'Must have a lowercase letter somewhere',
                  'Must have a number at the end']
    return render_template('home_t.html', first_list = first_list)

@app.route('/requirements')
def requirements():
    first_dict = {1:'Must have an uppercase letter somewhere.',
                  2:'Must have a lowercase letter somewhere',
                  3:'Must have a number at the end'}
    
    userName = request.args.get('userInfo')

    has_upper = False
    has_lower = False
    num_end = False

    for item in userName:
        if item.isupper():
            has_upper = True
        if item.islower():
            has_lower = True

    if userName[-1].isnumeric():
        num_end = True
    
    total = int(has_lower) + int(has_upper) + int(num_end)

    if num_end:
        first_dict.pop(3)
    if has_lower:
        first_dict.pop(2)
    if has_upper:
        first_dict.pop(1)

    

    return render_template('requirements.html', userName = userName, total = total,first_dict = first_dict)

if __name__ == '__main__':
    app.run(debug=True)