import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base



def mysql_session(db_dict):

    connection_string = 'mysql+pymysql://{}:{}@{}:{}'.format(db_dict['user'],
                                                             db_dict['pass'],
                                                             db_dict['host'],
                                                             db_dict['port'])

    engine = create_engine(connection_string, echo=True)
    engine.execute("USE {}".format(db_dict['schema']))
    Base.metadata.create_all(engine, checkfirst=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
