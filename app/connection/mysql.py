import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def mysql_engine(db_dict):
    connection_string = 'mysql+pymysql://{}:{}@{}:{}'.format(db_dict['user'],
                                                             db_dict['pass'],
                                                             db_dict['host'],
                                                             db_dict['port'])

    engine = create_engine(connection_string)
    return engine


def mysql_session(engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
