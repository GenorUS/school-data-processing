from sqlalchemy import Column, String, Float, DateTime
# from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class JrnlPublicSchoolStaff(Base):

    __tablename__ = 'jrnl_public_school_staff'.lower()
    # if PROD_FLG:
    #     __table_args__ = {'schema': DB_PROD['schema']}
    # else:
    #     __table_args__ = {'schema': DB_DEV['schema']}

    SURVYEAR = Column('SURVYEAR', String(9))
    FIPST = Column('FIPST', String(2))
    STABR = Column('STABR', String(2))
    STATENAME = Column('STATENAME', String(44))
    SEANAME = Column('SEANAME', String(59))
    LEAID = Column('LEAID', String(7))
    ST_LEAID = Column('ST_LEAID', String(35))
    LEA_NAME = Column('LEA_NAME', String(60))
    SCHID = Column('SCHID', String(5))
    ST_SCHID = Column('ST_SCHID', String(45))
    NCESSCH = Column('NCESSCH', String(12), primary_key=True, index=True)
    SCH_NAME = Column('SCH_NAME', String(60))
    FTE = Column('FTE', Float)
    INSERTED_TS = Column("INSERTED_TS", DateTime)
    UPDATED_TS = Column("UPDATED_TS", DateTime)
