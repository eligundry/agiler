import dataset
import yaml
from passlib.hash import bcrypt, md5_crypt

config = yaml.load(open('config.yml', 'r'))
connection = '%(engine)s://%(user)s:%(pass)s@%(host)s/%(database)s' % config['db']

class User:
    db = dataset.connect(connection)
    table = db['users']
    data = {}

    def __init__(self, user_id=None, email=None):
        if user_id is not None:
            self.data = self.table.find_one(id=user_id)

        if email is not None:
            self.data = self.table.find_one(email=email)

    def __contains__(self, x):
        return self.data.__contains__(x)

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

    def return_data(self):
        return {
            'first_name': self.data.first_name,
            'last_name': self.data.last_name,
            'user_id': str(self.data.id),
            'email': self.data.email,
            'access_token': self.get_access_token()
        }

class Category:
    db = dataset.connect(connection)
    table = db['categories']
    data = {}

    def __init__(self, category_id=None, name=None):
        if category_id is not None:
            self.data = self.table.find_one(id=category_id)
        elif name is not None:
            self.data = self.table.find_one(name=name)

    def create(self, name, color):
        if len(self.data):
            return False

        self.data = {
            'name': name,
            'color': color
        }

        self.table.insert(self.data)

    def get_all_categories(self):
        js = []
        cat = self.table.all()

        for c in cat:
            js.append(c)

        return js

class Event:
    db = dataset.connect(connection)
    table = db['events']
    data = {}

    def __init__(self, event_id=None, user_id=None):
        if event_id is not None:
            self.data = self.table.find_one(id=event_id)

        if user_id is not None:
            self.data = self.table.find(user_id=user_id)

    def create(self, user, category, name, recurring, time, duration):
        if len(self.data) is not 0:
            return False

        self.data = {
            'user': user,
            'category': category,
            'name': name,
            'recurring': recurring,
            'time': time,
            'duration': duration,
            'is_active': True
        }

        self.table.insert(self.data)

    def update(self):
        pass

    def delete(self):
        self.table.update({is_active: False})
