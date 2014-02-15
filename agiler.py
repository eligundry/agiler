from flask import Flask, render_template
import models
import yaml

app = Flask(__name__)
config = yaml.load(open('config.yml', 'r'))

# RESTful Routes

@app.route('/api/register')
def api_register():
    """
    POST request that creates new user account
    Requires: first_name, last_name, email, password
    """
    pass

@app.route('/api/login')
def api_login():
    """
    POST request that allows user to login
    Requires: email and password
    """
    pass

@app.route('/api/events')
def api_events():
    """
    A collection of routes for events

    GET: Returns a list of all user events
    POST: Create a new event for that user

    Requires: user_id and access_token
    """
    pass

@app.route('/api/events/<int:event_id>')
def api_event():
    """
    A collection of routes to do specific operations on an event

    GET: Returns details on an event
    DELETE: Marks the specified event as inactive and will not show up in searches
    PUT: Updates the specified event

    Requires: user_id and access_token
    """
    pass

# HTML Routes

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
