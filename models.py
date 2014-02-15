import dataset
from passlib.hash import bcrypt, md5_crypt
from agiler import config

connection = '%(engine)s://%(user)s:%(pass)s@%(host)s/%(database)s' % config['db']

class User:
    self.db = dataset.connect(connection)
    self.table = self.db['users']
    self.data = {}

    def __init__(self, user_id=None, email=None):
        if user_id is not None:
            self.data = self.table.find_one(id=user_id)

        if email is not None:
            self.data = self.table.find_one(email=email)

    def create(self, first_name, last_name, email, password):
        if len(self.data) is not 0:
            return False

        self.data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': bcrypt.encrypt(password)
        }

        self.table.insert(self.data)

    def update(self):
        pass

    def login(self, password):
        return bcrypt.verify(password, self.data['password'])

    def get_access_token(self):
        return md5_crypt.encrypt(self.data['password'])

    def verify_access_token(self, access_token):
        return md5_crypt.verify(access_token, md5_crypt.encrypt(self.data['password']))

class Category:
    self.db = dataset.connect(connection)
    self.table = self.db['categories']
    self.data = {}

    def __init__(self, category_id=None, name=None):
        pass

    def create(self, name, color):
        self.data = {
            'name': name,
            'color': color
        }

        self.table.insert(self.data)


class Event:
    self.db = dataset.connect(connection)
    self.table = self.db['events']
    self.data = {}

    def __init__(self, event_id=None, user_id=None):
        if event_id is not None:
            self.data = self.table.find_one(id=event_id)

        if user_id is not None:
            self.data = self.table.find(user_id=user_id)

    def create(self, name, description, location, recurring, time, duration):
        if len(self.data) is not 0:
            return False

        self.data = {
            'name': name,
            'description': description,
            'location': location,
            'recurring': recurring,
            'time': time,
            'duration': duration
        }

        self.table.insert(self.data)

    def update(self):
        pass
