import dataset
from agiler import config

connection = '%(engine)s://%(user)s:%(pass)s@%(host)s/%(database)s' % config['db']

class User:
    def __init__(self):
        self.db = dataset.connect(connection)
        self.table = self.db['users']

    def create(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

        self.table.insert(dict(
            first_name = self.first_name,
            last_name = self.last_name,
            email = self.email,
            password = self.password
        ))

    def login(self, user_id, password):
        pass
