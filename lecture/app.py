from flask import Flask, render_template, url_for, request, make_response, redirect, flash
import json
from options import DEFAULTS


app = Flask(__name__)
app.secret_key = 'esauhou>UO>au.sh35@<Uouo52%@#ouo.42!@#42'

def get_saved_data():
    '''Get Data from cookies'''
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
@app.route('/index')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(dict(request.form.items())))
    return response


@app.route('/builder')
def builder():
    return render_template('builder.html', saves=get_saved_data(), options = DEFAULTS)


if __name__ == '__main__':
    app.run(debug=True)
