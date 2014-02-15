from flask import Flask, render_template
from flask.ext import restful
import yaml

app = Flask(__name__)
api = restful.Api(app)
config = yaml.load(open('config.yml', 'r+'))

@app.route('/')
def index():
    return render_template('index.html')

class Register(restful.Resource):
    def post(self):
        """
        Create a new user
        Returns user id and access key
        """
        pass

api.add_resource(Register, '/register')

class Login(restful.Resource):
    def post(self):
        """
        Login an existing user
        Returns user id and access key
        """
        pass

api.add_resource(Login, '/login')

class Event(restful.Resource):
    def get(self, event_id):
        """
        Gets a single event specified by an event_id
        Requires user_id and access_key
        """
        pass

    def put(self, event_id):
        """
        Updates existing event for user
        Requires user_id, access_key, and updated event details
        Returns updated event data
        """
        pass

    def delete(self, event_id):
        """
        Deletes existing event for user
        Required user_id and access_key
        Returns status code for deleted object
        """
        pass

api.add_resource(Event, '/events/<int:event_id>')

class EventList(restful.Resource):
    def get(self):
        """
        Gets all events for the user
        Requires user_id and access_key
        """
        pass

    def post(self):
        """
        Create new event for user
        Requires user_id, access_key, and event details
        Returns event data
        """
        pass

api.add_resource(EventList, '/events')

if __name__ == '__main__':
    app.run(debug=True)
