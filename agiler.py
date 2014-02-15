from flask import Flask, render_template, request, jsonify
from models import *
import yaml
import json

app = Flask(__name__)
config = yaml.load(open('config.yml', 'r'))

# RESTful Routes

@app.route('/api/register', methods=['POST'])
def api_register():
    """
    POST request that creates new user account
    Requires: first_name, last_name, email, password
    """
    a = request.form

    u = User()
    u.create(first_name=a['first_name'], last_name=a['last_name'], email=a['email'], password=a['password'])
    return send_json(u.return_data(), status_code=201)

@app.route('/api/login', methods=['POST'])
def api_login():
    """
    POST request that allows user to login
    Requires: email and password
    """
    u = User(email = request.form['email'])

    if len(u.data) is None:
        return send_error('User with that email does not exist', 404)

    if u.login(request.form['password']):
        return send_json(u.return_data(), status_code=200)
    else:
        return send_error('The password for that user is incorrect', 400)


@app.route('/api/events', methods=['GET', 'POST'])
def api_events():
    """
    A collection of routes for events

    GET: Returns a list of all user events
    POST: Create a new event for that user

    Requires: user_id and access_token
    """
    if request.method is 'GET':
        pass
    elif request.method is 'POST':
        pass

@app.route('/api/events/<int:event_id>', methods=['GET', 'DELETE', 'PUT'])
def api_event(event_id):
    """
    A collection of routes to do specific operations on an event

    GET: Returns details on an event
    DELETE: Marks the specified event as inactive and will not show up in searches
    PUT: Updates the specified event

    Requires: user_id and access_token
    """
    if request.method is 'GET':
        pass
    elif request.method is 'PUT':
        pass
    elif request.method is 'DELETE':
        pass

# Helper Methods

def send_json(data, status_code=200):
    resp = jsonify({'code': str(status_code), 'data': data})
    resp.status_code = status_code
    return resp

def send_error(error_message, status_code=500):
    resp = jsonify({'code': str(status_code), 'message': error_message})
    resp.status_code = status_code
    return resp

# HTML Routes

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
