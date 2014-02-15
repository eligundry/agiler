import dataset
from passlib.hash import bcrypt, md5_crypt
from agiler import config

connection = '%(engine)s://%(user)s:%(pass)s@%(host)s/%(database)s' % config['db']

class User:
    def __init__(self, user_id=None):
        self.db = dataset.connect(connection)
        self.table = self.db['users']
        self.data = {}

        if user_id is not None:
            self.data = self.table.find_one(id=user_id)

    def create(self, first_name, last_name, email, password):
        self.data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': bcrypt.encrypt(password)
        }

        self.table.insert(self.data)

    def login(self, email, password):
        user = self.table.find_one(email = email)

        if bcrypt.verify(password, user.data['password']):
            pass
        else:
            return False

    def get_access_token(self):
        return md5_crypt.encrypt(self.data['password'])

    def verify_access_token(self, access_token):
        return md5_crypt.verify(access_token, mdb5_crypt.encrypt(self.data['password']))

