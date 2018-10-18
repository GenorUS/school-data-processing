import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base


def mysql_session(db_dict):
    print('wtf')
    connection_string = 'mysql+pymysql://{}:{}@{}:{}'.format(db_dict['user'],
                                                             db_dict['pass'],
                                                             db_dict['host'],
                                                             db_dict['port'])

    engine = create_engine(connection_string, echo=False)
    print('wtf2')
    Base.metadata.create_all(engine, checkfirst=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print('wtf3')
    return session
