from flask import Flask, render_template, url_for, request, make_response, redirect
import json


app = Flask(__name__)


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
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(dict(request.form.items())))
    return response


if __name__ == '__main__':
    app.run(debug=True)
