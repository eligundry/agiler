from flask import Flask, Blueprint, render_template
import yaml

app = Flask(__name__)
config = yaml.load(open('config.yml', 'r+'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    """
    Create a new user
    Returns user id and access key
    POST method
    """
    pass

@app.route('/login')
def login():
    """
    Login an existing user
    Returns user id and access key
    POST method
    """
    pass

@app.route('/events')
def get_all_events():
    """
    Returns all events for a user
    Requires user_id and event key
    """
    pass

@app.route('/event/<int:event_id>')
def get_single_event(event_id):
    """
    """
    pass

@app.route('/event/new')
def new_event():
    """
    Create new event for user
    Requires user_id, access_key, and event details
    Returns event data
    """
    pass

@app.route('/event/update')
def update_event():
    """
    Updates existing event for user
    Requires user_id, access_key, and updated event details
    Returns updated event data
    """
    pass

@app.route('/event/delete')
def delete_event():
    """
    Deletes existing event for user
    Required user_id and access_key
    Returns status code for deleted object
    """
    pass

if __name__ == '__main__':
    app.run(debug=True)
