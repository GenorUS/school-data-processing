from sqlalchemy import Column, String, Float, DateTime
from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class JrnlPublicSchoolCharacteristics(Base):

    __tablename__ = 'jrnl_public_school_characteristics_ref'.lower()
    if PROD_FLG:
        __table_args__ = {'schema': DB_PROD['schema']}
    else:
        __table_args__ = {'schema': DB_DEV['schema']}

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
    TITLEI_TEXT = Column('TITLEI_TEXT', String(63))
    TITLEI_STATUS = Column('TITLEI_STATUS', String(2))
    TITLEI = Column('TITLEI', String(14))
    STITLEI = Column('STITLEI', String(14))
    SHARED_TIME = Column('SHARED_TIME', String(7))
    MAGNET_TEXT = Column('MAGNET_TEXT', String(14))
    NSLPSTATUS_TEXT = Column('NSLPSTATUS_TEXT', String(57))
    NSLPSTATUS_CODE = Column('NSLPSTATUS_CODE', String(3))
    INSERTED_TS = Column("INSERTED_TS", DateTime)
    UPDATED_TS = Column("UPDATED_TS", DateTime)