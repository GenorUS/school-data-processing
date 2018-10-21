from sqlalchemy import Column, Float, DateTime, String
from .base import Base

# https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx


class JrnlCollegeActivity(Base):

    __tablename__ = 'jrnl_college_activity'.lower()

    UNITID = Column('UNITID', Float, primary_key=True, index=True)
    CDACTUA = Column('CDACTUA', Float)
    CNACTUA = Column('CNACTUA', Float)
    CDACTGA = Column('CDACTGA', Float)
    EFTEUG = Column('EFTEUG', Float)
    EFTEGD = Column('EFTEGD', Float)
    FTEUG = Column('FTEUG', Float)
    FTEGD = Column('FTEGD', Float)
    FTEDPP = Column('FTEDPP', Float)
    ACTTYPE = Column('ACTTYPE', Float)
    XCDACTUA = Column('XCDACTUA', String(1))
    XCNACTUA = Column('XCNACTUA', String(1))
    XCDACTGA = Column('XCDACTGA', String(1))
    XEFTEUG = Column('XEFTEUG', String(1))
    XEFTEGD = Column('XEFTEGD', String(1))
    XFTEUG = Column('XFTEUG', String(1))
    XFTEGD = Column('XFTEGD', String(1))
    XFTEDPP = Column('XFTEDPP', String(1))
    INSERTED_TS = Column("INSERTED_TS", DateTime)
    UPDATED_TS = Column("UPDATED_TS", DateTime)
