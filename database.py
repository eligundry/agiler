from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(setup_database_connection(), convert_unicode=True)
db_session = scoped_session(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import agiler.models
    Base.metadata.create_all(bind=engine)

def setup_database_connection():
    from agiler import config
    return '%(engine)s://%(user)s:%(pass)s@%(host)s/%(database)s' % config['db']
